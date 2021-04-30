
import pytest

from dawa import API

def test_politikredstilknytning_initial():

    api = API()

    politikredstilknytning = api.replicate('politikredstilknytning')

    for obj in politikredstilknytning:
        assert len(obj) != 0
        break

def test_politikredstilknytning_changes():

    api = API()

    politikredstilknytning = api.replicate('politikredstilknytning', txidfra=3432423, txidtil=3432423)

    for obj in politikredstilknytning:
        assert len(obj) != 0
        break
