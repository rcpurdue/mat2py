# ex6: Classes, Python

import numpy as np


class ex6classes(object):
    TWENTY_ONE = 21

    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar

    def run(self):
        return np.gcd(self.foo, self.bar)

    def check(self, baz):

        if baz[0] == self.TWENTY_ONE:
            print('Twenty-one!')
