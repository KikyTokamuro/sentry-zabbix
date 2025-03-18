sentry-zabbix
=============

An extension for Sentry to send event counts to Zabbix; shamelessly based on sentry-statsd_.
This will send keys formatted like ``<prefix>.<level>[<project>]`` (e.g. 
``sentry.error[my-thing]``), which will need to be configured as items in Zabbix.

Tested on sentry 25.2.0.

Install
-------

Install the package with ``pip``::

    git clone https://github.com/KikyTokamuro/sentry-zabbix
    cd sentry-zabbix
    pip install .


Configuration
-------------

Go to your project's configuration page (Projects -> [Project]) and select the
"Zabbix" tab. Enter the Zabbix host, port and prefix for metrics:

.. image:: https://github.com/KikyTokamuro/sentry-zabbix/raw/master/docs/images/options.png


After installing and configuring, make sure to restart sentry-worker and sentry-web for the
changes to take effect.

.. _sentry-statsd: https://github.com/dreadatour/sentry-statsd
