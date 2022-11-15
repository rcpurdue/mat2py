% ex6: Classes, MATLAB

classdef ex6classes < handle
    properties (Constant)
        TWENTY_ONE = 21
    end

    properties
        a
        b
    end

    methods
        function obj = ex6classes(a, b)
            obj.a = a;
            obj.b = b;
        end

        function c = run(obj)
            c = gcd(obj.a, obj.b);
        end

        function check(obj, c)

            if c(1) == obj.TWENTY_ONE
                disp('Twenty-one!');
            end
        end
    end
end
