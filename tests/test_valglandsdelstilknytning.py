
import pytest

from dawa import API

def test_valglandsdelstilknytning_initial():

    api = API()

    valglandsdelstilknytning = api.replicate('valglandsdelstilknytning')

    for obj in valglandsdelstilknytning:
        assert len(obj) != 0
        break

def test_valglandsdelstilknytning_changes():

    api = API()

    valglandsdelstilknytning = api.replicate('valglandsdelstilknytning', txidfra=3432423, txidtil=3432423)

    for obj in valglandsdelstilknytning:
        assert len(obj) != 0
        break
