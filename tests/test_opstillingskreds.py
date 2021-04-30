
import pytest

from dawa import API

def test_opstillingskreds_initial():

    api = API()

    opstillingskreds = api.replicate('opstillingskreds')

    for obj in opstillingskreds:
        assert len(obj) != 0
        break

def test_opstillingskreds_changes():

    api = API()

    opstillingskreds = api.replicate('opstillingskreds', txidfra=3432423, txidtil=3432423)

    for obj in opstillingskreds:
        assert len(obj) != 0
        break
