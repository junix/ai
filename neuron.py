#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import math


def inputs():
    xys = [
        (np.array([1., 1., 1.]), 0.),
        (np.array([1., 0., 1.]), -1.),
        (np.array([0, 1., 1.]), -1.),
        (np.array([0., 0., 1.]), -2.),
    ]
    while True:
        for xy in xys:
            yield xy


small_step = 1e-10


def small_enough(arr):
    for v in arr:
        if v < -small_step or v > small_step:
            return False
    return True

if __name__ == '__main__':
    w = np.array([1., 1., 0.])
    count = 0
    c = 0
    learning_rate = 0.1
    for (X, y) in inputs():
        c += 1
        y0 = np.dot(X, w)
        dw = (y - y0) * learning_rate * X
        w = w + dw
        count = 0 if not small_enough(dw) else count + 1
        if count > 10:
            break

    print('count={count}, args={args}'.format(
        count=c,
        args=w))

