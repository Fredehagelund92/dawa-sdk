
import pytest

from dawa import API

def test_storkreds_initial():

    api = API()

    storkreds = api.replicate('storkreds')

    for obj in storkreds:
        assert len(obj) != 0
        break

def test_storkreds_changes():

    api = API()

    storkreds = api.replicate('storkreds', txidfra=3432423, txidtil=3432423)

    for obj in storkreds:
        assert len(obj) != 0
        break
