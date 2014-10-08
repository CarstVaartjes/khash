#include "Python.h"
#include "numpy/arrayobject.h"
#include "numpy/arrayscalars.h"

#ifndef PANDAS_INLINE
  #if defined(__GNUC__)
    #define PANDAS_INLINE __inline__
  #elif defined(_MSC_VER)
    #define PANDAS_INLINE __inline
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define PANDAS_INLINE inline
  #else
    #define PANDAS_INLINE
  #endif
#endif

#define PANDAS_FLOAT 0
#define PANDAS_INT 1
#define PANDAS_BOOL 2
#define PANDAS_STRING 3
#define PANDAS_OBJECT 4
#define PANDAS_DATETIME 5

PANDAS_INLINE int
infer_type(PyObject* obj) {
  if (PyBool_Check(obj)) {
    return PANDAS_BOOL;
  }
  else if (PyArray_IsIntegerScalar(obj)) {
    return PANDAS_INT;
  }
  else if (PyArray_IsScalar(obj, Datetime)) {
    return PANDAS_DATETIME;
  }
  else if (PyFloat_Check(obj) || PyArray_IsScalar(obj, Floating)) {
    return PANDAS_FLOAT;
  }
  else if (PyString_Check(obj) || PyUnicode_Check(obj)) {
    return PANDAS_STRING;
  }
  else {
    return PANDAS_OBJECT;
  }
}

PANDAS_INLINE npy_datetime
get_datetime64_value(PyObject* obj) {
  return ((PyDatetimeScalarObject*) obj)->obval;

}

PANDAS_INLINE int
is_integer_object(PyObject* obj) {
  return (!PyBool_Check(obj)) && PyArray_IsIntegerScalar(obj);
//  return PyArray_IsIntegerScalar(obj);
}

PANDAS_INLINE int
is_float_object(PyObject* obj) {
  return (PyFloat_Check(obj) || PyArray_IsScalar(obj, Floating));
}
PANDAS_INLINE int
is_complex_object(PyObject* obj) {
  return (PyComplex_Check(obj) || PyArray_IsScalar(obj, ComplexFloating));
}

PANDAS_INLINE int
is_bool_object(PyObject* obj) {
  return (PyBool_Check(obj) || PyArray_IsScalar(obj, Bool));
}

PANDAS_INLINE int
is_string_object(PyObject* obj) {
  return (PyString_Check(obj) || PyUnicode_Check(obj));
}

PANDAS_INLINE char*
get_c_string(PyObject* obj) {
#if PY_VERSION_HEX >= 0x03000000
  PyObject* enc_str = PyUnicode_AsEncodedString(obj, "utf-8", "error");

  char *ret;
  ret = PyBytes_AS_STRING(enc_str);

  // TODO: memory leak here

  // Py_XDECREF(enc_str);
  return ret;
#else
  return PyString_AsString(obj);
#endif
}

void set_array_owndata(PyArrayObject *ao) {
    ao->flags |= NPY_OWNDATA;
}

void set_array_not_contiguous(PyArrayObject *ao) {
    ao->flags &= ~(NPY_C_CONTIGUOUS | NPY_F_CONTIGUOUS);
}


// PANDAS_INLINE PyObject*
// get_base_ndarray(PyObject* ap) {
//   // if (!ap || (NULL == ap)) {
//   //   Py_RETURN_NONE;
//   // }

//   while (!PyArray_CheckExact(ap)) {
//     ap = PyArray_BASE((PyArrayObject*) ap);
//     if (ap == Py_None) Py_RETURN_NONE;
//   }
//   // PyArray_BASE is a borrowed reference
//   if(ap) {
//     Py_INCREF(ap);
//   }
//   return ap;
// }
