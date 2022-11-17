# ex15: Advanced Classes, Python

from ex6classes import Example6


class Example15(object, Example6):

    def __init__(self, foo, bar):
        super().__init__(foo, bar)  # Call super constructor
        self._examine(foo, bar)
        self._baz = 3.14
        self._examine()  # Create protected attribute

    def check(self, baz):
        print('Checking...')
        super().check(baz)  # Call super method

    def _examine(self):
        return (not self.foo) or (not self.bar)

    @staticmethod
    def test():
        example = Example15([252, 253], [105, 106])
        gcd = example.process()
        example.check(gcd)
        return example


if __name__ == "__main__":
    ex1 = Example15.test()
    ex1.qux = 3.14  # Create a new attribute
