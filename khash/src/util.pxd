from numpy cimport ndarray
cimport numpy as cnp
cimport cpython

cdef extern from "numpy_helper.h":
    inline void set_array_owndata(ndarray ao)
    inline void set_array_not_contiguous(ndarray ao)

    inline int is_integer_object(object)
    inline int is_float_object(object)
    inline int is_complex_object(object)
    inline int is_bool_object(object)
    inline int is_string_object(object)

    inline char *get_c_string(object)