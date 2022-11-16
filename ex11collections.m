% ex11: Collections, MATLAB

% "array" ("vector", "matrix"): holds values of same type
foo1 = [1, 2, 3];
foo2 = [97, 98, 99];
foo3 = foo1 .* foo2;  % Can do math - NOTE ".*"

% "cell array": holds values of different types
bar1 = {1, 'two', 3.33};
bar2 = {'abc', 'def'};  % Sometimes holds values of same type
bar2{1} = 'xyz';  % NOTE different index operators, "{...}"

% "struct": holds values in named fields
baz = struct('shape', 'round', ...
             'color', 'red', ...
             'count', 42);
baz.color = 'green';  % Ok to change value of field
baz.age = 99;  % Ok to add new fields
% baz.4 = 'four'  % ERROR: Can't use some values as field names!
