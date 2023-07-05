#include <Python.h>

/**
 * print_python_string - function that prints Python strings.
 *
 * @p: ...
 *
 */

void print_python_string(PyObject *p)
{
    Py_ssize_t size;
    Py_UCS4 *unicode_str;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    size = PyUnicode_GET_LENGTH(p);
    unicode_str = PyUnicode_AsUCS4Copy(p);

    printf("  type: %s\n", Py_TYPE(p)->tp_name);
    printf("  length: %zd\n", size);
    printf("  value: %ls\n", unicode_str);

    PyMem_Free(unicode_str);
}
