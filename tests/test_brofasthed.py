
import pytest

from dawa import API

def test_brofasthed_initial():

    api = API()

    brofasthed = api.replicate('brofasthed')

    for obj in brofasthed:
        assert len(obj) != 0
        break

def test_brofasthed_changes():

    api = API()

    brofasthed = api.replicate('brofasthed', txidfra=3432423, txidtil=3432423)

    for obj in brofasthed:
        assert len(obj) != 0
        break
