#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mitch Lindgren'
SITENAME = u'mlindgren.ca'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Slate Star Codex', 'http://slatestarcodex.com'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

GITHUB_USER = 'mlindgren'
GITHUB_REPO_COUNT = 5
GITHUB_SKIP_FORK = False
GITHUB_SHOW_USER_LINK = False

X_MIN_READ = True

DEFAULT_PAGINATION = 10

ARTICLE_URL = 'entry/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'entry/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

THEME = '../mlindgren-pelican-theme'

SUMMARY_MAX_LENGTH = None

PLUGIN_PATHS = ["../pelican-plugins"]
PLUGINS = ["liquid_tags.img", "liquid_tags.video", "liquid_tags.youtube",
           "liquid_tags.include_code", "summary", "post_stats"]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
