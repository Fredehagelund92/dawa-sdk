# dawa-sdk
===================
#### Python - Dawa API

**dawa-sdk** is a simple client for dawa api. It uses [Dawa Web API](https://dawadocs.dataforsyningen.dk/dok/api. It is mainly designed for data replication, but will at later stages include search.



## Installation
```
pip install dawa-sdk
```

## Using
```python
from dawa import API
api = API()
```

## Replication

```python
def replicate():
    # Due to the amount of data on some endpoint, this returns a generator
```

```python
def txid():
    # Returns an integer
```



### Usage
```python
# Get current txid and store somewhere
txid = api.txid()

# Get initial replication
vejstykke = api.replicate('vejstykke')

# Get latest txid and check if it is greater than previous
txid = api.txid()

# if yes get all the changes between last and current txid
vejstykke = api.replicate('vejstykke', txidfra='3340338', txidtil='3340338')


# It is also possible to get data from a single txid
vejstykke = api.replicate('vejstykke', txid='3340338')

```




## Search
```python
Not implemented yet
```




## Contributing
[https://github.com/Fredehagelund92/dawa-python](https://github.com/Fredehagelund92/dawa-sdk)

## Dawa Web API
[Dawa Web API Doc](https://dawadocs.dataforsyningen.dk/dok/api)
