% ex1: Functions, MATLAB

gcd = euclidgcd(252, 105);
disp(gcd);


function a = euclidgcd(a, b)
    % EUCLIDGCD Return greatest common divisor

    while a ~= b

        if a > b
            a = a - b;
        else
            b = b - a;
        end
    end
end
