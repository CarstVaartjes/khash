from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    name='khash_test',
    version='0.0.1',
    packages=[''],
    url='',
    license='',
    author='Carst Vaartjes',
    author_email='carstvaartjes@gmail.com',
    description='A try out for a pandas-independent implementation of klib in Python'
)

inc_dirs = ['khash', 'khash/src/klib', 'khash/src']
lib_dirs = []
libs = []
def_macros = []
sources = ["./khash/hashtable.pyx"]

ext_modules = [
    Extension("hashtable", ["./khash/hashtable.pyx"])
]

setup(
  name = 'vf_api',
  cmdclass = {'build_ext': build_ext},
  include_dirs = inc_dirs,
  ext_modules = ext_modules, requires=[]
)
