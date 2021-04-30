
import pytest

from dawa import API

def test_sognetilknytning_initial():

    api = API()

    sognetilknytning = api.replicate('sognetilknytning')

    for obj in sognetilknytning:
        assert len(obj) != 0
        break

def test_sognetilknytning_changes():

    api = API()

    sognetilknytning = api.replicate('sognetilknytning', txidfra=3432423, txidtil=3432423)

    for obj in sognetilknytning:
        assert len(obj) != 0
        break
