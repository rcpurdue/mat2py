# ex15: More OOP, Python

from ex6classes import Example6


class Example15(Example6):  # Inheritance

    def __init__(self, foo, bar):
        super().__init__(foo, bar)  # Call super constructor
        self._describe()
        self._baz = None  # Protected attribute

    def process(self):
        self._baz = super().process()  # Call super method
        return self._baz

    def _describe(self):  # "Protected" method
        print(f'foo: {len(self.foo)}, bar: {len(self.bar)}')

    @staticmethod  # Static method
    def test():
        example = Example15([252, 253], [105, 106])
        gcd = example.process()
        example.check(gcd)
        return example


class Another():  # Mult classes in same file

    def __init__(self):
        print('Hi')


if __name__ == "__main__":  # Add'l code in same file
    example = Example15.test()
    example.qux = 3.14  # Create a new attribute
    print(example.__dict__)
    Another()
