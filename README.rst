===============
redis_connector
===============


.. image:: https://img.shields.io/pypi/v/redis_connector.svg
        :target: https://pypi.python.org/pypi/redis_connector

.. image:: https://img.shields.io/travis/monobot/redis_connector.svg
        :target: https://travis-ci.org/monobot/redis_connector

.. image:: https://readthedocs.org/projects/redis-connector/badge/?version=latest
        :target: https://redis-connector.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Redis pub/sub connector


* Free software: MIT license
* Documentation: https://redis-connector.readthedocs.io.


Features
--------

* Microservices will be able to process each of them their own messages, because of the redis lock feature each message is waranteed been processed 1 time max.
* you can also send promiscuous messages if you like them better
* sending ping messages to the different microservices allows you to know how many instances for each microservice are consuming the messages.

Todo
----

* add tests
* logg feeback when the message has not been processed by any consumer.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
