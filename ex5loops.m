% ex5: Loops, MATLAB

foo = [252, 253, 254];
bar = [105, 106, 107];
baz = gcd(foo, bar);

for i=1:length(baz)  % 1:3 --> 1, 2, 3

    if baz(i) == 21
        disp('Twenty-one!')
    end
end
