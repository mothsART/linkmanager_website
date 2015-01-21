#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'J\xe9r\xe9mie Ferry'
SITENAME = 'LinkManager'
SITEURL = 'http://linkmanager.io'
SITE_DESCRIPTION = "Manage Urls on terminal and/or with an web app!"
#ABSOLUTE_SITEURL = "http://linkmanager.io"

TIMEZONE = "Europe/Paris"

DEFAULT_LANG = 'fr'
RELATIVE_URLS = True

PATH = "content"
# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'}
}
# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'images',
    'extra/robots.txt'
]

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS =  (('Pelican', 'http://getpelican.com/'),
#           ('Python.org', 'http://python.org/'),
#           ('Jinja2', 'http://jinja.pocoo.org/'),
#           ('You can modify those links in your config file', '#'),)
PLUGIN_PATHS = ['plugins/pelican-plugins']
PLUGINS = [
    'assets', 'sitemap', 'gravatar',
    'i18n_subsites', 'tipue_search'#, 'disqus_static'
]

I18N_SUBSITES = {
    'fr': {
        'SITENAME': 'LinkManager',
    },
    'en': {
        'SITENAME': 'LinkManager',
    }
}

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = "themes/pelican-bootstrap3"
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

TAG_CLOUD_MAX_ITEMS = 30

# Code highlighting
PYGMENTS_STYLE = 'emacs'
PYGMENTS_RST_OPTIONS = {'linenos': 'table', 'anchorlinenos': '', 'linespans': 'line', 'lineanchors': 'code'}

DISQUS_SITENAME = 'linkmanager.io'
DISQUS_SECRET_KEY = 'gN5rHfwoTzkW2JQZU0soYRmrxc9GTJjk7yNSvrL9ipajQzL0SCoOxQ7k0vvDjsYg'
DISQUS_PUBLIC_KEY = 'P2aOBdvavl7uOirHbslqm2o9pyewxi4xMDm5h9o3wLtdeliWIRcHERI2WGK2AKPE'
