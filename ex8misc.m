% ex8: Misc., MATLAB

foo = 1;      % Boolean value (alt: "true")
bar = [];     % Empty value
baz = 'abc';  % Character array (alt: "abc", string)

% Exception handling
try

    % Expressions
    if foo || (isempty(bar) && strcmp(baz, 'abc'))   % alt: baz == "abc"
        disp('Yep');
    else
        disp('Nope');
    end

    % Multiple return values
    [foo, bar] = meshgrid([1 2], [1 2 3]);
    foo = meshgrid([1 2], [1 2 3]);  % only 1st
    [~, foo] = meshgrid([1 2], [1 2 3]);  % only 2nd

catch ME

    % Formatted output
    fprintf('Error: %s\n', ME.identifier);
end
