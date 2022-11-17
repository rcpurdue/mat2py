# ex6: Classes, Python

import numpy as np


class ExampleSix(object):  # Name can diff from file name
    TWENTY_ONE = 21

    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar

    def process(self):
        return np.gcd(self.foo, self.bar)

    def check(self, baz):

        if baz[0] == self.TWENTY_ONE:
            print('Twenty-one!')


