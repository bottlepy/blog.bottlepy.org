# -*- coding: utf-8 -*-
AUTHOR = u'Marcel Hellkamp'
SITENAME = u"bottlepy-dev"
SITESUBTITLE = u"Techtalk and stuff."
SITEURL = 'http://blog.bottlepy.org'
TIMEZONE = "Europe/Berlin"
THEME = 'bottle-theme'
ARTICLE_PERMALINK_STRUCTURE = '/%Y/%(category)s/'
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_ORPHANS = 3
DEFAULT_PAGINATION = 5
DEFAULT_DATE = (2012, 03, 02, 14, 01, 01)

GITHUB_URL = 'http://github.com/defnull/bottle'
#DISQUS_SITENAME = "bottlepy-blog"
TWITTER_USERNAME = "bottlepy"

#MENUITEMS = (('Docs','http://bottlepy.org/'),)

LINKS = (('Docs','http://bottlepy.org/'),)

SOCIAL = (('twitter', 'http://twitter.com/ametaireau'),
          ('lastfm', 'http://lastfm.com/user/akounet'),
          ('github', 'http://github.com/ametaireau'),)

# global metadata to all the contents
DEFAULT_METADATA = (('yeah', 'it is'),)

# static paths will be copied under the same name
STATIC_PATHS = ["static", ]

# A list of files to copy from the source to the destination
FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)

