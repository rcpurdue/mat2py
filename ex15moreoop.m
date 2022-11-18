% ex15: More OOP, MATLAB

classdef ex15moreoop < ex6classes  % Inheritance
    properties (Access = protected)
        baz  % Create protected attribute
    end

    methods
        function obj = ex15moreoop(foo, bar)
            obj = obj@ex6classes(foo, bar);  % Call super constructor
            obj.describe();
        end

        function baz = process(obj)
            baz = process@ex6classes(obj);  % Call super method
            obj.baz = baz;
        end
    end

    methods (Access = protected)
        function describe(obj)  % Protected method
            fprintf('foo: %d, bar: %d\n', length(obj.foo), length(obj.bar))
        end
    end

    methods (Static)
        function example = test()  % Static method
            example = ex15moreoop([252 253], [105 106]);
            gcd = example.process();
            example.check(gcd);
        end
    end
end

% classdef Another...  % One class per file
% example = ex15moreoop.test()  % No add'l code in file
% example.qux = 3.14  % No new attributes
