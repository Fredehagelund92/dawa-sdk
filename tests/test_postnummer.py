import pytest
import json

from dawa import API

def test_postnummer_initial():

    api = API()

    postnummer = api.replicate('postnummer')

    for obj in postnummer:
        assert 'nr' in obj
        break



def test_postnummer_changes():

    api = API()

    postnummer = api.replicate('postnummer', txidfra=3432423, txidtil=3432423)

    for obj in postnummer:
        assert 'nr' in obj
        break
