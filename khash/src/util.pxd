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
    inline int is_datetime64_object(object)
    inline int is_timedelta64_object(object)
    inline int assign_value_1d(ndarray, Py_ssize_t, object) except -1
    inline cnp.int64_t get_nat()
    inline object get_value_1d(ndarray, Py_ssize_t)
    inline int floatify(object, double*) except -1
    inline char *get_c_string(object)
    inline object char_to_string(char*)
