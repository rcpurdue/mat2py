% ex1: Functions, MATLAB

gcd = euclidgcd(252, 105);
disp(gcd);


function foo = euclidgcd(foo, bar)
    % EUCLIDGCD Return greatest common divisor

    while foo ~= bar

        if foo > bar
            foo = foo - bar;
        else
            bar = bar - foo;
        end
    end
end
