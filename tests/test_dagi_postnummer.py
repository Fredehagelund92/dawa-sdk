
import pytest

from dawa import API

def test_dagi_postnummer_initial():

    api = API()

    dagi_postnummer = api.replicate('dagi_postnummer')

    for obj in dagi_postnummer:
        assert len(obj) != 0
        break

def test_dagi_postnummer_changes():

    api = API()

    dagi_postnummer = api.replicate('dagi_postnummer', txidfra=3432423, txidtil=3432423)

    for obj in dagi_postnummer:
        assert len(obj) != 0
        break
