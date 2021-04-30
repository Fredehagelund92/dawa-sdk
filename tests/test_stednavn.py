
import pytest

from dawa import API

def test_stednavn_initial():

    api = API()

    stednavn = api.replicate('stednavn')

    for obj in stednavn:
        assert len(obj) != 0
        break

def test_stednavn_changes():

    api = API()

    stednavn = api.replicate('stednavn', txidfra=3432423, txidtil=3432423)

    for obj in stednavn:
        assert len(obj) != 0
        break
