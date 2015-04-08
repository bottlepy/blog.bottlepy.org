Virtualenv and Makefiles
########################

:date: 2012-07-16
:author: Marcel Hellkamp

Whenever I start a new project that is likely to have dependencies, I set up `virtualenv <http://www.virtualenv.org/>`_ and create a `requirememnts.txt <http://www.pip-installer.org/en/latest/requirements.html>`_. I am also a big fan of `Makefiles <http://www.gnu.org/software/make/manual/make.html>`_. Here is a small snippet that combines these tools:

.. code-block:: make

    # Makefile
    venv: venv/bin/activate
    venv/bin/activate: requirements.txt
        test -d venv || virtualenv venv
        venv/bin/pip install -Ur requirements.txt
        touch venv/bin/activate

So, what does it do? The ``venv`` target builds your virtual environment and keeps it in sync with your ``requirements.txt``. If everything is up-to-date, nothing happens. You can use the `venv` target as a dependency for other targets or call ``make venv`` to build or update the virtual environment manually. Just as an example:

.. code-block:: make

    devbuild: venv
        venv/bin/python setup.py install

    test: devbuild
        venv/bin/python test/runtests.py


Nothing special, but very handy. Especially if your users are new to python and don't know much about virtual environments.

