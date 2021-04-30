
import pytest

from dawa import API

def test_zonetilknytning_initial():

    api = API()

    zonetilknytning = api.replicate('zonetilknytning')

    for obj in zonetilknytning:
        assert len(obj) != 0
        break

def test_zonetilknytning_changes():

    api = API()

    zonetilknytning = api.replicate('zonetilknytning', txidfra=3432423, txidtil=3432423)

    for obj in zonetilknytning:
        assert len(obj) != 0
        break
