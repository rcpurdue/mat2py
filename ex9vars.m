% ex9: Variables, MATLAB

% Single value
foo = 1;
 bar = a;     % Copies value to new variable
 bar = 99;

 disp(foo);   % "1"
 disp(bar);   % "99"

 % Values in a container (array)
 foo = [1, 2 ,3];
 bar = foo;     % Copies value into new variable
 bar(1) = 99;

 disp(foo);   % "1 2 3"
 disp(bar);   % "99 2 3"
