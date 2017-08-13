#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ong Ming Yang, Chenyang Yuan'
SITENAME = 'MITSSS'
SITEURL = ''

PATH = 'content'
THEME = 'theme'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

PAGES = {'join': 'join.html'}
STATIC_PATHS = [
    'images',
    ]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Disable default page generation
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
TAG_SAVE_AS = ''
DIRECT_TEMPLATES = ('index',)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
