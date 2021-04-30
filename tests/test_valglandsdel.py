
import pytest

from dawa import API

def test_valglandsdel_initial():

    api = API()

    valglandsdel = api.replicate('valglandsdel')

    for obj in valglandsdel:
        assert len(obj) != 0
        break

def test_valglandsdel_changes():

    api = API()

    valglandsdel = api.replicate('valglandsdel', txidfra=3432423, txidtil=3432423)

    for obj in valglandsdel:
        assert len(obj) != 0
        break
