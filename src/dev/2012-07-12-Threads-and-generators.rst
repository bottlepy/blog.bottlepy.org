Thread-locals and Generators
#############################

:date: 2012-07-13
:author: Marcel Hellkamp

Looks like the next release (0.11) will break backwards compatibility in some edge cases. I am working on a patch that affects routes that stream content (yield) and access request/response after the first chunk of data is returned.

Details
----------

Accessing the thread-local request/response objects after yielding a chunk of data works most of the time, but is a bad idea anyway. The request context (the state of request/response) is undefined at that point. As soon as the route callback yields data, Bottle hands the response over to the WSGI server and is no longer in control. The server might start a new thread to send the stream to a client and thus break the thread-local request/response proxies. That'd be a very subtle bug and hard-to-debug scenario.

It worked until now because bottle does not delete the context, it just overwrites it as soon as a new request arrives.

Whats new?
----------

The thread-local request/response proxies will raise a RuntimeError() if they are accessed outside of a request-cycle (before a request or after the first chunk of data is returned).

How to upgrade?
--------------------

There are two new ways to get a real, local, persistent instance to the current request object: bottle.get_current_request() and bottle.request.get_current(). The object returned by these functions survives as long as you keep the reference around:

.. code-block:: python
    
    @route('/stream')
    def stream():
        # Get a local reference BEFORE returning data
        local_request = request.get_current()
        # Now we can use that instead of the global proxy
        for i in range(100):
            yield 'Hello %s!' % local_request.forms.name



As said above, the change is not committed yet. I am still experimenting. Just wanted to write it down to clear my head. The matter is even more complicated than explained here.
Diesen Beitrag minimieren
