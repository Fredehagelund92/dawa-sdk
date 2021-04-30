
import pytest

from dawa import API

def test_regionstilknytning_initial():

    api = API()

    regionstilknytning = api.replicate('regionstilknytning')

    for obj in regionstilknytning:
        assert len(obj) != 0
        break

def test_regionstilknytning_changes():

    api = API()

    regionstilknytning = api.replicate('regionstilknytning', txidfra=3432423, txidtil=3432423)

    for obj in regionstilknytning:
        assert len(obj) != 0
        break
