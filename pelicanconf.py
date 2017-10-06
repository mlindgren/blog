#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mitch Lindgren'
SITENAME = u'mlindgren.ca'
SITEURL = 'http://blog.mlindgren.ca'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = True

DISQUS_SITENAME = 'mlindgrenca'
GOOGLE_ANALYTICS = 'UA-56108181-1'

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
('<img src="http://files.mlindgren.ca/images/github.png"/> Github', 'https://github.com/mlindgren'),
('<img src="http://files.mlindgren.ca/images/last.fm.png"/> last.fm', 'http://last.fm/user/lindgrenM'),
('<img src="http://files.mlindgren.ca/images/stackoverflow.png"> Stack Overflow', 'http://stackoverflow.com/users/108340/mitch-lindgren'),
('<img src="http://files.mlindgren.ca/images/yelp.png"/> Yelp', 'http://mlindgren.yelp.com'),
('<img src="http://files.mlindgren.ca/images/yt.png"/> YouTube', 'http://www.youtube.com/user/lindgrenMitch'),
)

GITHUB_USER = 'mlindgren'
GITHUB_REPO_COUNT = 5
GITHUB_SKIP_FORK = False
GITHUB_SHOW_USER_LINK = False

X_MIN_READ = True

DEFAULT_PAGINATION = 10

ARTICLE_URL = 'entry/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'entry/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_LANG_URL = 'entry/{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}/'
ARTICLE_LANG_SAVE_AS = 'entry/{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}/index.html'
PAGE_URL = 'blog/{slug}/'
PAGE_SAVE_AS = 'blog/{slug}/index.html'
ARCHIVES_SAVE_AS = 'blog/archives/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

THEME = '../mlindgren-pelican-theme'

SUMMARY_MAX_LENGTH = None

PLUGIN_PATHS = ["../pelican-plugins"]
PLUGINS = ["liquid_tags.img", "liquid_tags.video", "liquid_tags.youtube",
           "liquid_tags.include_code", "summary", "post_stats", "render_math"]

STATIC_PATHS = ['extra/favicon.ico', 'extra/favicon.png']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/favicon.png': {'path': 'favicon.png'}
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
