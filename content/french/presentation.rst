LinkManager
###########

:date: 2014-09-23 10:20
:tags: presentation
:slug: presentation
:authors: Ferry Jérémie
:summary: Présentation de LinkManager
:lang: fr

Présentation
------------

LinkManager répond à un besoin précis :
Gérer ses marques-pages (favoris ou bookmark) de manière optimale.

Etant initialement un projet perso, il est assumé comme un soft pour un public
averti avant tout. (soft de développeur pour développeur)

Points de départ
----------------

Le projet par de plusieurs constats de l'auteur :
    1. Pourquoi un marque-page?
       Si l'on veut archiver un lien, c'est qu'il y a une raison précise!

       D'une part, l'adresse n'est pas facilement mémorisable.

       De l'autre, on désire reporter sa lecture ou relecture pour diverses raisons.

       Enfin, ce lien peut être désigné à du partage.

       La lecture peut être différé à une date précise ou non.

       Si on prend le temps d'archiver, c'est pour retrouver et en l'état.
       L'outil de recherche après archivage est donc primordial.

       De même, tomber sur un site down (temporaire ou non) ou avec du contenu
       modifié est innacceptable.
    2. Nous utilisons de plus en plus de périphériques pour accéder à internet.

       Devoir se rappeler avec quel ordinateur/smartphone + quelle navigateur nous avons visités tel lien remet
       en soit la nécessité d'un archivage...
    3. **Mes marques-pages m'appartiennent**. Elles ne devraient pas transiter par
       des services tiers (cloud) tel que Google dashboard, Delicious et/ou
       Evernote.

       Je ne détaillerais pas sur les effets de bord de ces services souvent
       **gratuits**.

       L'auto-hébergement devrait être une solution **possible**.
    4. Les principaux navigateurs sont bien trop gourmands (ram, CPU) pour 90% de notre
       utilisation : pour lire du contenu textuel, pas besoin de webGL, SVG,
       javascript et autre truc hype.
    5. Les gestionnaires de marques-pages de ces dit navigateurs sont obsolètes :
       au delà de 100 marques-pages, le stockage par arborescence demande
       beaucoup de rigueur et d'investissement, nécessite un service de cloud
       (firefox sync) pour le partager facilement sur plusieurs périphériques et
       est inter-dépendant au navigateur.
    6. La ligne de commande est l'outil quotidien d'un développeur chevronné et il n'a pas forcément besoin
       d'utiliser une appli graphique (un navigateur boulémique de surcroit).
    7. Du sur-mesure.
       Ma méthode d'archivage/recherche/lecture m'est propre.
       Pouvoir adapter ses outils à ses besoins me semble évident.

Qu'est-ce que LinkManager?
--------------------------

LinkManager a été créé dans le but de combler plusieurs manques :
    - un outil de gestion de marques-pages en cli (ligne de commandes) avec la
      présomption de poser cette question : est-il forcément utile d'utiliser un
      gros navigateur web (firefox, chrome etc.) pour lire du contenu textuel?
      Il est tout a fait possible de rester sur son terminal grâce à des
      navigateurs en ligne : elinks, lynx, w3m, links2, jumanji (pour ne citer
      que les plus connus) ou dans une moindre mesure des navigateurs léger :
      Dillo, uzbl.
    - une interface web afin d'étendre ou compléter le soft en cli si besoin.
    - un logiciel léger (non dépendant d'un navigateur principalement) remplissant
      la charte UNIX : un logiciel devrait faire une seule chose et bien.
    - de l'auto-hébergement : plutôt que de dépendre de services tiers (en cours
      de réalisation)
    - un soft orienté recherche : auto-complétion des étiquettes (tags)

Il utilise pleinement Python 3 : .. image:: https://caniusepython3.com/project/linkmanager.png?style=flat
    :target: https://caniusepython3.com/project/linkmanager

Sous le capot
-------------

Les fonctionnalités, c'est bien beau mais pour qu'un soft soit stable,
maintenable, scalable, il lui faut des bases solides.
LinkManager a été développé en python et librairies associés.
Il est construit autours de la culture Unix/Linux.

Une configuration par défaut pouvant être remplacé par une config perso :
    - pour tous les utilisateurs (/etc/linkmanager.conf)
    - pour un utilisateur (~/.config/linkmanager.conf)

Comme tout programme en cli, il dispose d'un manpage. (**man linkmanager** ou **man linkm**)
Pour une ergonomie réussi, LinkManager dispose de l'auto-complétion sur Bash et
Zsh.
Il utilise une Base de donnée NoSQL : Redis pour sa simplicité et sa grande
capacité de scalabilité.

LinkManager repose sur des tests unitaires et des tests fonctionnels sous la
forme de scénarios d'utilisation.sous la forme de scénarios d'utilisation.
Une couverture de code (coverage) permet d'éviter au maximum des zones non testés laissant place à des bugs d'étourderie ou de régression.
Les tests unitaires sont encadrés par des "Mock objets" afin de simuler des
librairies complexes tel que les appels à la base de donnée.
Enfin, le projet garde un contrôle évident sur chaque nouvelle version grâce à
des principes d'intégration continue : Tox et TravisCI.

Pour des raisons évidentes de scalabilité, il est prévu de mettre en place des
scénarios de benchmarks...

License
-------

BSD : évite tout frein à une quelconque participation. (sans trop de réflexion)

Contrat non rempli ?
--------------------

LinkManager n'a pas (encore) la prétention de répondre à tous les besoins.
Il pose des jalons et sert de plate-forme pour des plugins.

Et après ?
----------

Voici les fonctionnalités à venir : `Roadmap <|filename|/french/roadmap.rst>`_

Participation
-------------

Il y a plusieurs manières de participer activement à ce projet :
    - Si vous êtes développeur :
        - le projet github peut être facilement forkés.
        - des plugins *innovants* peuvent être envisagés.

      Voir la page `Développeur <|filename|/french/developper.rst>`_

    - Si vous êtes administrateur système :
        - proposer des tutoriaux d'installation de LM sur un serveur

      Voir la page `Admin Sys <|filename|/french/admin.rst>`_
    - Si vous êtes polyglotte : le soft a été pensé *i18n*;
      il peut donc être traduit dans d'autre langue que le français ou l'anglais.

      Voir la page `Traduction <|filename|/french/translate.rst>`_

    - Si vous êtes intégrateur, graphiste ou ergonome... vous avez votre mot à dire.

    - Si vous êtes utilisateur : parlez-en autours de vous, remonter les bugs.

Concurrents
-----------

- cozy.io avec son plugin "bookmarks" https://demo.cozycloud.cc/#apps/bookmarks/
- Shaarli : https://github.com/sebsauvage/Shaarli

- l'extension Chrome "Bookmark Manager" : http://www.developpez.com/actu/76841/Google-annonce-Bookmark-Manager-une-extension-pour-mieux-gerer-ses-favoris-sur-Chrome/

- raindrop.io

- https://addons.mozilla.org/fr/firefox/addon/scrapbook/

On en parle
-----------

Je référence quelques liens ou l'on parle de LinkManager :

- http://doc.ubuntu-fr.org/linkmanager
