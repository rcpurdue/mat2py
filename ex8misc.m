% ex8: Misc., MATLAB

foo = 1;      % Boolean value (alt: "true")
bar = [];     % Empty value
baz = 'abc';  % Character array

% Exception handling
try

    % Expressions
    if foo || (isempty(bar) && strcmp(baz, 'abc'))   % alt: baz == "abc"
        disp('Yep');
    else
        disp('Nope');
    end

    % Multiple return values
    [foo, bar] = log2(3.14);
    foo = log2(3.14);
    [~, foo] = log2(3.14);

catch ME

    % Formatted output
    fprintf('Error: %s\n', ME.identifier);
end
