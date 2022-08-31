#include <python3.9/Python.h>
#include <python3.9/object.h>
#include <python3.9/listobject.h>
#include <python3.9/bytesobject.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints information about a python list
 *
 * @p: Python Object (list)
 */
void print_python_list(PyObject *p)
{
    long int size;
    PyListObject *list;
    int i;
    const char *typename;

    list = (PyListObject *)p;
    size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %li\n", size);
    printf("[*] Allocated = %li\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        typename = (list->ob_item[i]->ob_type->tp_name);
        printf("Element %i: %s\n", i, typename);
        if (strcmp(typename, "bytes") == 0)
            print_python_bytes(list->ob_item[i]);
    }
}

/**
 * print_python_bytes - Print Information about Python bytes
 *
 * @p: Python Object (byte)
 */
void print_python_bytes(PyObject *p)
{
    long int size;
    char *t_str;
    int i = 0;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    PyBytes_AsStringAndSize(p, &t_str, &size);

    printf("  size: %li\n", size);
    printf("  trying string: %s\n", t_str);

    if (size < 10)
        printf("  first %li bytes:", size + 1);
    else
        printf("  first 10 bytes:");

    for (i = 0; i < size + 1 && i < 10; i++)
        printf(" %02hhx", t_str[i]);
    printf("\n");
}
