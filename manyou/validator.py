# -*- coding: utf-8; -*-

"""
validator functions
"""

import re

usernameRE = re.compile(r"^[^ \t\n\r@<>()]+$", re.I )
domainRE   = re.compile(r"^[a-z0-9][a-z0-9\.\-_]*\.[a-z]+$", re.I )

def validate_mail_address( mail_address ):
    if not mail_address:
        return False
    mail_address = mail_address.strip()
    splitted     = mail_address.split( '@', 1 )
    try:
        username, domain = splitted
    except ValueError:
        return False
    if not usernameRE.search( username ):
        return False
    if not domainRE.search( domain ):
        return False
    return True
