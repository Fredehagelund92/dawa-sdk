
import pytest

from dawa import API

def test_menighedsrådsafstemningsområdetilknytning_initial():

    api = API()

    menighedsrådsafstemningsområdetilknytning = api.replicate('menighedsrådsafstemningsområdetilknytning')

    for obj in menighedsrådsafstemningsområdetilknytning:
        assert len(obj) != 0
        break

def test_menighedsrådsafstemningsområdetilknytning_changes():

    api = API()

    menighedsrådsafstemningsområdetilknytning = api.replicate('menighedsrådsafstemningsområdetilknytning', txidfra=3432423, txidtil=3432423)

    for obj in menighedsrådsafstemningsområdetilknytning:
        assert len(obj) != 0
        break
