import pytest

from dawa import API

def test_postnummer_initial():

    api = API()

    postnummer = api.get('postnummer')
    assert len(postnummer) > 0

def test_postnummer_changes():

    api = API()

    postnummer = api.get('postnummer', txidfra=3432423, txidtil=3432423)
    assert len(postnummer) >= 0