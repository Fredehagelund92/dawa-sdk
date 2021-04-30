
import pytest

from dawa import API

def test_kommune_initial():

    api = API()

    kommune = api.replicate('kommune')

    for obj in kommune:
        assert len(obj) != 0
        break

def test_kommune_changes():

    api = API()

    kommune = api.replicate('kommune', txidfra=3432423, txidtil=3432423)

    for obj in kommune:
        assert len(obj) != 0
        break
