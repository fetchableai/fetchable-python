
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


    def __init__(self, api_version=None):
        """
        Constructs Fetchable API Client object.

        The client automatically reads in the auth file on initialisation, it will throw an
        exception if cannot do this.

        :param api_version: The version of the Fetchable API to use.
        :type api_version: enum
        """

        from .__version__ import __version__
        self.api_version = api_version or configuration.api_version.latest
        self.version = __version__
        self.user_agent = 'fetchable-python-client/{}'.format(self.version)
        self.host = 'https://api.fetchable.ai'



        auth_file_path = os.environ.get('FETCHABLE_AUTH_FILE')
        if(not auth_file_path):
            raise Exception('authentication file path environment variable not set')

        if(not os.path.isfile(auth_file_path)):
            raise Exception('{} is not a valid authentication file path'.format(auth_file_path))

        auth_file = open(auth_file_path)
        try:
            self.auth_credentials = json.load(auth_file)
        except:
            raise Exception('authentication file is not formatted properly')


    def status(self):
        """
        Gets the status of the Fetchable API.
        """
        try:
            response = requests.get(self.host)
            body = json.loads(response.content)
            body['status_code'] = response.status_code
            # print(body)
            return body

        except requests.exceptions.ConnectionError:
            body={}
            body['status_code'] = 1000
            body['reason'] = "Connection error occured"
            return body

        except requests.exceptions.HTTPError:
            body={}
            body['status_code'] = 1001
            body['reason'] = "HTTP error occured"
            return body

        except requests.exceptions.Timeout:
            body={}
            body['status_code'] = 1002
            body['reason'] = "Timeout error occured"
            return body

        except requests.exceptions.TooManyRedirects:
            body={}
            body['status_code'] = 1003
            body['reason'] = "Too many redirects error occured"
            return body

        except:
            body={}
            body['status_code'] = 1003
            body['reason'] = "Unknown error occured"
            return body


    def fetch(self, entity, attribute):
        """
        Fetches an entity-attribute value from the index

        :param entity: The entity to fetch.
        :type entity: str

        :param attribute: The attribute of the entity to fetch.
        :type attribute: str
        """

        if type(entity) != str or type(attribute) != str:
            raise Exception('parameters are not strings')

        resource = self.api_version+"/"+entity+"/"+attribute
        url = self.host+resource
        try:
            response = requests.get(url, headers=self.__constructHeaders(resource))
            body = json.loads(response.content)
            body['status_code'] = response.status_code
            return body

        except requests.exceptions.ConnectionError:
            body={}
            body['status_code'] = 1000
            body['reason'] = "Connection error occured"
            return body

        except requests.exceptions.HTTPError:
            body={}
            body['status_code'] = 1001
            body['reason'] = "HTTP error occured"
            return body

        except requests.exceptions.Timeout:
            body={}
            body['status_code'] = 1002
            body['reason'] = "Timeout error occured"
            return body

        except requests.exceptions.TooManyRedirects:
            body={}
            body['status_code'] = 1003
            body['reason'] = "Too many redirects error occured"
            return body

        except:
            body={}
            body['status_code'] = 1003
            body['reason'] = "Unknown error occured"
            return body


    def fetchRandomJoke(self):
        """
        Fetches a random joke
        """
        resource = self.api_version+"/random/joke"
        url = self.host+resource
        try:
            response = requests.get(url, headers=self.__constructHeaders(resource))
            body = json.loads(response.content)
            body['status_code'] = response.status_code
            return body

        except requests.exceptions.ConnectionError:
            body={}
            body['status_code'] = 1000
            body['reason'] = "Connection error occured"
            return body

        except requests.exceptions.HTTPError:
            body={}
            body['status_code'] = 1001
            body['reason'] = "HTTP error occured"
            return body

        except requests.exceptions.Timeout:
            body={}
            body['status_code'] = 1002
            body['reason'] = "Timeout error occured"
            return body

        except requests.exceptions.TooManyRedirects:
            body={}
            body['status_code'] = 1003
            body['reason'] = "Too many redirects error occured"
            return body

        except:
            body={}
            body['status_code'] = 1003
            body['reason'] = "Unknown error occured"
            return body


    def fetchRandomQuote(self):
        """
        Fetches a random quote
        """
        resource = self.api_version+"/random/quote"
        url = self.host+resource
        try:
            response = requests.get(url, headers=self.__constructHeaders(resource))
            body = json.loads(response.content)
            body['status_code'] = response.status_code
            return body

        except requests.exceptions.ConnectionError:
            body={}
            body['status_code'] = 1000
            body['reason'] = "Connection error occured"
            return body

        except requests.exceptions.HTTPError:
            body={}
            body['status_code'] = 1001
            body['reason'] = "HTTP error occured"
            return body

        except requests.exceptions.Timeout:
            body={}
            body['status_code'] = 1002
            body['reason'] = "Timeout error occured"
            return body

        except requests.exceptions.TooManyRedirects:
            body={}
            body['status_code'] = 1003
            body['reason'] = "Too many redirects error occured"
            return body

        except:
            body={}
            body['status_code'] = 1003
            body['reason'] = "Unknown error occured"
            return body


    def __constructHeaders(self, resource):
        date = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+"Z"
        signature_plain = "GET"+resource+date;
        hashed = hmac.new(self.auth_credentials['api_secret'].encode('ascii','ignore'),
            signature_plain,
            hashlib.sha1)
        signature1 = hashed.hexdigest()
        signature2 = base64.urlsafe_b64encode(signature1)
        header = {
            "authorization": "Fetchable "+self.auth_credentials['api_key']+":"+signature2,
            "date": date,
            "user-agent": self.user_agent
        }
        return header
