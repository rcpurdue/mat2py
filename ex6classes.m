% ex6: Classes, MATLAB

classdef ex6classes < handle
    properties (Constant)
        TWENTY_ONE = 21
    end

    properties
        foo
        bar
    end

    methods
        function obj = ex6classes(foo, bar)
            obj.foo = foo;
            obj.bar = bar;
        end

        function baz = run(obj)
            baz = gcd(obj.foo, obj.bar);
        end

        function check(obj, baz)

            if baz(1) == obj.TWENTY_ONE
                disp('Twenty-one!');
            end
        end
    end
end
