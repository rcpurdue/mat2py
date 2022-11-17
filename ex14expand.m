% ex14: Expanding Arrays, MATLAB

foo = [1, 2, 3];

% Append
foo(end+1) = 4;

% Auto expansion
foo(12) = 99;  % 1 2 3 4 0 0 0 0 0 0 0 99

disp(foo);
