# -*- coding: utf-8 -*-
AUTHOR = u'Marcel Hellkamp'
SITENAME = u"bottlepy-dev"
SITESUBTITLE = u"Techtalk and stuff."
SITEURL = 'http://blog.bottlepy.org'
TIMEZONE = "Europe/Berlin"
THEME = 'bottle-theme'
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_ORPHANS = 3
DEFAULT_PAGINATION = 10
DEFAULT_DATE = (2012, 03, 02, 14, 01, 01)

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
PAGE_LANG_URL = 'pages/{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}.html'

GITHUB_URL = 'http://github.com/bottlepy/bottle'
#DISQUS_SITENAME = "bottlepy"
#TWITTER_USERNAME = "bottlepy"

MENUITEMS = (('Home','/'),)

LINKS = (('Docs','http://bottlepy.org/'),)

SOCIAL = (('twitter', 'http://twitter.com/bottlepy'),
          ('github', 'http://github.com/defnull'),)

# global metadata to all the contents
#DEFAULT_METADATA = (('yeah', 'it is'),)

# static paths will be copied under the same name
STATIC_PATHS = ["static", ]

# A list of files to copy from the source to the destination
EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    'static/favicon.ico': {'path': 'favicon.ico'},
}
