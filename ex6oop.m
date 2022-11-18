% ex6: OOP, MATLAB

classdef ex6oop < handle  % Class name must match file's name
    properties (Constant)
        TWENTY_ONE = 21
    end

    properties
        foo
        bar
    end

    methods
        function obj = ex6oop(foo, bar)
            obj.foo = foo;
            obj.bar = bar;
        end

        function baz = process(obj)
            baz = gcd(obj.foo, obj.bar);
        end

        function check(obj, baz)

            if baz(1) == obj.TWENTY_ONE
                disp('Twenty-one!');
            end
        end
    end
end
