# [Language Wrappers](https://docs.seldon.io/projects/seldon-core/en/latest/workflow/overview.html#language-wrappers)

1. 
`make run_local` or `seldon-core-microservice SimpleConvNet --service-type MODEL`
```
curl http://localhost:9000/api/v1.0/predictions \
    -H 'Content-Type: application/json' \
    -d '{"data": {"ndarray":"samples/1.png"}}'
```
2. 
To create the docker, you can either use s2i or Docker according to [here](https://docs.seldon.io/projects/seldon-core/en/latest/python/python_component.html#next-steps). We'll go with s2i for this demo but here's the Seldon Docker [docs](https://docs.seldon.io/projects/seldon-core/en/latest/python/python_wrapping_docker.html) to explore
```
s2i build . seldonio/seldon-core-s2i-python3:1.17.0-dev ivy_model:0.1
```
or (untested)
```
docker build . -t ivy_model:0.1
```

