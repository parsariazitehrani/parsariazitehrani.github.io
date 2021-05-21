#!/usr/bin/python3
# -*- coding: utf-8 -*- #

AUTHOR = 'پارسا'
SITENAME = 'روباه قرمز'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tehran'

DEFAULT_LANG = 'fa'

THEME = 'theme/attila'
SITESUBTITLE = 'وبلاگ شخصی پارسا ریاضی تهرانی'
DISPLAY_PAGES_ON_MENU = True

# Plugins
# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ["pelican_persian_date"]

# Persian Date Plugin
DATE_FORMATS = {
    'fa': '%A %d %B %Y'
}

# Attila theme configuration
HEADER_COVER = 'theme/images/header_cover.jpg'
COLOR_SCHEME_CSS = 'monokai.css'
AUTHORS_BIO = {
  "parsa": {
    "name": "پارسا",
    "cover": "https://arulrajnet.github.io/attila-demo/assets/images/avatar.png",
    "image": "https://arulrajnet.github.io/attila-demo/assets/images/avatar.png",
    "website": "https://parsariazitehrani.github.io",
    "location": "مشهد، ایران",
    "bio": "من پارسا ریاضی تهرانی هستم. علاقمند به علم و ساختن چیزهای جدید"
  }
}


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
