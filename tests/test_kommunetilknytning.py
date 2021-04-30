
import pytest

from dawa import API

def test_kommunetilknytning_initial():

    api = API()

    kommunetilknytning = api.replicate('kommunetilknytning')

    for obj in kommunetilknytning:
        assert len(obj) != 0
        break

def test_kommunetilknytning_changes():

    api = API()

    kommunetilknytning = api.replicate('kommunetilknytning', txidfra=3432423, txidtil=3432423)

    for obj in kommunetilknytning:
        assert len(obj) != 0
        break
