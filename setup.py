from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy as np

inc_dirs = [
    'khash/src/klib',
    'khash/src',
    np.get_include(),
]

lib_dirs = []
libs = []
def_macros = []

sources = [
    "khash/hashtable.pyx",
    "khash/hashtable.pxd"
]

lib_depends = [
    "khash/src/util.pxd",
    "khash/src/numpy_helper.h"
]

ext_modules = [
    Extension("khash.hashtable",
              sources,
              include_dirs=inc_dirs,
              depends=lib_depends
    )
]

cmdclass = {'build_ext': build_ext}

setup(
    name='khash',
    version='0.0.1',
    packages=[''],
    url='',
    license='',
    author='Carst Vaartjes',
    author_email='carstvaartjes@gmail.com',
    description='''A try out for a pandas-independent
        implementation of klib in Python''',
    # -----
    cmdclass=cmdclass,
    ext_modules=ext_modules,
    requires=[],
)

# Compiled with:
# cython.__version__ = '0.20.2'