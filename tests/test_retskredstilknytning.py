
import pytest

from dawa import API

def test_retskredstilknytning_initial():

    api = API()

    retskredstilknytning = api.replicate('retskredstilknytning')

    for obj in retskredstilknytning:
        assert len(obj) != 0
        break

def test_retskredstilknytning_changes():

    api = API()

    retskredstilknytning = api.replicate('retskredstilknytning', txidfra=3432423, txidtil=3432423)

    for obj in retskredstilknytning:
        assert len(obj) != 0
        break
