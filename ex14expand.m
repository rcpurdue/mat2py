% ex14: Expanding Arrays, MATLAB

foo = [1, 2, 3];

% Append values
foo(end+1) = 4;  % foo=[1 2 3 4]

% Automatic expansion
foo(12) = 99;  % foo=[1 2 3 4 0 0 0 0 0 0 0 99]
