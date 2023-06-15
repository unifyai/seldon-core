# [Language Wrappers](https://docs.seldon.io/projects/seldon-core/en/latest/workflow/overview.html#language-wrappers)

1. 
`make run_local` or `seldon-core-microservice SimpleConvNet --service-type MODEL`
```
curl http://localhost:9000/api/v1.0/predictions \
    -H 'Content-Type: application/json' \
    -d '{"data": {"ndarray":"samples/1.png"}}'
```
2. 
```
s2i build . seldonio/seldon-core-s2i-python3:1.17.0-dev model:0.1
```
