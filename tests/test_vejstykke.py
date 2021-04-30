
import pytest

from dawa import API

def test_vejstykke_initial():

    api = API()

    vejstykke = api.replicate('vejstykke')

    for obj in vejstykke:
        assert len(obj) != 0
        break

def test_vejstykke_changes():

    api = API()

    vejstykke = api.replicate('vejstykke', txidfra=3432423, txidtil=3432423)

    for obj in vejstykke:
        assert len(obj) != 0
        break
