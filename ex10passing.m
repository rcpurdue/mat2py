% ex10: Passing, MATLAB

foo = [1 2 3];
change(foo);
disp(foo);   % 1 2 3

function change(bar)
    bar(1) = 99;  %#ok
end
