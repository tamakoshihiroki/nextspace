# -*- coding: utf-8; -*-

"""
logging functions
"""

import logging

LOG_SAMPLE = 'log/error.log'

logging.basicConfig( filename = LOG_SAMPLE, level = logging.DEBUG )

def log( message ):
    'log message'
    logging.error( message )
