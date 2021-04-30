
import pytest

from dawa import API

def test_storkredstilknytning_initial():

    api = API()

    storkredstilknytning = api.replicate('storkredstilknytning')

    for obj in storkredstilknytning:
        assert len(obj) != 0
        break

def test_storkredstilknytning_changes():

    api = API()

    storkredstilknytning = api.replicate('storkredstilknytning', txidfra=3432423, txidtil=3432423)

    for obj in storkredstilknytning:
        assert len(obj) != 0
        break
