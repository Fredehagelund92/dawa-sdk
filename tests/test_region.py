
import pytest

from dawa import API

def test_region_initial():

    api = API()

    region = api.replicate('region')

    for obj in region:
        assert len(obj) != 0
        break

def test_region_changes():

    api = API()

    region = api.replicate('region', txidfra=3432423, txidtil=3432423)

    for obj in region:
        assert len(obj) != 0
        break
