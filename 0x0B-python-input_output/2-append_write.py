#!/usr/bin/python3
"""
This module contains the function append_write.
"""
def append_write(filename="", text=""):
    """
    Appends to a file and returns the number of characters written.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
