# Django X Power


## NOTE
This is a total rewrite of the original package, so that it works with DJango 5.0+, where
there have been changes in middleware, app structure, and in deploying packages. I kept
the same licensing that was mentioned, and rough naming, even though it is 99% different.
I would likely have to name it differently, to publish on PyPI, however.

Even though it works when testing locally, I've abandoned the effort, as with some environments,
like my hosting provider, which uses Phusion Passenger, I was seeing that some headers are
added AFTER all the middleware runs. In particular, X-Powered-By, so I still could not mask
out/change that information. I was ideally thinking of making this more generic, so that
multiple 'unsafe' headers (e.g. Server and many others) could be removed or changed, but it
won't work uing middleware (yes, I did try this as the first middleware, so it changes
response headers last).

Leaving it here, in case things change, or I need to create other middleware, as it provides
an example.

## Authors
+ Justin Quick <justquick@gmail.com>
+ Paul Michali <pmichali@gmail.com>

## Current Version
+ 0.2.0

## Summary
Django X Power is a simple middleware that adds the ``X-Powered-By`` header to any Django site.


## Install
From PyPI, you can install version 0.1.0:
```
pip install django-xpower==0.2.0
```

For version 0.2.0, you can install from GitHub with:
```
poetry add git+https://github.com/pmichali/django-xpower.git
```

## Using in Django
In the project's `setting.py`, add this middleware to the Middleware class list:

    MIDDLEWARE_CLASSES = (
        'django_xpower.middleware.XPoweredByMiddleware',
        ...
    )

You can configure what you want for the X-Powered-By header by setting the following variable
in `settings.py`:

    X_POWERED_BY = 'Django'
    
If you do not set this it will use the default which is `Django/%(version)s`
where `%(version)s` is replaced with the version of Django that you are using.

## Notes
Using poetry in this project to define the dependencies (currently Django 5.0+, python 3.9+).
However, you can use whatever dependency management tool desired. If you want to use poetry,
you can install it on your platform and then use `poetry shell` to setup your environment.

## Testing
An example project is provided to test. Using poetry, here are the steps to test the middleware:

    poetry shell
    cd example
    python3 manage.py runserver
    curl -i http://localhost:8000 | head

You should see something like this:

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

## Version History
 * 0.2.0 Updated for newer Django version (5.0). Using Poetry for version control, and newer packaging
 * 0.1.0 Initial release
