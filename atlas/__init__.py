"""
Atlas API
This package contains all api integrations to atlas
"""
import requests
import logging
from requests.auth import HTTPDigestAuth
from atlas.errors import ApiError

version_tuple = (0, 0, 1, 'developmental')


def get_version_str():
    """
    :return: return api version
    """
    return '.'.join(map(str, version_tuple))


class BaseApi:
    """
    Simple base case representing
    """
    def __init__(self, api_usr, api_token, api_url='https://cloud.mongodb.com/api/atlas/v1.0'):
        """
        :param api_url:
        :param api_usr:
        :param api_token:
        """
        self.logger = logging.getLogger(__name__)
        self.api_url = api_url
        self.api_usr = api_usr
        self.api_token = api_token
        self.logger.info('api client setup: %s' % self.api_url)

    def _get(self, resource, params=None):
        """
        :param resource:
        :param params:
        :return:
        """
        self.logger.debug('attempting to read(GET) resource: %s' % resource)
        response = requests.get(
            str('{}{}'.format(self.api_url, resource)),
            params=params,
            auth=HTTPDigestAuth(username=self.api_usr, password=self.api_token)
        )

        self._validate_response(response, resource, 'GET')
        return response.json()

    def _patch(self, resource, data, params=None):
        response = requests.patch(
            '{}{}'.format(self.api_url, resource),
            json=data,
            params=params,
            auth=HTTPDigestAuth(username=self.api_usr, password=self.api_token)
        )
        self._validate_response(response, resource, 'PATCH')
        return response.json()

    def _post(self, resource, data, params=None):
        """
        :param resource: resource to create
        :param data: json data structure
        :param params:
        :return:
        """
        self.logger.debug('attempting to create(POST) resource: %s' % resource)
        response = requests.post(
            str('{}{}'.format(self.api_url, resource)),
            json=data,
            params=params,
            auth=HTTPDigestAuth(username=self.api_usr, password=self.api_token)
        )
        self._validate_response(response, resource, 'POST')
        return response.json()

    def _put(self, resource, data, params=None):
        self.logger.debug('attempting to put(UPDATE/CREATE) resource: %s' % resource)
        response = requests.put(
            str('{}{}'.format(self.api_url, resource)),
            params=params,
            auth=HTTPDigestAuth(username=self.api_usr, password=self.api_token)
        )
        return response.json()

    def _delete(self, resource, params=None):
        self.logger.debug('attempting to delete(DELETE) resource: %s' % resource)
        response = requests.delete(
            str('{}{}'.format(self.api_url, resource)),
            params=params,
            auth=HTTPDigestAuth(username=self.api_usr, password=self.api_token)
        )
        self._validate_response(response, resource, 'DELETE')
        return response.json()

    def _validate_response(self, response, resource, method):
        """
        :param response:
        :return:
        """
        if response.status_code < 200 or response.status_code > 299:
            r = response.json()
            self.logger.error(
                'api call(%s) failed for %s, status code: %d' % (method, resource, response.status_code)
            )
            self.logger.error('reason:%s, detail:%s' % (r['reason'], r['detail']))
            raise ApiError(
                '{}({}): {}'.format(r['reason'], response.status_code, r['detail']),
                response.status_code
            )
        self.logger.debug('valid response found')

    def get_from_link(self, link):
        """
        TODO: can we reduce this code to the _get! or vice versa _get builds a link!
        :param link:
        :return:
        """
        self.logger.debug('attempting to read for linked resource: %s' % link['href'])
        response = requests.get(
            link['href'],
            auth=HTTPDigestAuth(username=self.api_usr, password=self.api_token)
        )
        self._validate_response(response, link['href'], 'LINK')
        return response.json()


from atlas.api import AtlasApi
