#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'August Muench'
SITENAME = u'Data, Data, Everywhere'
SITEURL = 'http://localhost:8000'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# explicit (workaround for fab build)
PATH = "content"

# Blogroll
LINKS = None
LINKS = (('Seamless Astronomy', 'http://projects.iq.harvard.edu/seamlessastronomy'),)
# LINKS =  (('Pelican', 'http://getpelican.com/'),
#           ('Python.org', 'http://python.org/'),
#           ('Jinja2', 'http://jinja.pocoo.org/'),
#           ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/augustmuench'),
          )

# GITHUB_USER = 'adsass'
# GITHUB_SKIP_FORK = True

STATIC_PATHS = ['images', 'files', 'extra/robots.txt', 'extra/favicon.ico']

DEFAULT_PAGINATION = False

# THEME
# THEME = "notmyidea"
THEME = "pelican-bootstrap3"

### content related ###

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = True
