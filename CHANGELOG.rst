==========
Change Log
==========

This document records all changes to the Fetchable Python client-side SDK and adheres to the `Semantic Versioning <https://semver.org/>`_ philosophy.

Notes
=====
Both the API and the client-side SDKS are versioned. The major and minor versions of client-side SDKs follow changes on the API side. e.g.

* 0.1.x for client-side SDKs corresponds to the v0.1 (Alpha) version of the API.
* 0.2.x for client-side SDKs corresponds to the v0.2 (Beta) version of the API.

The patch versions of the client-side SDKs (e.g. x.x.1, x.x.2, x.x.3, etc.) are independent of backend API versions and are free to update as they wish.

0.1 (Alpha version)
====================


0.1.0 (Released Aug 25, 2019)
-----------------------------
Initial public release with:


* client object with: ability to set user-agent; constructs authentication headers; and exposes wrapper functions for all endpoints in v0.1 of the backend API,

* example code,

* configuration class with API version selection,

* license, readme, contributing file, setup.py and requirements file.


0.1.1 (Released Sept 5, 2019)
-----------------------------
* Added compatibility between Python 2.7 and 3.6.


0.1.2 (Released Sept 6, 2019)
-----------------------------
* Cheekily changed public-facing interface since still in Alpha and no users will be affected - removed 'random' from fun fact, joke and quote functions.
* Added a change log and updated `Contributing Guide <CONTRIBUTING.rst>`_ guide.


0.1.3 (Released Sept 6, 2019)
-----------------------------
* Bugfixes in fetchable client object.
* Fixed errata in readme and changelog.


0.1.4 (Released Sept 7, 2019)
-----------------------------
* Updated Github issue templates.
* Added sanitisation of function parameters through private helper function, e.g. fetch_entity_atrribute("Empire State building", "Height") -> fetch_entity_atrribute("empire_state_building", "height").
