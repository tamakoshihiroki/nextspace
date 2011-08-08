# -*- coding: utf-8; -*-

"""
tategaki functions
"""

def tategaki_replace( string ):
    """
    Replace horizontal letters to vertical letters
    """
    string = string.replace( u'[', u'∧' )
    string = string.replace( u']', u'∨' )
    string = string.replace( u'(', u'∧' )
    string = string.replace( u')', u'∨' )
    string = string.replace( u'（', u'∧' )
    string = string.replace( u'）', u'∨' )
    string = string.replace( u'/', u'／' )
    string = string.replace( u'<', u'∧' )
    string = string.replace( u'>', u'∨' )
    return string

def tategaki( name, uta, column, row ):
    """
    Returns tategaki text from uta
    """
    name = tategaki_replace( name )
    uta  = tategaki_replace( uta )
    name_splitted = []
    i = 0
    while True:
        splitted = name[ i : i + row ]
        if splitted:
            splitted = splitted.replace( u' ', u'　' )
            line = []
            for char in range( row ):
                try:
                    line.append( splitted[ char ] )
                except IndexError:
                    line.append( u'　' )
            name_splitted.append( line )
            i += row
        else:
            break
    uta_splitted = []
    i = 0
    while True:
        splitted = uta[ i : i + row ]
        if splitted:
            if ' ' == splitted[ 0 ]:
                i += 1
                splitted = uta[ i : i + row ]
            splitted = splitted.replace( u' ', u'　' )
            line = []
            for char in range( row ):
                try:
                    line.append( splitted[ char ] )
                except IndexError:
                    line.append( u'　' )
            uta_splitted.append( line )
            i += row
        else:
            break
    name_splitted.extend( uta_splitted )
    while True:
        if 0 == len( name_splitted ) % column:
            break
        else:
            name_splitted.append( [ u'　' for _ in range( row ) ] )
    body_splitted = []
    i = 0
    while True:
        splitted = name_splitted[ i : i + column ]
        if splitted:
            splitted.reverse()
            splitted = apply( zip, splitted )
            body_splitted.append( splitted )
            i += column
        else:
            break
    body = '\n\n'.join( [ '\n'.join( [ ' '.join( letters )
                                     for letters in page ] )
                        for page in body_splitted ] )
    return body
