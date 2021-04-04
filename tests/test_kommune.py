import pytest
import json

from dawa import API

def test_kommune_initial():

    api = API()

    postnummer = api.replicate('kommune')

    for obj in postnummer:
        assert 'navn' in obj
        break



def test_kommune_changes():

    api = API()

    postnummer = api.replicate('kommune', txidfra=3432423, txidtil=3432423)

    for obj in postnummer:
        assert 'navn' in obj
        break
