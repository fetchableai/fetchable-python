=================================
Fetchable: Python Client Side SDK
=================================

This is the Fetchable client-side Software Development Kit (SDK) for Python. It allows developers of robots, smart speakers, voice assistants, etc. to quickly develop programs that make calls to the Fetchable API. The library has only been tested on Ubuntu systems so far.


Table of Contents
=================

-  `Installation <#installation>`__
-  `Usage <#usage>`__
-  `Errors <#errors>`__
-  `Contributing <#contributing>`__
-  `License <#license>`__

Installation
============

Pre-requisites
--------------

* Python 2.7 or 3.6
* An active Fetchable account.

Install Package
---------------

The recommended way to install this package is through pip (or pip3) as follows:

.. code-block:: sh

  $ pip install fetchable


Set Up Keys
-----------

1. Log into your account and on the console page, download the authentication keys and note the location it downloaded to. The file should be named 'fetchable_auth_keys.json'. Note: be sure to keep this file secure and share it or commit it to any source control.

2. By default, when the library runs it will attempt to read the file containing your keys from an environment variable which
specifies the path to the file (you can also override the environment variable by explicitly setting the path in the constructor). Set the environment variable as so:

.. code-block:: sh

  $ export FETCHABLE_AUTH_FILE=/path/to/fetchable_auth_keys.json


Usage
=====
Once you have completed the installation, you can start fetching data from the index. The main class used to interact with the API is the FetchableClient object.

Constructing the Client Object
------------------------------

There are three optional parameters which can be passed to the constructor of the FetchableClient object.

1. API version

The verison of the API to be used can be specified with the :code:`api_version` parameter. The parameter is an enum defined in the configuration file which needs to be imported. The FetchableClient object will default to the latest version in the absence of this parameter.

.. code-block:: python

  from fetchable import FetchableClient
  from fetchable import configuration

  client = FetchableClient(api_version=configuration.api_version.v0_1)

2. User agent

The FetchableClient object allows you to set your own user-agent header, this can be done through the :code:`user_agent` parameter in the format :code:`<custom-user-agent>/<version>` where :code:`version` takes the form  :code:`v0.1`, :code:`v0.2`, :code:`v1.0`, etc. By setting this to something relevant to only your application (e.g. :code:`amazing-chatbot/0.1`) and by whitelisting only that value through the console you can enhance the security of your account and distinguish between different applications. The default is value is :code:`fetchable-python-client/v?.?`.

.. code-block:: python

  from fetchable import FetchableClient

  client = FetchableClient(user_agent='amazing-chatbot/0.1')


3. Authentication credentials

By default, the libary will attempt to read your authentication keys from the file specified by the :code:`FETCHABLE_AUTH_FILE` environment variable. You can also specify this through the constructor. If both are set, the value passed through to the constructor will override the  environment variable. If neither are set, an exception is thrown.

.. code-block:: python

  from fetchable import FetchableClient

  client = FetchableClient(auth_file='/path/to/file/here.json')



Fetching from endpoints
-----------------------

Once the installation has been completed and the object has been constructed, you can begin making calls against the API endpoints. Note: these endpoints only cover version v0.1 of the API, visit the `endpoint <https://fetchable.ai/docs/api/endpoints>`_ documentation for more details on these.

1. API status endpoint

This endpoint is useful to test the connection and authentication of the client as well as receive the current status of the API.

.. code-block:: python

  from fetchable import FetchableClient

  client = FetchableClient()

  status_response = client.status()

  if(status_response['status_code']==200):
      print("The Fetchable API is up - all systems are go")
  elif(status_response['status_code']==1001):
      print("I can't connect to the internet right now...")
  else:
      print(status_response)

2. Entity-attribute endpoint

This endpoint is used to fetch the attributes of entities in our index.

