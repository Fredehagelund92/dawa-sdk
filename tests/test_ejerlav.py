
import pytest

from dawa import API

def test_ejerlav_initial():

    api = API()

    ejerlav = api.replicate('ejerlav')

    for obj in ejerlav:
        assert len(obj) != 0
        break

def test_ejerlav_changes():

    api = API()

    ejerlav = api.replicate('ejerlav', txidfra=3432423, txidtil=3432423)

    for obj in ejerlav:
        assert len(obj) != 0
        break
