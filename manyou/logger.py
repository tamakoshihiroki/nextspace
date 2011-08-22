# -*- coding: utf-8; -*-

"""
logging functions
"""

import logging

LOG_ERROR = 'log/error.log'

logging.basicConfig(
    filename = LOG_ERROR,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    level = logging.DEBUG )

def log( message ):
    'log message'
    logging.error( message )
