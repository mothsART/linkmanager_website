Roadmap
#######

:date: 2014-09-23 10:20
:tags: roadmap
:slug: roadmap
:authors: Ferry Jérémie
:summary: L'avenir de LinkManager
:lang: en

Roadmap pour la 0.4
-------------------

- I18N update* Rajout de tests unitaires (dont un jsonschema pour les import/export :
  https://github.com/Julian/jsonschema) avec une meilleur couverture et éventuellement des tests sur la partie web
- Maj sur pypi et de mon ppa (je vais aussi mettre une option de mise à jour de sa base pour éviter de faire la manip proposé précédement)
- Paquet pour ArchLinux (j'ai 2 ordi sur 3 maintenant sous Arch)

Roadmap pour la 0.5
-------------------

- Linkmanager en mode "server"

- Caching des pages :
  si la page a changé depuis son enregistrement, un diff sera possible via la version web
- Rajout de flux rss
- Multi-pages avec une option de configuration (ex: MAX_RESULTS_BY_PAGE = 10)
- Nuage de tags avec la possibilité d'en glisser/déposer.
- Possibilité d'avoir le favicon et un aperçu du site au survol.(imprim écran)

Roadmap encore indéfini
-----------------------

- La possibilité de changer la configuration de linkmanager dans l'interface web
- Utilisation d'autres BDD que Redis : MongoDB, SQLite, PostGreSQL etc.
- Benchmarks
- Import/export avec Delicious et/ou Evernote
- Doc exhaustive sur http://readthedocs.org
- Amélioration du manpage (et version en français)
- Mise en ligne d'une version démo on-line + site de présentation du projet (sans doute créé avec pelican: http://blog.getpelican.com/ donc sous forme de blog avec une version français/anglais)
- maj de la doc sous ubuntu-fr
