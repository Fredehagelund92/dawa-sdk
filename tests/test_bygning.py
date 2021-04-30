
import pytest

from dawa import API

def test_bygning_initial():

    api = API()

    bygning = api.replicate('bygning')

    for obj in bygning:
        assert len(obj) != 0
        break

def test_bygning_changes():

    api = API()

    bygning = api.replicate('bygning', txidfra=3432423, txidtil=3432423)

    for obj in bygning:
        assert len(obj) != 0
        break
