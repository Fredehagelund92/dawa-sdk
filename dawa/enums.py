import sys
from enum import Enum

from .endpoints import *


class ReplicationMethod(Enum):
    full = 'FULL'
    interval = 'INTERVAL'
    single = 'SINGLE'

class DawaEnum(Enum):
    vejstykke = 'vejstykke'
    postnummer = 'postnummer'
    adresse = 'adresse'
    adgangsadresse = 'adgangsadresse'
    navngivenvej = 'navngivenvej'
    afstemningsområde = 'afstemningsområde'
    afstemningsområdetilknytning = 'afstemningsområdetilknytning'
    brofasthed = 'brofasthed'
    bygning = 'bygning'
    bygningtilknytning = 'bygningtilknytning'
    dagi_postnummer = 'dagi_postnummer'
    ejerlav = 'ejerlav'
    højde = 'højde'
    ikke_brofast_husnummer = 'ikke_brofast_husnummer'
    jordstykke = 'jordstykke'
    jordstykketilknytning = 'jordstykketilknytning'
    kommune = 'kommune'
    kommunetilknytning = 'kommunetilknytning'
    landpostnummer = 'landpostnummer'
    menighedsrådsafstemningsområde = 'menighedsrådsafstemningsområde'
    menighedsrådsafstemningsområdetilknytning = 'menighedsrådsafstemningsområdetilknytning'
    opstillingskreds = 'opstillingskreds'
    opstillingskredstilknytning = 'opstillingskredstilknytning'
    politikreds = 'politikreds'
    politikredstilknytning = 'politikredstilknytning'
    region = 'region'
    regionstilknytning = 'regionstilknytning'
    retskreds = 'retskreds'
    retskredstilknytning = 'retskredstilknytning'
    sogn = 'sogn'
    sognetilknytning = 'sognetilknytning'
    sted = 'sted'
    stednavn = 'stednavn'
    stednavntilknytning = 'stednavntilknytning'
    stedtilknytning = 'stedtilknytning'
    storkreds = 'storkreds'
    storkredstilknytning = 'storkredstilknytning'
    supplerendebynavn = 'supplerendebynavn'
    supplerendebynavntilknytning = 'supplerendebynavntilknytning'
    valglandsdel = 'valglandsdel'
    valglandsdelstilknytning = 'valglandsdelstilknytning'
    vejmidte = 'vejmidte'
    vejpunkt = 'vejpunkt'
    vejstykkepostnummerrelation = 'vejstykkepostnummerrelation'
    zone = 'zone'
    zonetilknytning = 'zonetilknytning'
    postnummertilknytning = 'postnummertilknytning'

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)

    @classmethod
    def get_model(cls, value):
        return getattr(sys.modules[__name__], value.capitalize())