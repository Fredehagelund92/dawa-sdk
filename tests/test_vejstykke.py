import pytest

from dawa import API

def test_vejstykker_initial():

    api = API()

    vejstykker = api.get('vejstykke', txid=None)

    assert len(vejstykker) > 0

def test_vejstykker_changes():

    api = API()

    vejstykker = api.get('vejstykke', txidfra=3432423, txidtil=3432423)

    assert len(vejstykker) >= 0