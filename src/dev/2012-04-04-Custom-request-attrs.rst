Custom Request Attributes
#############################

:date: 2012-04-04
:author: Marcel Hellkamp

This might be useful for Plugin developers:
https://github.com/bottlepy/bottle/commit/a21d71694fdea222844dba5076efad3726ccdb68

To sum it up: You can now add custom attributes or properties to the bottle.request object. These are stored in the environ dictionary ('bottle.request.ext.*' namespace) which has some advantages over traditional instance attributes:

* User defined attributes don't leak into other requests.
* They are garbage-collected soon after the request is over.
* You can add or read these values from low-level middleware or via plugins.

Something like bottle.request.db or bottle.request.session is now feasible. You can add methods, too (using types.MethodType(func, bottle.request)).
