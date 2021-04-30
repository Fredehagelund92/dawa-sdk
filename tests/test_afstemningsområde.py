
import pytest

from dawa import API

def test_afstemningsområde_initial():

    api = API()

    afstemningsområde = api.replicate('afstemningsområde')

    for obj in afstemningsområde:
        assert len(obj) != 0
        break

def test_afstemningsområde_changes():

    api = API()

    afstemningsområde = api.replicate('afstemningsområde', txidfra=3432423, txidtil=3432423)

    for obj in afstemningsområde:
        assert len(obj) != 0
        break
