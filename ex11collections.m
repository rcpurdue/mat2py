% ex11: Collections, MATLAB

% Same type: array (vector, matrix)
foo = [1, 2, 3];
bar = [97, 98, 99];
baz = foo .* bar;  %#ok, Can do math, note .*

% Diff types: cell array
foo = {1, 'two', 3.33};
bar = {'abc', 'def'};  % Can do same type
bar{1} = 'xyz';  % Note diff brackets

% Named fields: struct
baz = struct('shape', 'round', ...
             'color', 'red', ...
             'count', 42);
baz.age = 99;  % New field
% baz.4 = 'four'  % Restricted field names

print([foo bar baz])
