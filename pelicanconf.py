#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Robert McGibbon'
SITENAME = u"Robert's Notebook"
SITESUBTITLE = u"Computational Chemistry, Python, Politics, Policy"
SITEURL = ''

# Times and dates
DEFAULT_DATE_FORMAT = '%b %d, %Y'
TIMEZONE = 'US/Pacific'
DEFAULT_LANG = u'en'

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Title menu options
MENUITEMS = [('Archives', '/archives.html'),
             ('Home Page', 'http://rmcgibbo.appspot.com/')]
NEWEST_FIRST_ARCHIVES = False

# Github include settings
GITHUB_USER = 'rmcgibbo'
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# STATIC_OUT_DIR requires pelican 3.3
STATIC_OUT_DIR = ''
STATIC_PATHS = ['images', 'figures', 'downloads']
FILES_TO_COPY = [('favicon.png', 'favicon.png')]
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

# Theme and plugins
#  Theme requires http://github.com/duilio/pelican-octopress-theme/
#  Plugins require http://github.com/getpelican/pelican-plugins/
THEME = 'pelican-octopress-theme/'
PLUGIN_PATH = 'pelican-plugins/'
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal']

TWITTER_USER = 'rmcgibbo'
GOOGLE_PLUS_USER = 'rmcgibbo'
GOOGLE_PLUS_ONE = False
GOOGLE_PLUS_HIDDEN = True
FACEBOOK_LIKE = False
TWITTER_TWEET_BUTTON = True
TWITTER_LATEST_TWEETS = True
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_COUNT = 3
TWITTER_SHOW_REPLIES = 'false'
TWITTER_SHOW_FOLLOWER_COUNT = 'true'

# RSS/Atom feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom.xml'

# Search
SEARCH_BOX = True

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
