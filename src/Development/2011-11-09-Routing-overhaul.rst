Routing Overhaul
#################

:date: 2011-11-09
:author: Marcel Hellkamp

It took some time, but the new routing code is finished.

Highlights:

* New wildcard syntax: ``/object/<id:int>``
* Wildcard filtering/validation as part of the route syntax
* Support for custom wildcard filters
* Faster url() building
* Better error messages
* Much simpler code (I dropped CGI optimization)
* Lots of documentation
* (the old syntax still works)

You can read about it `in the docs <http://bottlepy.org/docs/dev/routing.html>` and test it in the "routing" branch. I am very exited about this feature and think it is important enough to trigger a new release. Please give it a try and test it with your applications. Any feedback may help to get this stable enough for a release.

