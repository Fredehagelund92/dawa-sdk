
import pytest

from dawa import API

def test_stednavntilknytning_initial():

    api = API()

    stednavntilknytning = api.replicate('stednavntilknytning')

    for obj in stednavntilknytning:
        assert len(obj) != 0
        break

def test_stednavntilknytning_changes():

    api = API()

    stednavntilknytning = api.replicate('stednavntilknytning', txidfra=3432423, txidtil=3432423)

    for obj in stednavntilknytning:
        assert len(obj) != 0
        break
