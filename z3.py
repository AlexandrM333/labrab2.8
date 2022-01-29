#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def multiplication():
    sum = 1
    while True:
        num = int(input("Ведите число: "))
        if num != 0:
            sum *= num
            print(sum)
        else:
            return False


if __name__ == '__main__':
    multiplication()