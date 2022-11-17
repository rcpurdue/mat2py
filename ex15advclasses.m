% ex15: Advanced Classes, MATLAB

classdef ex15advclasses < handle & ex6classes
    properties (Access = protected)
        baz  % Create protected property
    end

    methods
        function obj = ex15advclasses(foo, bar)
            obj = obj@ex6classes(foo, bar);  % Call super constructor
            obj.examine(foo, bar);
            obj.baz = length(foo);
        end

        function check(obj, baz)
            disp('Checking...');
            check@ex6classes(obj, baz);  % Call super method
        end
    end

    methods (Access = protected)
        function empty = examine(obj)
            empty = isempty(obj.foo) || isempty(obj.bar);
        end
    end

    methods (Static)
        function test()
            example = ex15advclasses([252 253], [105 106]);
            gcd = example.process();
            example.check(gcd);
        end
    end
end

