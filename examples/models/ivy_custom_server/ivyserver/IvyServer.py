import yaml
import os
import logging
import requests
import ivy
import importlib.util

from seldon_core import Storage
from seldon_core.user_model import SeldonComponent
from typing import Dict, List, Union

logger = logging.getLogger()

IVY_MODEL = 'model.py'
IVY_WEIGHTS = "model.pkl"

class IvyServer(SeldonComponent):
    def __init__(self, model_uri: str, xtype: str = "ivy.array"):
        super().__init__()
        logger.info(f"Creating Ivy server with URI {model_uri}")
        logger.info(f"xtype: {xtype}")
        self.model_uri = model_uri
        self.xtype = xtype
        self.ready = False
        self.column_names = None
    
    def load(self):
        logger.info(f"Loading model from {self.model_uri}")
        # specify a local folder to get model with file://
        model_folder = Storage.download(self.model_uri)
        model_file = os.path.join(model_folder, IVY_MODEL)
        model_weights = os.path.join(model_folder, IVY_WEIGHTS)
        # TODO: this is very band aid-y. needs a more dynamic approach
        # rishab: look into this after getting this POC running
        # also, lint fixes definitely needed
        spec = importlib.util.spec_from_file_location('models', model_file)
        custom_module = importlib.util.module_from_spec(spec)
        ivy.set_backend(custom_module.backend)
        spec.loader.exec_module(custom_module)
        self._model = custom_module.Regressor(custom_module.input_dim, 
                                              custom_module.output_dim,
                                              is_training=False)
        self._model.v = ivy.Container.cont_from_disk_as_pickled(model_weights)
        self.ready = True

    def predict(
            self,
            X,
            meta: Dict = None
    ) -> Union[ivy.array, List, Dict, str, bytes]:
        
        logger.debug(f"Requesting prediction with: {X}")

        if not self.ready:
            raise requests.HTTPError("Model not loaded yet")
        
        if self.xtype == "ivy.array":
            result = self._model(X)
        else:
            X = ivy.array(X)
            result = self._model(X)
        
        logger.debug(f"Prediction result: {result}")
        return result
    
    def init_metadata(self):
        file_path = os.path.join(self.model_uri, "metadata.yaml")

        try:
            with open(file_path, "r") as f:
                return yaml.safe_load(f.read())
        except FileNotFoundError:
            logger.debug(f"metadata file {file_path} does not exist")
            return {}
        except yaml.YAMLError:
            logger.error(
                f"metadata file {file_path} present but does not contain valid yaml"
            )
            return {}
