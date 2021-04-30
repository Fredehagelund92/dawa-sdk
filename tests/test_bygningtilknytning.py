
import pytest

from dawa import API

def test_bygningtilknytning_initial():

    api = API()

    bygningtilknytning = api.replicate('bygningtilknytning')

    for obj in bygningtilknytning:
        assert len(obj) != 0
        break

def test_bygningtilknytning_changes():

    api = API()

    bygningtilknytning = api.replicate('bygningtilknytning', txidfra=3432423, txidtil=3432423)

    for obj in bygningtilknytning:
        assert len(obj) != 0
        break
