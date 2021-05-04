import requests
import tempfile
import csv

from .exceptions import EndpointException, ValidationError
from .enums import DawaEnum, ReplicationMethod

ITER_CHUNK_SIZE = 1024
BASE_URL = "https://dawa.aws.dk"


class API:

    def txid(self):
        return self._get_current_txid()

    def search(self, endpoint, **kwargs):
        return

    def replicate(self, endpoint, **kwargs):

        endpoint_lower = endpoint.lower()


        # Check if endpoint exists
        if not DawaEnum.has_value(endpoint_lower):
            raise EndpointException('The following endpoint does not exists or is not supported: %s' % endpoint)

        # Validate replication params
        # You cannot have only one of the parameters txidtil and txidfra
        if 'txidtil' in kwargs and 'txidfra' not in kwargs:
            raise ValidationError('You cannot have parameter txidtil without txidfra')

        # You cannot have only one of the parameters txidfra and txidtil
        if 'txidfra' in kwargs and 'txidtil' not in kwargs:
            raise ValidationError('You cannot have parameter txidfra without txidtil')

        # You cannot have txid with txidfra and txidtil
        if 'txid' in kwargs and ('txidtil' in kwargs or 'txidfra' in kwargs):
            raise ValidationError('You cannot combine parameter txid with txidfra and txidtil')

        # Create default request params
        params = {}
        params['entitet'] = endpoint_lower
        params['format'] = 'csv'

        # Set params for single replication
        if 'txid' in kwargs:
            params['txid'] = kwargs['txid']

            if params['txid'] == self._get_current_txid():
                return

            # Retrieve latest updates
            return self.response(self._get_updates(params))

        # Set params for interval replication
        if 'txidtil' in kwargs and 'txidfra' in kwargs:
            params['txidtil'] = kwargs['txidtil']
            params['txidfra'] = kwargs['txidfra']
            return self.response(self._get_updates(params))


        return self.response(self._get_initial(params))

    def _get_initial(self, params):
        url = '%s/replikering/udtraek' % BASE_URL

        return self._get(url, params=params)

    def _get_updates(self, params):
        url = '%s/replikering/haendelser' % BASE_URL

        return self._get(url, params=params)

    def _get_current_txid(self):
        url = '%s/replikering/senestetransaktion' % BASE_URL
        data = requests.get(url).json()

        if 'txid' in data:
            return data['txid']

        return None

    @staticmethod
    def _get(url, params=None):
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
                        # Set value initial to None to handle literal_eval type
                        new_value = None

                        # If value not empty then proceed
                        if value:
                            new_value = endpoint_class._field_types[field](value)

                            # Convert empty strings to handle datetime
                            if not new_value:
                                row[field] = None
                            else:
                                row[field] = new_value
                    except (ValueError, KeyError) as e:
                        row.pop(field, None)

                vals = row

                yield vals

    @staticmethod
    def response(response):
        return response
