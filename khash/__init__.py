__author__ = 'carstvaartjes'

try:
    from . import hashtable
except Exception:  # pragma: no cover
    import sys
    e = sys.exc_info()[1]  # Py25 and Py3 current exception syntax conflict
    print e
    if 'No module named lib' in str(e):
        raise ImportError('C extensions not built: if you installed already '
                          'verify that you are not importing from the source '
                          'directory')
    else:
        raise