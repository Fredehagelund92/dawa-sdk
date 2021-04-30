
import pytest

from dawa import API

def test_adresse_initial():

    api = API()

    adresse = api.replicate('adresse')

    for obj in adresse:
        assert len(obj) != 0
        break

def test_adresse_changes():

    api = API()

    adresse = api.replicate('adresse', txidfra=3432423, txidtil=3432423)

    for obj in adresse:
        assert len(obj) != 0
        break
