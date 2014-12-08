Template Search-Path Workaround
===============================

:date: 2012-07-20 17:00
:tags: workaround templates
:author: Marcel Hellkamp

One of the most annoying limitations you may encounter in bottle when building bigger applications is the way templates are searched on the file system. At the time the 
template system was designed, nobody thought about multi-app projects, third-party apps, ``Bottle.mount()`` and the complexities these features introduce. The typical 
bottle applications consisted of one application in a single file. Using module-globals (e.g. ``bottle.TEMPLATE_PATH``) just worked.

Today, Bottle is more a general-purpose low-overhead framework than a micro-framework. We still focus on small applications, but try to remove the limitations so the 
framework can grow with your project. Plugins and the ability to mount sub-applications are just two examples.

The Problem
------------

Currently, Bottle uses a global list of search paths (``bottle.TEMPLATE_PATH``) to find templates on the file system. Even worse, this list contains relative paths. This 
might break in two ways:

#. Your current working directory (``./``) is not where you expect it to be.
#. You run more than one bottle application at the same time.

The first is `covered in the docs <http://bottlepy.org/docs/dev/faq.html#template-not-found-in-mod-wsgi-mod-python>`_. The second scenario is a bit more tricky.


Workaround
-----------

The obvious solution is to make templates and their configuration application-bound. Then you could define separate search paths for each application and make them 
relative to the applications install path. We are working on a feature that does exactly this.

While this feature is in the works, this workaround might help:

.. code-block:: python

    import bottle
    import os.path, functools
    
    # Create a new list with absolute paths
    MY_TEMPLATE_PATH = [
       os.path.abspath(os.path.join(os.path.dirname(__file__), './views')),
    ]

    # Patch @view() so it uses the customized path list instead of the global one
    view = functools.partial(bottle.view, template_lookup=MY_TEMPLATE_PATH)

Sill, this does not solve all problems. Templates are cached by their name. If two applications load different templates that have the same name, they mix up.

To get this workaround to actually work, I implemented a `quick fix <https://github.com/bottlepy/bottle/commit/cecbd04fc80e44f0b422b5bb7a894563102bed7f>`_ and
pushed it to the repository. The ID of the template lookup path list is now part of the cache key. It’s not a perfect solution, but at least allows for a
decent workaround while we are working on a `real` solution.

