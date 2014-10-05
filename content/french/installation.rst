Installation
============

:date: 2014-09-23 10:20
:tags: installation
:slug: installation
:authors: Ferry Jérémie
:summary: Installation
:lang: fr

Via Ubuntu (13.10 and 14.04 exclusively)
----------------------------------------

.. code-block:: bash

    add-apt-repository -y ppa:jerem-ferry/linkmanager
    apt-get update
    apt-get install linkmanager

Via Pypi (Python >= 3.3)
------------------------

Linkmanager depends on redis Database and GIT (personnal "clint" version). You must install it like this (on debian/ubuntu) :

.. code-block:: bash

    sudo apt-get install redis-server git

.. code-block:: bash

    sudo pip3 install linkmanager

To enjoy "completion", you normaly should do nothing. A "sudo pip install" should add it automatically. Otherwise, just put that line in your ~/.bashrc (or ~/.zshrc) :

.. code-block:: bash

    eval "$(register-python-argcomplete linkm)"
