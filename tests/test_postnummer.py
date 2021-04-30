
import pytest

from dawa import API

def test_postnummer_initial():

    api = API()

    postnummer = api.replicate('postnummer')

    for obj in postnummer:
        assert len(obj) != 0
        break

def test_postnummer_changes():

    api = API()

    postnummer = api.replicate('postnummer', txidfra=3432423, txidtil=3432423)

    for obj in postnummer:
        assert len(obj) != 0
        break
