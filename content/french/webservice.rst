Webservice
==========

:date: 2014-11-13 21:20
:tags: webservice api
:slug: webservice
:authors: Ferry Jérémie
:summary: Utiliser LinkManager en tant que webservice
:lang: fr

Introduction
------------

LinkManager n'a pas été initialement créé pour être utilisé en tant que webservice.
Néanmoins, l'ensemble des échanges du client web avec le coeur se fait via un serveur Flask et des échanges en Json!

L'api web qui suit utilisera comme préfixe **<url>** qui représente dans le cas de ce site l'adresse http://195.154.252.48/linkmanager/demo/


Suggestion de tags
------------------

* requête GET (avec 2 mots clés : **linux** et **dev**) :

**<url>**/linkmanager/demo/suggest?tags=linux+dev

* exemple de réponse (en Json) :

.. code-block:: json

    {
        "linux developpement": 10,
        "linux developper": 8
    }

On a 2 réponses => la clé donne les tags suggérés et la valeur du **poid** associé.


Recherche de l'ensemble des liens
---------------------------------

* requête GET sans mots clés :

**<url>**/search

* réponse :

retourne l'ensemble des liens


Recherche à partir de tags
--------------------------

* requête GET (avec 2 mots clés : **linux** et **developpement**) :

**<url>**/search?linux+developpement

* exemple de réponse (en Json) :

.. code-block:: json

    {
      "http://linuxfr.org": {
        "author": "root",
        "description": "french geek website",
        "init date": "2014-10-06T17:07:55.366679+02:00",
        "l_uuid": "efc4401b-e032-41f4-9628-11a6a23200f9",
        "priority": "1",
        "tags": [
          "developpement",
          "linux"
        ],
        "title": "Accueil - LinuxFr.org"
      }
    }