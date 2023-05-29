#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x integer members of a list.

    Args:
        my_list (list): The list to elements will be printed from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
