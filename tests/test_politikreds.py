
import pytest

from dawa import API

def test_politikreds_initial():

    api = API()

    politikreds = api.replicate('politikreds')

    for obj in politikreds:
        assert len(obj) != 0
        break

def test_politikreds_changes():

    api = API()

    politikreds = api.replicate('politikreds', txidfra=3432423, txidtil=3432423)

    for obj in politikreds:
        assert len(obj) != 0
        break
