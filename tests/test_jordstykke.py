
import pytest

from dawa import API

def test_jordstykke_initial():

    api = API()

    jordstykke = api.replicate('jordstykke')

    for obj in jordstykke:
        assert len(obj) != 0
        break

def test_jordstykke_changes():

    api = API()

    jordstykke = api.replicate('jordstykke', txidfra=3432423, txidtil=3432423)

    for obj in jordstykke:
        assert len(obj) != 0
        break
