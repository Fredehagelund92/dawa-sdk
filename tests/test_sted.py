
import pytest

from dawa import API

def test_sted_initial():

    api = API()

    sted = api.replicate('sted')

    for obj in sted:
        assert len(obj) != 0
        break

def test_sted_changes():

    api = API()

    sted = api.replicate('sted', txidfra=3432423, txidtil=3432423)

    for obj in sted:
        assert len(obj) != 0
        break
