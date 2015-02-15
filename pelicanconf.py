#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jérémie Ferry'
SITENAME = 'LinkManager'
SITEURL = 'http://195.154.252.48/linkmanager'
SITEURL = 'http://127.0.0.1:8000'
SITE_DESCRIPTION = "Manage Urls on terminal and/or with an web app!"
ABSOLUTE_SITEURL = 'http://195.154.252.48/linkmanager'
# ABSOLUTE_SITEURL = "http://linkmanager.io"


TIMEZONE = "Europe/Paris"

DEFAULT_LANG = 'en'
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

DATE_FORMATS = {
    'en': '%Y-%m-%d',
}

# Blogroll
# LINKS =  (('Pelican', 'http://getpelican.com/'),
#           ('Python.org', 'http://python.org/'),
#           ('Jinja2', 'http://jinja.pocoo.org/'),
#           ('You can modify those links in your config file', '#'),)
PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'assets', 'sitemap', 'gravatar',
    'tipue_search', 'disqus_static'
]

I18N_SUBSITES = {
    'fr': {
        'SITENAME': 'LinkManager'
    },
    'en': {
        'SITENAME': 'LinkManager'
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
SOCIAL = (
    ('Github account', 'https://github.com/mothsART/linkmanager'),
    (
        'French topic about avancement',
        'http://forum.ubuntu-fr.org/viewtopic.php?id=1534131'
    ),
)

DEFAULT_PAGINATION = 10

THEME = "themes/pelican-bootstrap3"

TAG_CLOUD_MAX_ITEMS = 30

# Code highlighting
PYGMENTS_STYLE = 'emacs'
PYGMENTS_RST_OPTIONS = {
    'linenos': 'table',
    'anchorlinenos': '',
    'linespans': 'line', 'lineanchors': 'code'
}

DISQUS_SITENAME = 'linkamanager'
DISQUS_CATEGORY_ID = "3506724"  # Dev

DISQUS_SECRET_KEY = 'Iq1skapIEykejHa4FwVcbomNJOKkm4CoUhTHXwiKrnNrWFDMRYvo6VUcbS5c5ode'
DISQUS_PUBLIC_KEY = 'YbVM9ctM6uTgnAAWrezSFa1rwCiRhhNjjaPwBI9dmgcHJVYCmbw3PpwNgHcLdGzN'
