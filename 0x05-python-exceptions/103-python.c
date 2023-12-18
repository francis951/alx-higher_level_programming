#include <Python.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "[*] Python list info\n  [ERROR] Invalid List Object\n");
        return;
    }

    printf("[*] Python list info\n[*] Size of the Python List = %ld\n[*] Allocated = %ld\n",
           PyList_Size(p), ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < PyList_Size(p); ++i) {
        printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
        if (PyBytes_Check(PyList_GetItem(p, i))) {
            print_python_bytes(PyList_GetItem(p, i));
        } else if (PyFloat_Check(PyList_GetItem(p, i))) {
            print_python_float(PyList_GetItem(p, i));
        }
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("[.] bytes object info\n  size: %ld\n  trying string: %s\n  first 10 bytes: ",
           PyBytes_Size(p), PyBytes_AS_STRING(p));

    for (Py_ssize_t i = 0; i < PyBytes_Size(p) && i < 10; ++i) {
        printf("%02x ", (unsigned char)PyBytes_AS_STRING(p)[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        fprintf(stderr, "[.] float object info\n  [ERROR] Invalid Float Object\n");
        return;
    }

    printf("[.] float object info\n  value: %lf\n", PyFloat_AS_DOUBLE(p));
}
