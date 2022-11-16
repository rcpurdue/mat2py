% ex12: Advanced Arrays, MATLAB

% Commas
foo = [1 2 3 4];
bar = [1, 2, 3, 4];  % NOTE commas optional

% Autofill
foo = zeros(10);  % [0 0 0 0 0 0 0 ...]
bar = ones(20);  % [1 1 1 1 1 1 1 ...]
baz = 1:5;  % [1 2 3 4 5]  NOTE values up to five

% Multidimensional
foo = [1 2 3; 4 5 6];  % NOTE semicolon
bar = size(foo);  % call function size(), bar=[2, 3]
baz = ndims(foo);  % call funciont ndims(), baz=2

% Concatenation
foo = [[1 2] [3 4]];  % Concatenates, foo=[1 2 3 4]
bar = [[1 2], [3 4]];  % Same as above
baz = [[1 2]; [3 4]];  % Creates 2x2
