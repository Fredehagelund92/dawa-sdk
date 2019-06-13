import ast
import typing

class Postnummer(typing.NamedTuple):
    nr: str
    navn: str
    stormodtager: str

class Vejstykke(typing.NamedTuple):
    id: str
    kommunekode: str
    kode: str
    oprettet: str
    ændret: str
    navn: str
    adresseringsnavn: str
    navngivenvej_id: str

class Adresse(typing.NamedTuple):
    id: str
    status: int
    oprettet: str
    ændret: str
    ikrafttrædelsesdato: str
    adgangsadresseid: str
    etage: str
    dør: str
    kilde: int
    esdhreference: str
    journalnummer: str

class Adgangsadresse(typing.NamedTuple):
    id: str
    status: str
    oprettet: str
    ændret: str
    ikrafttrædelsesdato: str
    kommunekode: str
    vejkode: str
    husnr: str
    supplerendebynavn: str
    postnr: str
    ejerlavkode: int
    matrikelnr: str
    esrejendomsnr: str
    etrs89koordinat_øst: float
    etrs89koordinat_nord: float
    nøjagtighed: str
    kilde: int
    husnummerkilde: int
    tekniskstandard: str
    tekstretning: float
    adressepunktændringsdato: str
    esdhreference: str
    journalnummer: str
    højde: float
    adgangspunktid: str
    supplerendebynavn_dagi_id:str
    vejpunkt_id: str
    navngivenvej_id: str

class Navngivenvej(typing.NamedTuple):
    id: str
    darstatus: str
    oprettet: str
    ændret: str
    navn: str
    adresseringsnavn: str
    administrerendekommune: str
    beskrivelse: str
    retskrivningskontrol: str
    udtaltvejnavn: str
    beliggenhed_oprindelse_kilde: str
    beliggenhed_oprindelse_nøjagtighedsklasse: str
    beliggenhed_oprindelse_registrering: str
    beliggenhed_oprindelse_tekniskstandard: str

class Afstemningsområde(typing.NamedTuple):
    ændret: str
    geo_ændret: str
    geo_version: int
    visueltcenter: ast.literal_eval
    bbox: ast.literal_eval
    geometri: ast.literal_eval
    dagi_id: str
    nummer: str
    navn: str
    afstemningsstednavn: str
    afstemningsstedadresse: str
    kommunekode: str
    opstillingskreds_dagi_id: str

class Afstemningsområdetilknytning(typing.NamedTuple):
    adgangsadresseid: str
    kommunekode: str
    afstemningsområdenummer: str


class Brofasthed(typing.NamedTuple):
    stedid: str
    brofast: bool


class Bygning(typing.NamedTuple):
    id: str
    bygningstype: str
    metode3d: str
    målested: str
    bbrbygning_id: str
    synlig: bool
    overlap: bool
    geometri: ast.literal_eval


class Bygningtilknytning(typing.NamedTuple):
    bygningid: int
    adgangsadresseid: str


class Dagi_postnummer(typing.NamedTuple):
    ændret: str
    geo_ændret: str
    geo_version: int
    visueltcenter:  ast.literal_eval
    bbox:  ast.literal_eval
    geometri: ast.literal_eval
    dagi_id: str
    nr: str
    navn: str

class Ejerlav(typing.NamedTuple):
    kode: int
    navn: str
    geo_ændret: str
    geo_version: int
    ændret: str
    visueltcenter:  ast.literal_eval
    bbox:  ast.literal_eval
    geometri: ast.literal_eval

class Højde(typing.NamedTuple):
    husnummerid: str
    højde: float


class Ikke_brofast_husnummer(typing.NamedTuple):
    husnummerid: int

class Jordstykke(typing.NamedTuple):
    ejerlavkode: int
    matrikelnr: str
    kommunekode: str
    regionskode: str
    sognekode: str
    retskredskode: str
    esrejendomsnr: str
    udvidet_esrejendomsnr: str
    sfeejendomsnr: str
    geometri: ast.literal_eval
    featureid: str
    fælleslod: bool
    moderjordstykke: int
    registreretareal: int
    arealberegningsmetode: str
    vejareal: int
    vejarealberegningsmetode: str
    vandarealberegningsmetode: str
    visueltcenter: ast.literal_eval
    bbox: ast.literal_eval


class Jordstykketilknytning(typing.NamedTuple):
    ejerlavkode: int
    matrikelnr: str
    adgangsadresseid: str

class Kommune(typing.NamedTuple):
    ændret: str
    geo_ændret: str
    geo_version: int
    visueltcenter: ast.literal_eval
    bbox: ast.literal_eval
    geometri: ast.literal_eval
    dagi_id: str
    kode: str
    navn: str
    regionskode: str
    udenforkommuneinddeling: bool

class Kommunetilknytning(typing.NamedTuple):
    adgangsadresseid: str
    kommunekode: str

class Landpostnummer(typing.NamedTuple):
    ændret: str
    geo_ændret: str
    geo_version: int
    visueltcenter: ast.literal_eval
    bbox: ast.literal_eval
    geometri: ast.literal_eval
    nr: str
    navn: str

