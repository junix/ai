#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import math

and_train_data = [
    (np.array([1., 1., 1.]), 1.),
    (np.array([1., 0., 1.]), -1.),
    (np.array([0, 1., 1.]), -1.),
    (np.array([0., 0., 1.]), 1.),
]


def inputs(xs):
    while True:
        for xy in xs:
            yield xy


small_step = 1e-10


def small_enough(u):
    return math.fabs(u) < small_step


learning_rate = 0.0000001


class Cell:
    def __init__(self, pre_cells=None):
        self.w = None
        self.ps = pre_cells
        if self.ps:
            for p in self.ps:
                p.ns = self
        self.ns = None
        self.X = None

    def eval(self, x):
        if self.ps:
            self.X = np.array([p.eval(x) for p in self.ps])
        self.X = x
        if self.w is None:
            self.w = np.zeros(len(self.X))
        return np.dot(self.X, self.w)

    def adjust(self, u):
        if self.ps:
            for p in self.ps:
                p.adjust(u)
        self.w += u * self.X

    def __repr__(self):
        return '{w}'.format(w=self.w)

    def train(self, data_set):
        count = 0
        for (X, y) in inputs(data_set):
            y0 = self.eval(X)
            u = (y - y0) * learning_rate
            if small_enough(u):
                count += 1
            else:
                print(u)
                count = 0
            self.adjust(u)
            if count > 10:
                return


if __name__ == '__main__':
    c0, c1 = Cell(), Cell()
    c2 = Cell(pre_cells=[c0, c1])
    c2.train(and_train_data)
    for c in (c0,c1,c2):
        print(c)
