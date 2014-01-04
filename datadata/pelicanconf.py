#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'August Muench'
SITENAME = u'Data, Data, Everywhere'
SITESUBTITLE = u'All about managing, sharing, and archiving your data.'
SITEURL = 'http://localhost:8000'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%b %d, %Y'
DEFAULT_PAGINATION = False
DEFAULT_CATEGORY = ('Blog')

# explicit (workaround for fab build)
PATH = "content"
STATIC_PATHS = ['images', 'files', 'extra/robots.txt', 'extra/favicon.ico']
PLUGIN_PATH = '../src/pelican-plugins'
# OUTPUT_PATH = 'output'
# OUTPUT_PATH = '../html/datadata'

# menuitems
workshop = 'aas223'
MENUITEMS = [('Workshop', '/pages/{0}-workshop.html'.format(workshop)),
			 ('URLography', '/pages/urlography.html'),
             ]

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


# THEME
# THEME = "notmyidea"
# THEME = "pelican-octopress-theme"
THEME = "pelican-bootstrap3"
BOOTSTRAP_THEME = 'spacelab'
# BOOTSTRAP_THEME = 'readable'

# varia
# TWITTER_USERNAME = "augustmuench" 
# pelican-bootstrap3 circumvents the twitter button in fav of #addthis #poor
# ADDTHIS_PROFILE = 'ra-52c6d7b07d5342cd'
# GITHUB_USER = 'adsass'
# GITHUB_SKIP_FORK = True
# discussions
# DISQUS_SITENAME = 'datadata'

# Blogroll
LINKS = None
# LINKS = (('Seamless Astronomy', 'http://projects.iq.harvard.edu/seamlessastronomy'),)
# LINKS =  (('Pelican', 'http://getpelican.com/'),
#           ('Python.org', 'http://python.org/'),
#           ('Jinja2', 'http://jinja.pocoo.org/'),
#           ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = None
# (('Twitter', 'https://twitter.com/augustmuench'),
#           )

PLUGINS = ['sitemap']

# sitemap
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

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_CATEGORIES_ON_SIDEBAR = True

DISPLAY_PAGES_ON_MENU = False
DISPLAY_TAGS_ON_SIDEBAR = True

DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
RECENT_POST_COUNT = 3