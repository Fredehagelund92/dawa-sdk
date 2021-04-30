
import pytest

from dawa import API

def test_retskreds_initial():

    api = API()

    retskreds = api.replicate('retskreds')

    for obj in retskreds:
        assert len(obj) != 0
        break

def test_retskreds_changes():

    api = API()

    retskreds = api.replicate('retskreds', txidfra=3432423, txidtil=3432423)

    for obj in retskreds:
        assert len(obj) != 0
        break
