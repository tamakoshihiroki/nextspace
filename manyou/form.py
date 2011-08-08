# -*- coding: utf-8; -*-

"""
from functions
"""

def get_form_value( form, name, default_value ):
    'get form value'
    try:
        return form[ name ].value
    except KeyError:
        return default_value

