import pytest

from dawa import API

def test_txid():

    api = API()

    txid = api.txid()
    assert type(txid) is int