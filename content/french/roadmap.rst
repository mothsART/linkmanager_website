Roadmap
#######

:date: 2014-09-23 10:20
:tags: roadmap
:slug: roadmap
:authors: Ferry Jérémie
:summary: L'avenir de LinkManager
:lang: fr

Roadmap pour la 0.4
-------------------

- **DONE** I18N update
- **DONE** Maj sur Pypi

Roadmap pour la 0.4.1
---------------------

- EditMode gardé en mémoire
- L'édition du fichier de configuration est pris en compte en "live"
- **DONE** Résoudre les bugs liés à la mise en production. (soucis d'urls relatives)
- Rajout de tests unitaires (dont un jsonschema pour les import/export :
  https://github.com/Julian/jsonschema) avec une meilleur couverture et éventuellement des tests sur la partie web
- Maj sur pypi et de mon ppa
- tests unitaires de Flask avec pytest : https://pypi.python.org/pypi/pytest-flask
- [webserver] :
    - favicon
    - fenêtre modale pour la suppression (évite les accidents) + paramètrage
    - **DONE** update amélioré (rapidité d'execution + factorisation du code)
    - ajout amélioré
    - Paramètrage : suppression et/ou modification bloqué

Roadmap pour la 0.5
-------------------

- Paquet pour ArchLinux (j'ai 2 ordi sur 3 maintenant sous Arch)
- Linkmanager en mode "server":
    - fichiers de log : activité et erreurs

- Caching des pages :
  - si la page a changé depuis son enregistrement, un diff sera possible via la version web
  - option de taille du cache (du coup, jauge de remplissage), de l'emplacement
- Possibilité d'avoir le favicon et un aperçu du site au survol.(imprim écran)
- [webserver] :
    - i18n
    - ajout de filtres (rechercher tout sauf ce qui se rapporte au tag "cuisine" par exemple)
    - Nuage de tags avec la possibilité d'en glisser/déposer.
    - Multi-pages avec une option de configuration (ex: MAX_RESULTS_BY_PAGE = 10)
    - Rajout de flux rss sortants

Roadmap encore indéfini
-----------------------

- Ajout "automatiques" à partir de flux Rss/Atom
    - possibilité de filtrer
- Auto-tag de certains sites :
    - ex: une URL sous Youtube fournira d'emblé un tag "vidéo"
- Correction Orthographique sur les commentaires et titres :
  Utilisation de "Hunspell spellchecker" si possible, sinon Aspell.
- Correction Grammatical sur les commentaires et titres (on peut rêver) :
  http://cgit.freedesktop.org/libreoffice/lightproof/
- La possibilité de changer la configuration de linkmanager dans l'interface web
- Utilisation d'autres BDD que Redis : MongoDB, SQLite, PostGreSQL etc.
- Benchmarks
- Import/export avec Delicious et/ou Evernote
- Doc exhaustive sur http://readthedocs.org
- Amélioration du manpage (et version en français)
- Mise en ligne d'une version "démo" + site de présentation du projet (sans doute créé avec pelican: http://blog.getpelican.com/ donc sous forme de blog avec une version français/anglais)
- maj de la doc sous ubuntu-fr
- création d'un fuzzer spécialement dédié à LinkManager via "Fusil"
