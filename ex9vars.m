% ex9: Variables, MATLAB

% Single value
foo = 1;
bar = a;  %#ok Copy value
bar = 99;

disp([foo bar]);  % 1 99

 % Values in container (array)
foo = [1, 2 ,3];
bar = foo;     % Copy array
bar(1) = 99;

disp([foo bar]);   % [1 2 3]  [99 2 3]
