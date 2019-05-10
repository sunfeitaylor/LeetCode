# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import functools


# 递归改进版
def fibMemo(n, memo={}):
    if n <= 1:
        return n
    if memo.get(n):
        return memo[n]
    result = fibMemo(n-1, memo) + fibMemo(n-2, memo)
    memo[n] = result
    return result


print('fib with memory', str(40), 'is', fibMemo(40))


# 尾递归
def fibTail(n):

    def fibProcess(n, prePreVal, preVal, begin):
        if n == begin:
            return preVal + prePreVal
        else:
            begin += 1
            return fibProcess(n, preVal, prePreVal + preVal, begin)

    if n <= 1:
        return n
    else:
        return fibProcess(n, 0, 1, 2)


print('fib with begin', str(40), 'is', fibTail(40))


# 矩阵快速幂次解法
def fibMatrixType(n):
    if n <= 1:
        return n
    A = np.array([[1, 1],
                  [1, 0]])
    result = [[1],
              [0]]
    n = n - 1
    while n > 0:
        if n % 2:
            result = A.dot(result)
        n = n // 2
        A = A.dot(A)
    return result[0, 0]


print('fib with matrix', str(40), 'is', fibMatrixType(40))


# 换个好懂的矩阵求解法
def matrixPower(n, A_init):
    if n <= 1:
        return A_init
    A_xiafen = matrixPower(n//2, A_init)
    A = np.dot(A_xiafen, A_xiafen)
    if n % 2:
        return np.dot(A_init, A)
    else:
        return A


def fibBetterMatrixType(n):
    A = np.array([[1, 1],
                  [1, 0]])
    result = [[1],
              [0]]
    A = matrixPower(n - 1, A)
    result = np.dot(A, result)
    return result[0, 0]


print('fib with matrix', str(40), 'is', fibBetterMatrixType(40))


@functools.lru_cache()
def fib_use_lru_cache(n):
    return n if n < 2 else fib_use_lru_cache(n-2) + fib_use_lru_cache(n-1)


print('fib using lru_cache', str(40), 'is', fib_use_lru_cache(40))
