Admin Sys
=========

:date: 2014-09-23 10:20
:tags: admin
:slug: admins
:authors: Ferry Jérémie
:summary: Utilisation sur un serveur
:lang: fr

Vous désirez utiliser LinkManager en temps que serveur et vous connaisser l'admin linux sur le bout des doigts?
Vous êtes le bien venu! Mes connaissances sont loin d'être parfaite et une relecture ne serait pas déplaisante.

Installation sur un serveur dédié
---------------------------------

Pour cela, j'utilise :
- le serveur Nginx (plus approprié que Apache pour l'asynchrone, pour la Ram, le nombre de client en simultanné supporté etc.)

  http://joeandmotorboat.com/2008/02/28/apache-vs-nginx-web-server-performance-deathmatch/

- uwsgi : plus performant que gunicorn à priori (pas fait de bench)

  http://www.peterbe.com/plog/fcgi-vs-gunicorn-vs-uwsgi

  http://nichol.as/benchmark-of-python-web-servers

- supervisor (relancer LM au cas ou il y aurait un bug ... presque inutile ^^)

  Pourrais sans doute être remplacé par systemd. (ou d'autres technos plus vielles/bancales : launchd ou runinit)

J'ai utilisé des technos "hypes" sans pour autant garantir qu'elles sont les plus adaptés.
Pour celà, un bench serait le bienvenue...

::


                                      +------------------------------------------------------------------------------------+
                                      :                                        SERVER                                      |
                                      |                                                                                    |
                                      |     +------------------------------------------------------+                       |
 +-------------------------+          |     |                      Supervisor                      |                       |
 :{c}         WEB          |          |     |  (Surveille le bon fonctionnement de NGINX et UWSGI) |                       |
 |                         |          |     +------------------------------------------------------+                       |
 |                         |          |              |                             |                                       |
 |                         |          |              |                             |                                       |
 |                         |          |              |                             |                                       |
 | /------------------\    |          |              v                             v                                       |
 | | Internaute **1** |----|----      |     +-----------------+       +-------------------------+       +---------------+  |
 | \------------------/    |    \     |     |                 |       |                         |       |               |  |
 |         .               |     -----|---->|      NGINX      |       |     UWSGI               |       |  LinkManager  |  |
 |         .               |          |     |                 |<----->|                         |<----->|               |  |
 |         .               |     -----|---->| (Proxy Inverse) |       | (Serveur d'application) |       |               |  |
 | /------------------\    |    /     |     |                 |       |                         |       |               |  |
 | | Internaute **n** |----|----      |     +-----------------+       +-------------------------+       +---------------+  |
 | \------------------/    |          |              |                                                          ^          |
 |                         |          |              |                                                          |          |
 +-------------------------+          |              v                                                          v          |
                                      |   +-------------------------------+                             +---------------+  |
                                      |   |{d}                            |                             |{s}            |  |
                                      |   |        Contenu statique       |                             |     Redis     |  |
                                      |   | (js, css, images, fonts etc.) |                             |               |  |
                                      |   +-------------------------------+                             +---------------+  |
                                      |                                                                                    |
                                      +------------------------------------------------------------------------------------+


Attention, cette configuration sert d'exemple.
Il est fort probable que pour des questions d'optimisation, vous changiez le nombre de cpus et de threads utilisés.
(soit dans supervisor, nginx, uwsgi et même dans LinkManager)

Pour en avoir le coeur net :

.. code-block:: bash

    lscpu

De même, les règles de caching restent approximatives et pourraient être améliorés, selon le cas, par une gestion du cache en RAM.
(Nginx peut cacher en Ram via Memcached, Redis, tempfs etc.)

Tâches Cron/Anacron
-------------------

Vous désirez garder une trace de votre base de donnée et la sauvegarder régulièrement?
Il est bien évidement possible d'utiliser la périodicité sous linux.

Perso, je lance ceci en "daily" via anacron: (en user mode)

.. code-block:: bash

    linkm dump >| $HOME/backup/linkmanager/$(date +"%d_backup.json")
