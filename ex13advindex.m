% ex13: Advanced Indexing, MATLAB

foo = [11 22 33 44];

% Iterating over all values
for i=1:length(foo)   % length(foo)=4, 1:4=1, 2, 3, 4
    disp(foo(i))
end

% Slicing
bar = foo(2:3);  % bar=[22 33]

% Slicing to the last value
baz = foo(2:end);  % baz=[22 33, 44]

% Changing a value in a slice
baz(1) = 0;  % foo=[11 22 33 44], baz=[0 33 44]

% Get the last value: NOTE "end means last one"
bar = foo(end);  % bar=44

% Backwards indexing
bar = foo(end-1);  % end=4, end-2=2, bar="22"
