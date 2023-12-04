Django X Power
===============

:Authors:
   Justin Quick <justquick@gmail.com>
   Paul Michali <pmichali@gmail.com>
:Version: 0.2


::

    pip install django-xpower==0.2.0

Django X Power is a simple middleware that adds the ``X-Powered-By`` header to any Django site.

    
Install
--------

Install the module using pip/easy_install or whatever you like then add in the middleware into your ``MIDDLEWARE_CLASSES``::

    MIDDLEWARE_CLASSES = (
        'xpower.middleware.XPoweredByMiddleware',
        ...
    )

Configure
----------

In your settings you may define the contents of the ``X-Powered-By`` header::

    X_POWERED_BY = 'Django'
    
If you do not set this it will use the default which is ``Django/%(version)s``
where ``%(version)s`` is replaced with the version of Django that you are using.

Testing
--------

An example project is provided to test. Using poetry to ensure version of python and
Django. Steps are:

``
poetry shell
cd example
python3 manage.py runserver
curl -i http://localhost:8000 | head
``

You should see something like this::

    HTTP/1.1 200 OK
    Date: Mon, 04 Dec 2023 20:25:50 GMT
    Server: WSGIServer/0.2 CPython/3.12.0
    Content-Type: text/html; charset=utf-8
    X-Powered-By: Me, Myself, and Irene
    X-Frame-Options: DENY
    Content-Length: 10629
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Cross-Origin-Opener-Policy: same-origin

Alternates
----------

Some alternatives for the header contents:

 * Ponies with magical powers
 * Who the fuck knows
 * A series of tubes
 * Perfectionists with deadlines
 * Opinionated developers

Version History
---------------

 * 0.2.0 Updated for newer Django version (5.0). Using Poetry for version control
 * 0.1.0 Initial release
