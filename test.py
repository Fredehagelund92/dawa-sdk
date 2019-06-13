from dawa import API

api = API()

for t in api.get('politikreds'):
    r = t
    print(r)


# import ast
# import typing

# def empty_to_none(s):
#     if s == '':
#         return None
#     return s

# class Postnummer(typing.NamedTuple):
#     nr : str
#     navn: str
#     stormodtager: str


# csv_reader = [
#     {'nr': '9981', 'navn': 'Jerup', 'stormodtager': ''},
#     {'nr': '9981', 'navn': 'Jerup', 'stormodtager': '1'}
# ]


# for i, row in enumerate(csv_reader):
#     row = {field: Postnummer._field_types[field](empty_to_none(value))
#                   for field, value in row.items()}
#     print(row)