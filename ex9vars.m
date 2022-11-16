% ex9: Variables, MATLAB

% Single value
 a = 1;
 b = a;     % Copies value to new variable
 b = 99;

 disp(a);   % "1"
 disp(b);   % "99"

 % Values in a container (array)
 a = [1, 2 ,3];
 b = a;     % Copies value into new variable
 b(1) = 99;

 disp(a);   % "1 2 3"
 disp(b);   % "99 2 3"
