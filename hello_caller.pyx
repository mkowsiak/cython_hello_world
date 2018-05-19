''' hello_caller.pyx '''

cdef extern from "hello.c":
  void f(char *)

''' 
    take a look here for details about different Cython declarations

    http://notes-on-cython.readthedocs.io/en/latest/function_declarations.html
'''
cpdef hello_world(str):
  f(str)

