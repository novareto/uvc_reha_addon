===============================
Cookiecutter Namespace Template
===============================

`Cookiecutter <https://github.com/audreyr/cookiecutter>`_ Namespace Template
for a Python package.

|Downloads| |Updates| |Versions| |Contributors| |License| |Docs|

.. |Downloads| image:: https://pepy.tech/badge/cookiecutter-namespace-template
   :target: https://pepy.tech/project/cookiecutter-namespace-template
.. |Updates| image:: https://pyup.io/repos/github/veit/cookiecutter-namespace-template/shield.svg
   :target: https://pyup.io/repos/github/veit/cookiecutter-namespace-template/
.. |Versions| image:: https://img.shields.io/pypi/pyversions/cookiecutter-namespace-template.svg
   :target: https://pypi.org/project/cookiecutter-namespace-template/
.. |Contributors| image:: https://img.shields.io/github/contributors/veit/cookiecutter-namespace-template.svg
   :target: https://github.com/veit/cookiecutter-namespace-template/graphs/contributors
.. |License| image:: https://img.shields.io/github/license/veit/cookiecutter-namespace-template.svg
   :target: https://github.com/veit/cookiecutter-namespace-template/blob/master/LICENSE
.. |Docs| image:: https://readthedocs.org/projects/cookiecutter-namespace-template/badge/?version=latest
   :target: https://cookiecutter-namespace-template.readthedocs.io/en/latest/

Features
--------

* Testing setup with ``unittest`` or ``pytest``
* `Tox <https://tox.readthedocs.io/>`_ testing: Setup to easily test for Python
  3.5, 3.6, 3.7, 3.8
* `Sphinx <http://www.sphinx-doc.org/>`_ docs: Documentation ready for
  generation with, for example, ReadTheDocs_
* `bump2version <https://github.com/c4urself/bump2version>`_: Pre-configured
  version bumping with a single command
* Optional auto-release to `PyPI <https://pypi.org/>`_ when you push a new tag
  to master (optional)
* Optional command line interface using `Click
  <https://palletsprojects.com/p/click/>`_

If you really want to create a new package with Python 2, in spite of the
`Python 2.7 countdown <https://pythonclock.org/>`_ and the `Sunsetting Python 2
support <https://python3statement.org/>`_, then use
``cookiecutter-namespace-template`` <0.2.

Quickstart
----------

#. Install the latest Cookiecutter if you haven’t installed it yet (this requires
   Cookiecutter 1.4.0 or higher)::

    $ pip install -U cookiecutter

#. Generate a Python package project::

    $ cookiecutter https://github.com/veit/cookiecutter-namespace-template.git

#. Create a repo and put it there.

#. `Register <https://pypi.org/account/register/>`_ your project with PyPI.

#. Add the repo to your `ReadTheDocs <https://readthedocs.io/>`_ account and
   turn on the ReadTheDocs service hook.

#. If you want to add the pyup badge to your README file
   
   #. create a new account at `pyup.io <https://pyup.io>`_ or log into your
      existing account
   #. click on the green *Add Repo* button
   #. click *Pin* to add the repo

#. Release your package by pushing a new tag to master.

Pull requests
~~~~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. I also accept pull requests on this, if they’re
small, atomic, and if they make my own packaging experience better.

