#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "Invalid Python List\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List: %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "Invalid Python Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    Py_ssize_t max_display = size > 10 ? 10 : size;

    printf("[.] bytes object info\n");
    printf("size: %ld\n", size);
    printf("trying string: %s\n", PyBytes_AsString(p));

    printf("first %ld bytes: ", max_display);
    for (Py_ssize_t i = 0; i < max_display; i++) {
        printf("%02hhx", ((char *)PyBytes_AsString(p))[i]);
        if (i < max_display - 1) {
            printf(" ");
        }
    }
    printf("\n");
}
