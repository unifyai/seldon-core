SHELL := /bin/bash
VERSION := $(shell cat ../../../version.txt)
IMAGE_NAME_BASE=ivyserver
IMAGE_NAME=${IMAGE_NAME_BASE}
KIND_NAME ?= kind

run_local:
	export PREDICTIVE_UNIT_PARAMETERS='[{"type":"STRING","name":"model_uri","value":"file://'${PWD}'/artifacts"}]' && cd ivyserver && seldon-core-microservice --service-type MODEL IvyServer


build:
	s2i build \
		-E environment \
		./ivyserver \
		seldonio/seldon-core-s2i-python3:${VERSION} \
		${IMAGE_NAME}:${VERSION}

run_docker:
	docker run -it --rm -p 9000:9000 -e PREDICTIVE_UNIT_PARAMETERS='[{"type":"STRING","name":"model_uri","value":"file:///models"}]' -v ${PWD}/artifacts:/models ${IMAGE_NAME}:${VERSION}

push:
	docker push ${IMAGE_NAME}:${VERSION}

kind_load:
	kind load -v 3 docker-image ${IMAGE_NAME}:${VERSION} --name ${KIND_NAME}

