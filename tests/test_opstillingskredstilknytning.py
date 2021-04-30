
import pytest

from dawa import API

def test_opstillingskredstilknytning_initial():

    api = API()

    opstillingskredstilknytning = api.replicate('opstillingskredstilknytning')

    for obj in opstillingskredstilknytning:
        assert len(obj) != 0
        break

def test_opstillingskredstilknytning_changes():

    api = API()

    opstillingskredstilknytning = api.replicate('opstillingskredstilknytning', txidfra=3432423, txidtil=3432423)

    for obj in opstillingskredstilknytning:
        assert len(obj) != 0
        break
