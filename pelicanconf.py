#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Connor Monahan'
SITENAME = 'Connor\'s Technical Site'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'Misc'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('WashU Racing', 'http://sae.wustl.edu/'),
         ('Ratchet Rockers', 'http://ratchetrockers1706.org/'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/cmastudios'),
          ('LinkedIn', 'https://www.linkedin.com/in/connor-monahan-a23318146/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'pdfs']
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'

EXTRA_PATH_METADATA = {'images/favicon.ico': {'path': 'favicon.ico'},}

