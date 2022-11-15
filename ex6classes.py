# ex6: Classes, Python

import numpy as np


class ex6classes(object):
    TWENTY_ONE = 21

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def run(self):
        return np.gcd(self.a, self.b)

    def check(self, c):

        if c[0] == self.TWENTY_ONE:
            print('Twenty-one!')