.. code-block:: python

  from fetchable import FetchableClient

  client = FetchableClient()

  entity_response = client.fetch_entity_atrribute("Mount Everest", "Elevation")

  if(entity_response['status_code']==200):
      print("The height of mount_everest is {} {}.".format(entity_response['value'], entity_response['unit']))
  elif(entity_response['status_code']==1001):
      print("Can't connect to the internet right now...")
  else:
      print(entity_response)

3. Dictionary endpoint

Used to fetch the definitions of words.

.. code-block:: python

  from fetchable import FetchableClient

  client = FetchableClient()

  definition_response = client.fetch_word_definition("ameliorate")

  if(definition_response['status_code']==200):
      print("The definition of {}: is {}".format("ameliorate", definition_response['meanings'][0]))
  elif(definition_response['status_code']==1001):
      print("Can't connect to the internet right now...")
  else:
      print(definition_response)


4. Joke endpoint

.. code-block:: python

  from fetchable import FetchableClient

  client = FetchableClient()

  joke_response = client.fetch_joke()

  if(joke_response['status_code']==200):
      print("{} - {}".format(joke_response['setup'], joke_response['punchline']))
  elif(joke_response['status_code']==1001):
      print("Can't connect to the internet right now...")
  else:
      print(joke_response)

5. Inspirational quote endpoint

.. code-block:: python

  from fetchable import FetchableClient

  client = FetchableClient()

  quote_response = client.fetch_quote()

  if(quote_response['status_code']==200):
      print("{} by {}".format(quote_response['quote'], quote_response['author']))
  elif(quote_response['status_code']==1001):
      print("Can't connect to the internet right now...")
  else:
      print(quote_response)

4. Fun fact endpoint

.. code-block:: python

  from fetchable import FetchableClient

  client = FetchableClient()

  fun_fact_response = client.fetch_fun_fact()

  if(fun_fact_response['status_code']==200):
      print(fun_fact_response['fun_fact'])
  elif(fun_fact_response['status_code']==1001):
      print("Can't connect to the internet right now...")
  else:
      print(fun_fact_response)

4. Exact endpoint

This endpoint allows you to specify an exact endpoint to fetch.

.. code-block:: python

  from fetchable import FetchableClient

  client = FetchableClient()

  endpoint_response = client.fetch_endpoint("/v0.1/mount_everest/height")

  if(endpoint_response['status_code']==200):
      print("The height of mount_everest is {} {}s.".format(endpoint_response['value'], endpoint_response['unit']))
  elif(endpoint_response['status_code']==1001):
      print("Can't connect to the internet right now...")
  else:
      print(endpoint_response)


Errors
======

1. Exceptions

The FetchableClient object will throw exceptions when:

* The path to the authentication file is not set through an environment variable or constructor argument.
* The path to the authentication file is not a valid file path.
* The authentication file is not formatted properly.
* Functions taking string parameters are passed arguments which are not strings.

2. Error codes

There are two types of error codes you can receive back from the client object. Those in the 1xxx range are errors thrown by the client object itself and other error codes in the 2xx, 3xx, 4xx and 5xx ranges are the standard http error codes received from the server. For more information on the server error codes visit the `documentation <https://fetchable.ai/docs/api/general>`_.

+-------+------------------+--------------------------------------------------------------+
| Code  | Description      | Reason                                                       |
+-------+------------------+--------------------------------------------------------------+
| 1001  | Connection error |  The client cannot make a connection to the API server.      |
+-------+------------------+--------------------------------------------------------------+
| 1002  | Timeout error    |  The request timed out.                                      |
+-------+------------------+--------------------------------------------------------------+
| 1003  | Proxy error      |  A proxy error occurred.                                     |
+-------+------------------+--------------------------------------------------------------+
| 1004  | Unknown error    |  An unknown error occurred.                                  |
+-------+------------------+--------------------------------------------------------------+

Contributing
============

Contributions are welcome and encouraged! See the `Contributing Guide <CONTRIBUTING.rst>`_ for information on how to contribute.


License
=======
Licensed under Apache Version 2.0.

See the `LICENSE <LICENSE>`_ file for more information.
