#include <Python.h>
#include <stdio.h>
#include <string.h>
#include <float.h>
#include <sys/types.h>
#include <python3.4/Python.h>
#include <python3.4/object.h>
#include <python3.4/listobject.h>
#include <python3.4/floatobject.h>
#include <python3.4/unicodeobject.h>
#define PY_SSIZE_T_C
#define PY_SSIZE_T_CLEAN

/**
 * print_python_string - implementation for print python bytes function
 * @p: The Pointer to the Python string
 *
 * Return: If p is not a valid PyBytesObject, print an error message
 */

