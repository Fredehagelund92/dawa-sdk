from dawa import API

api = API()

for t in api.get('ikke_brofast_husnummer'):
    r = t
    print(t)


