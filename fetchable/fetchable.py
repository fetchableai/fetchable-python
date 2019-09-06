import six

import os
import json
import requests
import datetime

import hashlib
import hmac
import base64

from .configuration import configuration


class FetchableClient(object):
    """
    The Fetchable API Client object.

    Use this object to interact with the Fetchable API.
    """


    def __init__(self, api_version=None, user_agent=None, auth_file=None):
        """
        Constructs Fetchable API Client object.

        The client automatically reads in the auth file on initialisation, it will throw an
        exception if cannot do this.

        :param api_version: The version of the Fetchable API to use.
        :type api_version: enum

        :param user_agent: The user-agent header to be sent to Fetchable.
        :type user_agent: string

        :param auth_file: The absolute path to the authentication file.
        :type auth_file: string
        """

        from .__version__ import __version__
        self.api_version = api_version or configuration.api_version.latest
        self.version = __version__
        self.user_agent = user_agent or 'fetchable-python-client/{}'.format(self.version)
        # self.host = 'https://api.fetchable.ai'
        self.host = 'http://localhost:5003'



        auth_file_path = auth_file or os.environ.get('FETCHABLE_AUTH_FILE')
        if not auth_file_path:
            raise Exception('path authentication file not set')

        if not os.path.isfile(auth_file_path):
            raise Exception('{} is not a valid authentication file path'.format(auth_file_path))

        credentials_file = open(auth_file_path)
        try:
            self.auth_credentials = json.load(credentials_file)
            credentials_file.close()
        except:
            raise Exception('authentication file is not formatted properly')
        if 'api_key' not in self.auth_credentials:
            raise Exception('authentication file is not formatted properly')
        if 'api_secret' not in self.auth_credentials:
            raise Exception('authentication file is not formatted properly')
        if type(self.auth_credentials['api_key']) != six.text_type:
            raise Exception('authentication file is not formatted properly')
        if type(self.auth_credentials['api_secret']) != six.text_type:
            raise Exception('authentication file is not formatted properly')

    def status(self):
        """
        Gets the status of the Fetchable API
        """
        return self.make_request(None)


    def fetch_entity_atrribute(self, entity, attribute):
        """
        Fetches an entity-attribute value from the index

        :param entity: The entity to fetch.
        :type entity: str

        :param attribute: The attribute of the entity to fetch.
        :type attribute: str
        """
        if not entity or not attribute:
            raise Exception('parameters cannot be null')

        if type(entity) != str or type(attribute) != str:
            raise Exception('parameters are not strings')

        resource = self.api_version+"/"+entity+"/"+attribute
        return self.make_request(resource)


    def fetch_word_definition(self, word):
        """
        Fetches the definition of a word

        :param word: The word to get the definition of.
        :type word: str
        """

        if not word:
            raise Exception('parameters can not be null')

        if type(word) != str:
            raise Exception('parameters are not strings')

        resource = self.api_version+"/"+word+"/definition"
        return self.make_request(resource)


    def fetch_joke(self):
        """
        Fetches a joke
        """
        resource = self.api_version+"/random/joke"
        return self.make_request(resource)


    def fetch_quote(self):
        """
        Fetches a quote
        """
        resource = self.api_version+"/random/quote"
        return self.make_request(resource)


    def fetch_fun_fact(self):
        """
        Fetches a fun fact
        """
        resource = self.api_version+"/random/fun_fact"
        return self.make_request(resource)


    def fetch_endpoint(self, endpoint):
        """
        Makes a request against a specific endpoint.

        Note: it is up to the caller to construct the endpoint here. This will override the version set in the constructor.
        Note: must start with a /
        Examples:   /ameliorate/definition
                    /v0.1/amazon_river_length

        :param endpoint: The endpoint to make a request against.
        :type endpoint: str
        """
        if not endpoint:
            raise Exception('parameters can not be null')

        if type(endpoint) != str:
            raise Exception('parameters are not strings')

        return self.make_request(endpoint)





    #private functions
    def make_request(self, resource):
        """
        Makes request to Fetchable API and returns the response body.
        """
        try:
            if resource:
                url = self.host+resource
                response = requests.get(url, headers=self.construct_headers(resource))
            else: #get status endpoint
                response = requests.get(self.host)
            body = json.loads(response.content)
            body['status_code'] = response.status_code
            return body

        except requests.exceptions.ConnectionError:
            body={}
            body['status_code'] = 1001
            body['reason'] = "Connection error occured"
            return body

        except requests.exceptions.Timeout:
            body={}
            body['status_code'] = 1002
            body['reason'] = "Timeout error occured"
            return body

        except requests.exceptions.ProxyError:
            body={}
            body['status_code'] = 1003
            body['reason'] = "Proxy error occured"
            return body

        except:
            body={}
            body['status_code'] = 1004
            body['reason'] = "Unknown error occured"
            return body


    def construct_headers(self, resource):
        """
        Constructs headers for the request
        """
        date = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+"Z"
        signature_plain = ('GET'+resource+date).encode();

        hashed = hmac.new(self.auth_credentials['api_secret'].encode('ascii','ignore'),
            signature_plain,
            hashlib.sha1)
        signature1 = hashed.hexdigest().encode()
        signature2 = base64.urlsafe_b64encode(signature1)
        header = {
            "authorization": "Fetchable "+self.auth_credentials['api_key']+":"+signature2.decode(),
            "date": date,
            "user-agent": self.user_agent
        }
        return header
