
import pytest

from dawa import API

def test_ikke_brofast_husnummer_initial():

    api = API()

    ikke_brofast_husnummer = api.replicate('ikke_brofast_husnummer')

    for obj in ikke_brofast_husnummer:
        assert len(obj) != 0
        break

def test_ikke_brofast_husnummer_changes():

    api = API()

    ikke_brofast_husnummer = api.replicate('ikke_brofast_husnummer', txidfra=3432423, txidtil=3432423)

    for obj in ikke_brofast_husnummer:
        assert len(obj) != 0
        break
