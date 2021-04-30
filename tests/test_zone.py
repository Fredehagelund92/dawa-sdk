
import pytest

from dawa import API

def test_zone_initial():

    api = API()

    zone = api.replicate('zone')

    for obj in zone:
        assert len(obj) != 0
        break

def test_zone_changes():

    api = API()

    zone = api.replicate('zone', txidfra=3432423, txidtil=3432423)

    for obj in zone:
        assert len(obj) != 0
        break
