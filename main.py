#!/usr/bin/env python
# coding: utf-8
"""
@File    :   main.py
@Time    :   2022/05/27 22:23:38
@Author  :   https://github.com/hangsz
@Version :   0.1.0
@Contact :   zhenhang.sun@gmail.com
"""


import os 
import sys

def main() -> int:
    os.system('hugo')

    os.system('git add .')
    os.system('git commit -m "add"')
    os.system('git push origin main')

    return 0


if __name__ == "__main__":
    sys.exit(main())