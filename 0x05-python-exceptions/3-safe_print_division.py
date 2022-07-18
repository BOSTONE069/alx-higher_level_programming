#!/usr/bin/python3

global div


def safe_print_division(a, b):
    global div
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div
