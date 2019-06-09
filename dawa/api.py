import requests
import json
from urllib.parse import urlencode

from .exceptions import DawaException, EndpointException
from .enums import DawaEnum

ITER_CHUNK_SIZE = 1024
BASE_URL = "https://dawa.aws.dk"


class API:

    def _get_current_txid(self):
        url = '%s/replikering/senestetransaktion' % BASE_URL
        data = self._get(url).json()

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
        params['entitet'] = endpoint

        # Set txid if in kwargs
        if 'txid' in kwargs and kwargs['txid'] is not None:
            params['txid'] = kwargs['txid']

        # If no txid then do initial replication
        if not 'txid' in params:
            # params['format'] = 'csv'
            return self.response(self._get_initial(params))

        # if txid is equal to current txid return nothing
        if params['txid'] == self._get_current_txid():
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
        result = requests.get(url, params=params, **kwargs)
        _response = result.json()

        if _response and 'error' in _response:
            raise DawaException(_response['error']['code'], _response['error']['message'], result)

        if result.status_code != 200:
            raise DawaException(result.status_code, result.reason, result)

        return result


    @staticmethod
    def response(response):
        return response.json()
