# [Language Wrappers](https://docs.seldon.io/projects/seldon-core/en/latest/workflow/overview.html#language-wrappers)

1. 
Run microservice - 
```
seldon-core-microservice SimpleConvNet --service-type MODEL
```
Test microservice with quick inference - 
```
curl http://localhost:9000/api/v1.0/predictions \
    -H 'Content-Type: application/json' \
    -d '{"data": {"ndarray":"samples/1.png"}}'
```
2. 
Set up and install Seldon Core in a Kubernetes cluster running on your local machine by following Seldon [docs](https://docs.seldon.io/projects/seldon-core/en/latest/install/kind.html#install-cluster-ingress)  
3.  
To create the docker, you can either use s2i or Docker according to [here](https://docs.seldon.io/projects/seldon-core/en/latest/python/python_component.html#next-steps). We'll go with s2i for this demo but here's the Seldon Docker [docs](https://docs.seldon.io/projects/seldon-core/en/latest/python/python_wrapping_docker.html) to explore
```
s2i build . seldonio/seldon-core-s2i-python3:1.17.0-dev ivy_model:0.1
```
or (untested)
```
docker build . -t ivy_model:0.1
```
4. 
Deploy it to our Seldon Core Kubernetes Cluster
```
kubectl apply -f ivy_server.yml
# seldondeployment.machinelearning.seldon.io/ivy-deployment-example created
```
    - Quick delete resource - `kubectl delete -f ivy_server.yml`
5.
Check deployment status. You should get `"state": "Available"` - 
```
kubectl get sdep ivy-deployment-example -o json --namespace default | jq .status
```