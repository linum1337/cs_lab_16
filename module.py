#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def just_main():
    def outer_function():
        def inner_function(x):
            return x + 3

        return inner_function

    cnt = outer_function()
    k = int(input("Введите значение k: "))
    result = cnt(k)
    print("Результат:", result)
