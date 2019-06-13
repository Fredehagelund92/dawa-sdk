import requests
import tempfile
import csv

from .exceptions import DawaException, EndpointException
from .enums import DawaEnum

ITER_CHUNK_SIZE = 1024
BASE_URL = "https://dawa.aws.dk"


class API:
    def __init__(self):
        pass

    def _get_current_txid(self):
        url = '%s/replikering/senestetransaktion' % BASE_URL
        data = requests.get(url).json()

        if 'txid' in data:
            return data['txid']

        return None

    def txid(self):
        return self._get_current_txid()

    def get(self, endpoint, **kwargs):

        # Check if endpoint exists
        if not DawaEnum.has_value(endpoint):
            raise EndpointException('The following endpoint does not exists: %s' % endpoint)



        # Create request params
        params = {}
        params['entitet'] = endpoint.lower()
        params['format'] = 'csv'

        # You cannot have only one of the parameters txidtil and txidfra
        if 'txidtil' in kwargs and 'txidfra' not in kwargs:
            raise EndpointException('You cannot have parameter txidtil without txidfra')

        if 'txidfra' in kwargs and 'txidtil' not in kwargs:
            raise EndpointException('You cannot have parameter txidfra without txidtil')


        # Set txid if in kwargs and it is not None
        if 'txidtil' in kwargs and 'txidfra' in kwargs:
            if kwargs['txidtil'] is not None and kwargs['txidfra'] is not None:
                params['txidtil'] = kwargs['txidtil']
                params['txidfra'] = kwargs['txidfra']

        # If no txid then do initial replication
        if 'txidtil' not in params and 'txidfra' not in params:
            return self.response(self._get_initial(params))

        # if txid is equal to current txid return nothing
        if params['txidfra'] == self._get_current_txid():
            return

        # Retrieve latest updates
        return self.response(self._get_updates(params))

    def _get_initial(self, params):
        URL = '%s/replikering/udtraek' % BASE_URL


        return self._get(URL, params=params)


    def _get_updates(self, params):
        URL = '%s/replikering/haendelser' % BASE_URL

        return self._get(URL, params=params)


    @staticmethod
    def _get(url, params=None, **kwargs):
        headers = dict()
        headers['Content-Type'] = 'text/csv'

        with tempfile.NamedTemporaryFile(mode="w+", encoding="utf8") as csv_file:
            resp = requests.get(url, params=params, headers=headers, stream=True)
            for chunk in resp.iter_content(chunk_size=ITER_CHUNK_SIZE, decode_unicode=True):
                if chunk:
                    # Replace any NULL bytes in the chunk so it can be safely given to the CSV reader
                    csv_file.write(chunk.replace('\0', ''))

            csv_file.seek(0)
            csv_reader = csv.reader(
                csv_file,
                delimiter=',',
                quotechar='"'
            )
            # Get header values
            column_name_list = next(csv_reader)


            endpoint = params['entitet']
            endpoint_class = DawaEnum.get_model(endpoint)



            for line in csv_reader:
                rec = dict(zip(column_name_list, line))

                row = {}
                for field, value in rec.items():
                    try:
                        new_value = endpoint_class._field_types[field](value)

                        # Convert empty strings to handle datetime
                        if not new_value:
                            row[field] = None
                        else:
                            row[field] = new_value
                    except ValueError:
                        row[field] = None

                vals = row
                yield vals

    @staticmethod
    def response(response):
        return response
