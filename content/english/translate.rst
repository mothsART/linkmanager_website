Traduction
##########

:date: 2014-09-23 10:20
:tags: traduction
:slug: traduction
:authors: Ferry Jérémie
:summary: Traduction
:lang: en

LinkManager est traduit en 2 langues actuellement : le français et l'anglais.

Ce n'est sans doute pas parfait et une aide en ce sens n'est vraiment pas inutile...

J'ai évidement attribué à chaque chaîne de caractère de pouvoir être traduite... en utilisant Gettext.

Pour simplifier la traduction, j'ai pompé allègrement (mais adapté quand même) les merveilleux outils du projet Django.
Du coup, en ce mettant à la racine, un

.. code-block:: bash

    ./makemessages

parcourera le projet afin d'y chercher de nouvelles chaines de caractères à traduire.

et un

.. code-block:: bash

    ./compilemessages

compilera les fameuses chaines traduites.

Si on veut les 2 en 1:

.. code-block:: bash

    invoke trans
