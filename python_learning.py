#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def check_if_int(number_list):
    for i in number_list:
        if not isinstance(i, int):
            raise TypeError("TypeError: Unsupported type. Expected type is 'int'")

# 掛け算
def multiplication(a, b):
    check_if_int([a, b])
    return a * b

# 割り算
def division(a, b):
    check_if_int([a, b])
    if b == 0:
        raise ZeroDivisionError("ZeroDivisionError: division by zero")
    return a / b

# 足し算
def addition(a, b):
    check_if_int([a, b])
    return a + b

# 引き算
def subtraction(a, b):
    check_if_int([a, b])
    return a - b

def main():
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])

        result = multiplication(a, b)
        print("{a} x {b} = {result}".format(a=a, b=b, result=result))

        result = division(a, b)
        print("{a} / {b} = {result}".format(a=a, b=b, result=result))

    except Exception as e:
        print("\n[ERROR]\n" + str(e))
        sys.exit(1)
    
    else:
        print("\nNormal end.")
        sys.exit(0)


if __name__ == "__main__":
    main()