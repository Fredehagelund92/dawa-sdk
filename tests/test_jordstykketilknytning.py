
import pytest

from dawa import API

def test_jordstykketilknytning_initial():

    api = API()

    jordstykketilknytning = api.replicate('jordstykketilknytning')

    for obj in jordstykketilknytning:
        assert len(obj) != 0
        break

def test_jordstykketilknytning_changes():

    api = API()

    jordstykketilknytning = api.replicate('jordstykketilknytning', txidfra=3432423, txidtil=3432423)

    for obj in jordstykketilknytning:
        assert len(obj) != 0
        break
