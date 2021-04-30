
import pytest

from dawa import API

def test_supplerendebynavn_initial():

    api = API()

    supplerendebynavn = api.replicate('supplerendebynavn')

    for obj in supplerendebynavn:
        assert len(obj) != 0
        break

def test_supplerendebynavn_changes():

    api = API()

    supplerendebynavn = api.replicate('supplerendebynavn', txidfra=3432423, txidtil=3432423)

    for obj in supplerendebynavn:
        assert len(obj) != 0
        break
