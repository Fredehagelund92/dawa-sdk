# dawa-python
===================
#### Python - Dawa API

**dawa-python** is a simple client for dawa api. It uses [Dawa Web API](https://dawa.aws.dk/dok/api).

## Installation
``` 
sudo pip install youtube-python
```

## Using
```python
from dawa import API
api = API()
```

## References
```python
txid = api.txid()
vejstykke = api.get('vejstykke', id='B7FJV9KIn58')
```



## Contributing
[https://github.com/Fredehagelund92/dawa-python](https://github.com/Fredehagelund92/dawa-python)

## Dawa Web API
[Dawa Web API Doc](https://dawa.aws.dk/dok/api)
