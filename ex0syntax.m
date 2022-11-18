% ex0: Syntax, MATLAB
% Ref: https://en.wikipedia.org/wiki/Euclidean_algorithm

foo = 252;
bar = 105;

while foo ~= bar

    if foo > bar
        foo = foo - bar;
    else
        bar = bar - foo;
    end
end

disp(foo);
