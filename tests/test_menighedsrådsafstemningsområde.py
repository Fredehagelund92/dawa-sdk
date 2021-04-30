
import pytest

from dawa import API

def test_menighedsrådsafstemningsområde_initial():

    api = API()

    menighedsrådsafstemningsområde = api.replicate('menighedsrådsafstemningsområde')

    for obj in menighedsrådsafstemningsområde:
        assert len(obj) != 0
        break

def test_menighedsrådsafstemningsområde_changes():

    api = API()

    menighedsrådsafstemningsområde = api.replicate('menighedsrådsafstemningsområde', txidfra=3432423, txidtil=3432423)

    for obj in menighedsrådsafstemningsområde:
        assert len(obj) != 0
        break
