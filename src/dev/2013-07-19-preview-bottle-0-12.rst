====================
Preview: Bottle 0.12
====================

:date: 2013-07-19 18:00
:tags: preview
:author: Marcel Hellkamp

Some time has passed and some really nice features have found their way into the bottle core framework. As we are now preparing for the new release, let me show you the most important changes and `let us know <mailto:bottlepy@googlegroups.com>`_ what you thin about it!

As promised: All changes are **fully backwards compatible** to the **last stable release (bottle-0.11)** and all deprecated APIs print a warning to make the transition as easy as possible.

Configuration
=============

Bottle had the ``app.config`` attribute for a while now, but it was poorly documented  and not very useful in its old state. The "Uppercase attributes are namespaces" feature just felt odd and I have not seen a single project or plugin that actually uses it that way. It ws time to re-think the whole application-configuration topic and make it right.

The new `ConfigDict() <http://bottlepy.org/docs/dev/configuration.html#bottle.ConfigDict>`_ implementation of the `Bottle().config <http://bottlepy.org/docs/dev/api.html#bottle.Bottle.config>`_ attribute is `well documented <http://bottlepy.org/docs/dev/configuration.html>`_ and has some very nice features.

* **Speed:** *ConfigDict* is subclass of *dict* and has zero overhead for read operations. Yes, it is as fast as a build-in dictionary for all read operations (item access, the ``get()`` method and so on).
* **Namespaces:** Plugins and applications can use a ``dot.separated.name_spaces`` scheme to avoid name collisions (e.g. ``plugin_name.field_name``). Many features directly support this kind of name-spacing, but it is not enforced.
* **Config Files:** The *ConfigDict* can load values from `ini-style config files <http://docs.python.org/2/library/configparser.html>`_ or nested dictionaries (e.g. from json or YAML files).
* **Config Hook**: The application is notified on changes to the config dictionary and fires the new ``config`` hook. Plugins can listen to that hook and re-configure themselves at run-time.
* **Meta Fields and Validators:** Next to the actual value, each config key can be associated with named meta fields that offers a lot of possibilities. Currently implemented is the ``filter`` field. If this field holds a callable, that callable is used to filter new values as soon as they are assigned to the associated config key. Plugins can implement validators or just enforce a specific type for their config values this way. I am sure we find other use cases in the future. Oh, and the ``help`` meta field may be displayed by a future in-browser administration tool, perhaps? *\*hint hint\**

For examples and more details have a look at the new `Configuration article <http://bottlepy.org/docs/dev/configuration.html>`_.

Routing
=======

Thanks to the awesome work of *Nicolas Vanhoren*, we got rid of the `routing order problems with overlapping rules <http://bottlepy.org/docs/0.11/routing.html#routing-order>`_ that were caused by our optimization code. The new implementation is as fast as the old one (slightly faster for some scenarios), but without the reordering and grouping special cases of the old implementation.

Additionally we added `Route.get_undecorated_callback() <http://bottlepy.org/docs/dev/api.html#bottle.Route.get_undecorated_callback>`_ and `Route.get_callback_args() <http://bottlepy.org/docs/dev/api.html#bottle.Route.get_callback_args>`_ to allow inspection of the request callback even if decorators were applied directly (not using the ``route(apply=...)`` feature).

Templating
==========

Our built-in template engine called "SimpleTemplate" (or `stpl` for short) got a lot of attention in 0.12! Most of the changes are internal, but some new features were added, too:

* **Multiline Code Blocks:** Instead of starting each code line with a ``%``, you can now use ``<?`` and ``?>`` to mark a whole block of python code. That should save a lot of typing.
* **Include/rebase Functions:** The ``include`` and ``rebase`` keywords are functions now. The most important benefit is that you can specify the target template in a variable (e.g. ``% include(variable_with_template_name, ...)``). Apart from that, we follow the Python3 philosophy (print as a function) and reduce unnecessary magic with this decision. By the way: ``include()`` returns the namespace of the included template. Nice, eh?

Documentation is still lacking, though. Anyone?

File Uploads
============

The ``cgi.FieldStorage`` API is poorly documented and behaves... strange in some ways. We replaced it with `FileUpload() <http://bottlepy.org/docs/dev/api.html#bottle.FileUpload>`_, a new class that has some very nice additional features.

* **Safe Filename:** The ``.filename`` attribute contains a normalized version of the client side file name to ensure maximum file system compatibility (lowercase, no whitespace, no path separators, no unsafe characters, ASCII only).
* **Save to Disk:** ``FileUpload().save(destination, overwrite=False)`` saves a file upload to disk or copies its content to an open file(-like) object in a memory-efficient way. You can specify a directory as destination. In that case the ``.filename`` attribute is added to the path automatically. Existing files are not overwritten, unless you explicitly allow it.

Apart from that, it is mostly compatible with the old ``cgi.FieldStorage`` API.

Documentation
=============

Yes, we have a `Chinese translation <http://bottlepy.org/docs/dev-cn/>`_.


