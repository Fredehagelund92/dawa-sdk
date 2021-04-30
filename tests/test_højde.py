
import pytest

from dawa import API

def test_højde_initial():

    api = API()

    højde = api.replicate('højde')

    for obj in højde:
        assert len(obj) != 0
        break

def test_højde_changes():

    api = API()

    højde = api.replicate('højde', txidfra=3432423, txidtil=3432423)

    for obj in højde:
        assert len(obj) != 0
        break
