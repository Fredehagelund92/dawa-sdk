
import pytest

from dawa import API

def test_stedtilknytning_initial():

    api = API()

    stedtilknytning = api.replicate('stedtilknytning')

    for obj in stedtilknytning:
        assert len(obj) != 0
        break

def test_stedtilknytning_changes():

    api = API()

    stedtilknytning = api.replicate('stedtilknytning', txidfra=3432423, txidtil=3432423)

    for obj in stedtilknytning:
        assert len(obj) != 0
        break
