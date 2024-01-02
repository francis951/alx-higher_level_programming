#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p) {
    if (!PyUnicode_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid String Object\n");
        return;
    }

    printf("[.] string object info\n");
    printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object");
    printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
    printf("  value: %ls\n", PyUnicode_AsWideCharString(p, NULL));
}

int main(void) {
    wchar_t *str = L"The spoon does not exist";
    PyObject *py_str = PyUnicode_DecodeW(str, wcslen(str), "utf-32", "strict");

    print_python_string(py_str);

    Py_DECREF(py_str);

    return 0;
}