class Menighedsrådsafstemningsområde(typing.NamedTuple):
    ændret: str
    geo_ændret: str
    geo_version: int
    visueltcenter: ast.literal_eval
    bbox: ast.literal_eval
    geometri: ast.literal_eval
    dagi_id: str
    nummer: str
    navn: str
    afstemningsstednavn: str
    kommunekode: str
    sognekode: str

class Menighedsrådsafstemningsområdetilknytning(typing.NamedTuple):
    adgangsadresseid: str
    kommunekode: str
    menighedsrådsafstemningsområdenummer: str

class Opstillingskreds(typing.NamedTuple):
    ændret: str
    geo_ændret: str
    geo_version: int
    visueltcenter: ast.literal_eval
    bbox: ast.literal_eval
    geometri: ast.literal_eval
    dagi_id: str
    nummer: str
    kode: str
    navn: str
    valgkredsnummer: str
    storkredsnummer: str
    kredskommunekode: str

class Opstillingskredstilknytning(typing.NamedTuple):
    adgangsadresseid: str
    opstillingskredskode: str

class Politikreds(typing.NamedTuple):
    ændret: str
    geo_ændret: str
    geo_version: int
    visueltcenter: ast.literal_eval
    bbox: ast.literal_eval
    geometri: ast.literal_eval
    dagi_id: str
    kode: str
    navn: str

class Politikredstilknytning(typing.NamedTuple):
    adgangsadresseid: str
    politikredskode: str

class Postnummertilknytning(typing.NamedTuple):
    adgangsadresseid: str
    postnummer: str

class Region(typing.NamedTuple):
    ændret: str
    geo_ændret: str
    geo_version: int
    visueltcenter: ast.literal_eval
    bbox: ast.literal_eval
    geometri: ast.literal_eval
    dagi_id: str
    kode: str
    navn: str

class Regionstilknytning(typing.NamedTuple):
    adgangsadresseid: str
    regionskode: str

class Retskreds(typing.NamedTuple):
    ændret: str
    geo_ændret: str
    geo_version: int
    visueltcenter: ast.literal_eval
    bbox: ast.literal_eval
    geometri: ast.literal_eval
    dagi_id: str
    kode: str
    navn: str

class Retskredstilknytning(typing.NamedTuple):
    adgangsadresseid: str
    retskredskode: str

class Sogn(typing.NamedTuple):
    ændret: str
    geo_ændret: str
    geo_version: int
    visueltcenter: ast.literal_eval
    bbox: ast.literal_eval
    geometri: ast.literal_eval
    dagi_id: str
    kode: str
    navn: str

class Sognetilknytning(typing.NamedTuple):
    adgangsadresseid: str
    sognekode: str

class Sted(typing.NamedTuple):
    id: str
    hovedtype: str
    undertype: str
    bebyggelseskode: int
    indbyggerantal: int
    visueltcenter: ast.literal_eval
    bbox: ast.literal_eval
    geometri: ast.literal_eval

class Stednavn(typing.NamedTuple):
    stedid: str
    navn: str
    navnestatus: str
    brugsprioritet: str

class Stednavntilknytning(typing.NamedTuple):
    stednavn_id: str
    adgangsadresse_id: str

class Stedtilknytning(typing.NamedTuple):
    stedid: str
    adgangsadresseid: str

class Storkreds(typing.NamedTuple):
    ændret: str
    geo_ændret: str
    geo_version: int
    visueltcenter: ast.literal_eval
    bbox: ast.literal_eval
    geometri: ast.literal_eval
    nummer: str
    navn: str
    regionskode: str
    valglandsdelsbogstav: str

class Storkredstilknytning(typing.NamedTuple):
    adgangsadresseid: str
    storkredsnummer: str

class Supplerendebynavn(typing.NamedTuple):
    ændret: str
    geo_ændret: str
    geo_version: int
    visueltcenter: ast.literal_eval
    bbox: ast.literal_eval
    geometri: ast.literal_eval
    dagi_id: str
    navn: str
    kommunekode: str

class Supplerendebynavntilknytning(typing.NamedTuple):
    adgangsadresseid: str
    dagi_id: str

class Valglandsdel(typing.NamedTuple):
    ændret: str
    geo_ændret: str
    geo_version: int
    visueltcenter: ast.literal_eval
    bbox: ast.literal_eval
    geometri: ast.literal_eval
    bogstav: str
    navn: str

class Valglandsdelstilknytning(typing.NamedTuple):
    adgangsadresseid: str
    valglandsdelsbogstav: str

class Vejmidte(typing.NamedTuple):
    kommunekode: str
    vejkode: str
    geometri: ast.literal_eval

class Vejpunkt(typing.NamedTuple):
    id: str
    kilde: str
    tekniskstandard: str
    nøjagtighedsklasse: str
    position: ast.literal_eval

class Vejstykkepostnummerrelation(typing.NamedTuple):
    kommunekode: str
    vejkode: str
    postnr: str

class Zone(typing.NamedTuple):
    ændret: str
    geo_ændret: str
    geo_version: int
    visueltcenter: ast.literal_eval
    bbox: ast.literal_eval
    geometri: ast.literal_eval
    zone: str

class Zonetilknytning(typing.NamedTuple):
    adgangsadresseid: str
    zone: str