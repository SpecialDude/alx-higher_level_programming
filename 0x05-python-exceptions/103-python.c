#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - print some basic info about Python lists
 *
 * @p: PyObject
 */
void print_python_list(PyObject *p)
{
    int long size, i;
    const char *type;
    PyListObject *list_object;

    setbuf(stdout, NULL);
    printf("[*] Python list info\n");


    if (strcmp(p->ob_type->tp_name, "list") != 0)
    {
        printf("  [ERROR] Invalid List Object");
        return;
    }

    list_object = (PyListObject *)p;
    size = list_object->ob_base.ob_size;

    printf("[*] Size of the Python List = %li\n", size);
    printf("[*] Allocated = %li\n", list_object->allocated);

    for (i = 0; i < size; i++)
    {
        type = list_object->ob_item[i]->ob_type->tp_name;

        printf("Element %li: %s\n", i, type);

        if (strcmp(type, "bytes") == 0)
            print_python_bytes(list_object->ob_item[i]);
        else if (strcmp(type, "float") == 0)
            print_python_float(list_object->ob_item[i]);
    }
}

/**
 * print_python_bytes - print some basic info about Python bytes
 *
 * @p: PyObject
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes_object;
    int long size, chunk, i;

    setbuf(stdout, NULL);
    printf("[.] bytes object info\n");

    if (strcmp(p->ob_type->tp_name, "bytes") != 0)
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    bytes_object = (PyBytesObject *)p;

    size = bytes_object->ob_base.ob_size;

    printf("  size: %li\n", size);
    printf("  trying string: %s\n", bytes_object->ob_sval);

    chunk = (size >= 10) ? 10 : size + 1;

    printf("  first %li bytes:", chunk);

    for (i = 0; i < chunk; i++)
        printf(" %02hhx", bytes_object->ob_sval[i]);
    printf("\n");

}

/**
 * print_python_float - print some basic info about Python float
 *
 * @p: PyObject
 */
void print_python_float(PyObject *p)
{
    PyFloatObject *float_object;
    double value;

    setbuf(stdout, NULL);
    printf("[.] float object info\n");


    if (strcmp(p->ob_type->tp_name, "float") != 0)
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    float_object = (PyFloatObject *)p;

    value = float_object->ob_fval;


    if (value - (int)value == 0)
        printf("  value: %#.1g\n", float_object->ob_fval);
    else
        printf("  value: %.16g\n", float_object->ob_fval);

}
