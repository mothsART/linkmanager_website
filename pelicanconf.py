#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'J\xe9r\xe9mie Ferry'
SITENAME = u'LinkManager'
#SITEURL = 'linkmanager.io'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
RELATIVE_URLS=True

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS =  (('Pelican', 'http://getpelican.com/'),
#           ('Python.org', 'http://python.org/'),
#           ('Jinja2', 'http://jinja.pocoo.org/'),
#           ('You can modify those links in your config file', '#'),)

PLUGIN_PATHS = ['plugins']
PLUGINS = ['assets', 'gravatar', 'i18n_subsites']

I18N_SUBSITES = {
    'fr': {
        'SITENAME': 'LinkManager',
    }
}

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
