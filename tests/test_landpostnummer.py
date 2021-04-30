
import pytest

from dawa import API

def test_landpostnummer_initial():

    api = API()

    landpostnummer = api.replicate('landpostnummer')

    for obj in landpostnummer:
        assert len(obj) != 0
        break

def test_landpostnummer_changes():

    api = API()

    landpostnummer = api.replicate('landpostnummer', txidfra=3432423, txidtil=3432423)

    for obj in landpostnummer:
        assert len(obj) != 0
        break
