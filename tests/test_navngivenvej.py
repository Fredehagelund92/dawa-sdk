
import pytest

from dawa import API

def test_navngivenvej_initial():

    api = API()

    navngivenvej = api.replicate('navngivenvej')

    for obj in navngivenvej:
        assert len(obj) != 0
        break

def test_navngivenvej_changes():

    api = API()

    navngivenvej = api.replicate('navngivenvej', txidfra=3432423, txidtil=3432423)

    for obj in navngivenvej:
        assert len(obj) != 0
        break
