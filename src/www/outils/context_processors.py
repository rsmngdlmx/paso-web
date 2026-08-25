# -*- coding: utf-8 -*-

'''
Copyright 2026. Created in Zapopan, Mexico. All Rights Reserved.
'''

__author__ = 'Ricardo Samuel Mendoza Núñez <rsmn.development@gmail.com>'
__status__ = 'Development'
__date__ = '11-05-2026'
__last_update__ = '10-06-2026'


_DOMAIN = 'ricardomendoza.dev'

from django.utils.translation import gettext as _
from datetime import datetime

def _get_page(url):
    page = url.replace('/', '')
    return 'bio' if page == '' else page

def _get_current_year():
    return datetime.today().strftime('%Y')

def shared(request):
    return {
        'lang': request.LANGUAGE_CODE,
        'skippy': _('Go to main content'),
        'domain': f'{_DOMAIN}',
        'web_url': f'https://www.{_DOMAIN}',
        'blog_url': f'https://blog.{_DOMAIN}',
        'chingu_url': 'https://chingu.mx/',
        'short_bio': _('Software Engineer with extensive experience in web '
                       'development as well as incorporating AI into the SDLC.'),
        'page': _get_page(request.path[3:]),
        'current_year': _get_current_year()
    }
