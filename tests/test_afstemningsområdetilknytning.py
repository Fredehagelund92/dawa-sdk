
import pytest

from dawa import API

def test_afstemningsområdetilknytning_initial():

    api = API()

    afstemningsområdetilknytning = api.replicate('afstemningsområdetilknytning')

    for obj in afstemningsområdetilknytning:
        assert len(obj) != 0
        break

def test_afstemningsområdetilknytning_changes():

    api = API()

    afstemningsområdetilknytning = api.replicate('afstemningsområdetilknytning', txidfra=3432423, txidtil=3432423)

    for obj in afstemningsområdetilknytning:
        assert len(obj) != 0
        break
