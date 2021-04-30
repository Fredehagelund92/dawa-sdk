
import pytest

from dawa import API

def test_vejpunkt_initial():

    api = API()

    vejpunkt = api.replicate('vejpunkt')

    for obj in vejpunkt:
        assert len(obj) != 0
        break

def test_vejpunkt_changes():

    api = API()

    vejpunkt = api.replicate('vejpunkt', txidfra=3432423, txidtil=3432423)

    for obj in vejpunkt:
        assert len(obj) != 0
        break
