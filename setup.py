''' setup.py '''
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

sourcefiles = ['hello_caller.pyx']
ext_modules = [Extension("hello_caller", 
                          sourcefiles )]

setup(
  name = 'Hello world',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)
