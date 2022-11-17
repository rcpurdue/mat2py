% ex13: Slicing, MATLAB

foo = [11 22 33 44];

% Slicing makes copies
bar = foo(2:3);  % bar=[22 33]
bar(1) = 0;  % foo unchanged

baz = foo(2:end);  %#ok, Slice to end
baz = foo(end);  %#ok, Last value: "end means last one"
baz = foo(end-1); % Backwards indexing

disp([foo bar baz]);

foo = [1 2 3; 4 5 6];

% Colon alone, "all"
bar = foo(:, 2);  %#ok,  2 5
bar = foo(1, :);  %#ok,  1 2 3
bar = foo(:);  %  1x6: 1 2 3 4 5 6

% Partial indexes
baz = foo(1);  %  1

disp([foo bar baz]);
