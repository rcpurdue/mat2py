% ex12: More Arrays, MATLAB

% Commas
foo = [1 2 3 4];  %#ok
bar = [1, 2, 3, 4];  %#ok, Commas optional

% Autofill
foo = zeros(10);  %#ok
bar = ones(20);  %#ok
baz = 1:5;  %#ok

% Multidimensional
foo = [1 2 3; 4 5 6];  % Note semicolon
bar = size(foo);  %#ok
baz = ndims(foo);

% Concatenation
foo = [[1 2] [3 4]];
bar = [[1 2]; [3 4]];

disp([foo bar baz])
