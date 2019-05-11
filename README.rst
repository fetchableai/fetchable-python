=================================
Fetchable: Client Side Python SDK
=================================

This is the Fetchable client-side Software Development Kit (SDK) for Python. It allows developers of robots, smart speakers, voice assistants, etc. to quickly write software that makes calls to the Fetchable API.


Table of Contents
=================

-  `Installation <#installation>`__
-  `Usage <#usage>`__
-  `Contributing <#contributing>`__
-  `License <#license>`__

Installation
============

Pre-requisites
-------------

* Python 2.7 or 3.4
* An active Fetchable account.

Install Package
---------------

.. code-block:: sh

  $ pip install fetchable-client


Setup Environment Variables
---------------------------

By default, the library will read your key file from an environment variable. Set the path to the key file as so:

.. code-block:: sh

  $ export FETCHABLE_AUTH_FILE=/path/to/file.json


Usage
=====
Once the installation is correctly done, to start fetching data from the index, simply follow these examples.

Constructing the Client Object
------------------------------

There are three optional parameters which can be passed to the constructor of the FetchableClient object.

1. API version

The verison of the API to be used can be specified with the :code:`api_version` parameter. The parameter is an enum defined in the configuration file which needs to be imported.

.. code-block:: python

  from fetchable import FetchableClient
  from fetchable import configuration

  client = FetchableClient(api_version=configuration.api_version.v0_1)

1. User agent

The user-agent header to be sent to Fetchable can be set through the :code:`user_agent` parameter. By setting this to something you specify (e.g. :code:`amazing-chatbot/0.1`) and by whitelisting only that through the console you can enhance the security of your account. Only user-agents matching that will be permitted.

.. code-block:: python

  from fetchable import FetchableClient

  client = FetchableClient(user_agent='amazing-chatbot/0.1')


1. Authentication credentials

By default, the libary will read your authentication keys from the file specified by the environment variable you set. But you can also specify this through the constructor, this will overide the environment variable.

.. code-block:: python

  from fetchable import FetchableClient

  client = FetchableClient(auth_file='/path/to/file/here.json')



Entity-Attribute
----------------

.. code-block:: python

  from fetchable import FetchableClient

  client = FetchableClient()

  response = client.fetch("mount_everest", "elevation")

  if(response['status_code']==200):
      print("The height of mount_everest is {}.".format(response['answer']))

  elif(response['status_code']==1000):
      print("I cant connect to the internet right now...")


Random Quote
-----------------

.. code-block:: python

  from fetchable import FetchableClient

  client = FetchableClient()

  response = client.fetchRandomQuote()

  if(response['status_code']==200):
      print("{} by {}".format(response['quote'], response['author']))

  elif(response['status_code']==1000):
      print("I cant connect to the internet right now...")




Contributing
============

Contributions are welcome and encouraged! See the `Contributing Guide <CONTRIBUTING.rst>`_ for information on how to contribute.


License
=======
Licensed under Apache Version 2.0.

See the `LICENSE <LICENSE>`_ file for more information.
