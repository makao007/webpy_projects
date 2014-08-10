#!/usr/bin/env python
# coding: utf-8

import os
import sys

def find_root (n):
    path = os.path.abspath(__file__)
    for i in range(n):
        path = os.path.dirname(path)
    return path

root = find_root (3)
if root not in sys.path:
    sys.path.append (root)
    
if __name__ == "__main__":
    print find_root(3)

