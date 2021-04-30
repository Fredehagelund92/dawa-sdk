
import pytest

from dawa import API

def test_sogn_initial():

    api = API()

    sogn = api.replicate('sogn')

    for obj in sogn:
        assert len(obj) != 0
        break

def test_sogn_changes():

    api = API()

    sogn = api.replicate('sogn', txidfra=3432423, txidtil=3432423)

    for obj in sogn:
        assert len(obj) != 0
        break
