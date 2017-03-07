#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'邵揮洲'
SITENAME = u'邵揮洲'
# leave SITEURL blank when developing
SITEURL = ''

PATH = 'content'

# avoid processing .html files
READERS = {'html': None}

# mix articles and static files in the same place
# @see https://github.com/getpelican/pelican/issues/1587
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['articles', 'extra', 'code']
EXTRA_PATH_METADATA = {'extra/robots.txt': {'path': 'robots.txt'},}

# modify TIMEZONE to your timezone
TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = u'zh'
LOCALE = 'zh_TW.UTF-8'

# @see http://docs.getpelican.com/en/latest/settings.html#basic-settings
# @see http://docs.getpelican.com/en/latest/settings.html#path-metadata
PATH_METADATA = 'articles/(?P<date>\d{4}/\d{2}/\d{2})/(?P<slug>[-a-zA-Z0-9.]*)%(?P<lang>[_a-zA-Z]{2,5})\.rst'

# @see http://docs.getpelican.com/en/latest/settings.html#url-settings
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

THEME = 'theme'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites',
           'edit_on_github',
           'embed_github_repository_file',
           'embed_picasaweb_image']

# custom setting for HTML meta info
META_KEYWORDS = '邵揮洲'
META_DESCRIPTION = '邵揮洲 教授 個人網站'

# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
  'en': {
    'SITENAME': 'Heiu-Jou Shaw',
    'AUTHOR': 'Heiu-Jou Shaw',
    'LOCALE': 'en_US.UTF-8',
    'META_KEYWORDS': 'Heiu-Jou Shaw',
    'META_DESCRIPTION': 'Professor Heiu-Jou Shaw Personal Website',
  },
}
I18N_UNTRANSLATED_ARTICLES = 'remove'

# generate only index.html and pages and articles. (no archives, tags, categories)
#DIRECT_TEMPLATES = ['index']
# use metadata attribute 'order' in page files for ordering
# @see http://docs.getpelican.com/en/latest/settings.html#url-settings
PAGE_ORDER_BY = 'order'

# CONTENT_DIR_URL is the setting for edit_on_github plugin
CONTENT_DIR_URL = u'https://github.com/USERNAME/REPO/tree/master/content'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# custom Jinja2 filter
def hidden_pages_get_page_with_slug_index(hidden_pages):
    for page in hidden_pages:
        if page.slug == "index":
            return page

# custom Jinja2 filter for localizing theme
def gettext(string, lang):
    if lang == "en":
        if string == "邵揮洲": return "Heiu-Jou Shaw"
        elif string == "教授": return "Professor"
        elif string == "系統及船舶機電工程學系": return "Systems and Naval Mechatronic Engineering"
        elif string == "成功大學": return "National Cheng Kung University"
        elif string == "http://w3.sname.ncku.edu.tw/main.php": return "http://w3.sname.ncku.edu.tw/main.php?site_id=2"
        elif string == "https://www.google.com/search?q=%E9%82%B5%E6%8F%AE%E6%B4%B2": return "https://www.google.com/search?q=Heiu-Jou+Shaw"
        #elif string == "": return ""
        else: return string
    elif lang == "zh":
        if string == "Archives": return "歸檔"
        elif string == "Categories": return "分類"
        elif string == "Category": return "分類"
        elif string == "Authors": return "作者"
        elif string == "Author": return "作者"
        elif string == "Tags": return "標籤"
        elif string == "Updated": return "更新"
        elif string == "Translation(s)": return "翻譯"
        elif string == "Edit on Github": return "在Github上編輯"
        else: return string
    else:
        return string

JINJA_FILTERS = {
    "hidden_pages_get_page_with_slug_index": hidden_pages_get_page_with_slug_index,
    "gettext": gettext,
}
