# dawa-python
===================
#### Python - Dawa API

**dawa-python** is a simple client for dawa api. It uses [Dawa Web API](https://dawa.aws.dk/dok/api).

## Installation
``` 
sudo pip install dawa-python
```

## Using
```python
from dawa import API
api = API()
```

## References
```python
# Get current txid
txid = api.txid() # 3340338

# Get initial replication
vejstykke = api.get('vejstykke')

# Get latest changes 
txid = api.txid() # 3340339
vejstykke = api.get('vejstykke', txid='3340338')

```



## Contributing
[https://github.com/Fredehagelund92/dawa-python](https://github.com/Fredehagelund92/dawa-python)

## Dawa Web API
[Dawa Web API Doc](https://dawa.aws.dk/dok/api)
