
import pytest

from dawa import API

def test_vejmidte_initial():

    api = API()

    vejmidte = api.replicate('vejmidte')

    for obj in vejmidte:
        assert len(obj) != 0
        break

def test_vejmidte_changes():

    api = API()

    vejmidte = api.replicate('vejmidte', txidfra=3432423, txidtil=3432423)

    for obj in vejmidte:
        assert len(obj) != 0
        break
