'''
Copyright 2026. Created in Zapopan, Mexico. All Rights Reserved.
'''

__author__ = 'Ricardo Samuel Mendoza Núñez <rsmn.development@gmail.com>'
__status__ = 'Development'
__date__ = '19-05-2026'
__last_update__ = '19-05-2026'


from django import template
from django.urls import translate_url
from django.utils.translation import get_language

register = template.Library()

@register.simple_tag(takes_context=True)
def get_translated_url(context, lang_code):
    path = context['request'].get_full_path()
    return translate_url(path, lang_code)
