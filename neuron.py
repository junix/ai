#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import math

and_train_data = [
    (np.array([1., 1., 1.]), 0.),
    (np.array([1., 0., 1.]), -1.),
    (np.array([0, 1., 1.]), -1.),
    (np.array([0., 0., 1.]), -2.),
]


def inputs(xs):
    while True:
        for xy in xs:
            yield xy


small_step = 1e-10


def small_enough(arr):
    for v in arr:
        if v < -small_step or v > small_step:
            return False
    return True


learning_rate = 0.1


def train(data):
    count = 0
    c = 0
    w = 0
    for (X, y) in inputs(data):
        c += 1
        y0 = np.dot(X, w)
        dw = (y - y0) * learning_rate * X
        w += dw
        count = 0 if not small_enough(dw) else count + 1
        if count > 10:
            print('count={count}, args={args}'.format(count=c, args=w))
            return w

if __name__ == '__main__':
    train(and_train_data)
