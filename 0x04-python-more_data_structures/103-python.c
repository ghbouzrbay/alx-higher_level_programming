#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */


void print_python_list(PyObject *p)
{
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        const char *itemType = Py_TYPE(item)->tp_name;

        printf("Element %ld: %s\n", i, itemType);
    }
}


/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */


void print_python_bytes(PyObject *p)
{
    Py_ssize_t size;
    char *str;
    Py_ssize_t i;

    printf("[.] Bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  Size: %ld\n", size);
    printf("  trying string: %s\n", str);

    printf("  first %ld bytes: ", size + 1 > 10 ? 10 : size + 1);
    for (i = 0; i < size + 1 && i < 10; i++) {
        printf("%02hhx", str[i]);
        if (i + 1 < size + 1 && i + 1 < 10)
            printf(" ");
    }
    printf("\n");
}
