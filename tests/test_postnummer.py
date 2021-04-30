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

    postnummer = api.replicate('postnummer', txidfra=0, txidtil=3786429)

    for obj in postnummer:
        assert 'nr' in obj
        break
