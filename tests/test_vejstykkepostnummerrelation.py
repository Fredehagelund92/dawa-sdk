
import pytest

from dawa import API

def test_vejstykkepostnummerrelation_initial():

    api = API()

    vejstykkepostnummerrelation = api.replicate('vejstykkepostnummerrelation')

    for obj in vejstykkepostnummerrelation:
        assert len(obj) != 0
        break

def test_vejstykkepostnummerrelation_changes():

    api = API()

    vejstykkepostnummerrelation = api.replicate('vejstykkepostnummerrelation', txidfra=3432423, txidtil=3432423)

    for obj in vejstykkepostnummerrelation:
        assert len(obj) != 0
        break
