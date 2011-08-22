# -*- coding: utf-8; -*-

"""
validator functions
"""

import re

USERNAME = re.compile(r"^[^ \t\n\r@<>()]+$", re.I )
DOMAIN   = re.compile(r"^[a-z0-9][a-z0-9\.\-_]*\.[a-z]+$", re.I )

def validate_mail_address( mail_address ):
    'validate the mail address'
    if not mail_address:
        return False
    mail_address = mail_address.strip()
    splitted     = mail_address.split( '@', 1 )
    try:
        username, domain = splitted
    except ValueError:
        return False
    if not USERNAME.search( username ):
        return False
    if not DOMAIN.search( domain ):
        return False
    return True
