assuming kubernetes is [installed](https://docs.seldon.io/projects/seldon-core/en/latest/nav/installation.html) locally - 
```
kubectl port-forward -n istio-system svc/istio-ingressgateway 8080:80

kubectl port-forward $(kubectl get pods -l istio=ingressgateway -n istio-system -o jsonpath='{.items[0].metadata.name}') -n istio-system 8003:8080


make build

push
```