% ex5: Loops, MATLAB

a = [252, 253, 254];
b = [105, 106, 107];
c = gcd(a, b);

for i=1:length(c)

    if c(i) == 21
        disp('Twenty-one!')
    end
end
