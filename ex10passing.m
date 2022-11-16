% ex10: Passing, MATLAB

a = [1, 2, 3];
change(a);
disp(a);   % "1 2 3"

function change(b)
    b(1) = 99;
end
