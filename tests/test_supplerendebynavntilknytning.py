
import pytest

from dawa import API

def test_supplerendebynavntilknytning_initial():

    api = API()

    supplerendebynavntilknytning = api.replicate('supplerendebynavntilknytning')

    for obj in supplerendebynavntilknytning:
        assert len(obj) != 0
        break

def test_supplerendebynavntilknytning_changes():

    api = API()

    supplerendebynavntilknytning = api.replicate('supplerendebynavntilknytning', txidfra=3432423, txidtil=3432423)

    for obj in supplerendebynavntilknytning:
        assert len(obj) != 0
        break
