More robust Auto-reload
#######################

:date: 2011-11-15
:author: Marcel Hellkamp

The Bottle auto-reload feature got an upgrade today: It is now able to handle syntax and import errors in your application or imported modules. Just start the server with the new command-line interface and give it a try:

.. code-block:: bash

  bottle.py --debug --reload package.module:app

I had to change a lot of the reloading code to achieve this and was not able to test it with windows yet. If you have some time and a windows machine at hand, please try and tell me if anything goes wrong.
