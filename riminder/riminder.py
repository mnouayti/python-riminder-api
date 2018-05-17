import requests as req

__author__ = "Change me"

RIMINDER_API_URL = "https://www.riminder.net/sf/public/api/v1.0/"


class Riminder(object):

    def __init__(self, api_key):
        self.auth_header = {
            "X-API-Key": api_key
        }

    def _create_request_url(self, resource_url):
        return "{api_endpoint}{resource_url}".format(
            api_endpoint=RIMINDER_API_URL,
            resource_url=resource_url
        )

    def get(self, resource_endpoint, query_params={}):
        url = self._create_request_url(resource_endpoint)
        return req.get(url, headers=self.auth_header, params=query_params)