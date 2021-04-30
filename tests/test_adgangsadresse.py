
import pytest

from dawa import API

def test_adgangsadresse_initial():

    api = API()

    adgangsadresse = api.replicate('adgangsadresse')

    for obj in adgangsadresse:
        assert len(obj) != 0
        break

def test_adgangsadresse_changes():

    api = API()

    adgangsadresse = api.replicate('adgangsadresse', txidfra=3432423, txidtil=3432423)

    for obj in adgangsadresse:
        assert len(obj) != 0
        break
