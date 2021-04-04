import pytest

from dawa import API

def test_vejstykker_initial():

    api = API()

    vejstykker = api.replicate('vejstykke')

    for obj in vejstykker:
        assert 'id' in obj
        break

def test_vejstykker_changes():

    api = API()

    vejstykker = api.replicate('vejstykke', txidfra=3432423, txidtil=3432423)

    for obj in vejstykker:
        assert 'id' in obj
        break