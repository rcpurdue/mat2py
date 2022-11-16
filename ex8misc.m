% ex8: Misc., MATLAB

foo = 1;      % Boolean value (alt: "true")
bar = [];     % Empty value
baz = 'abc';  % Character array

% Exception handling
try

    % Expressions
    if foo || (isempty(bar) && strcmp(baz, 'abc'))   % alt: baz == "abc"
        disp('Ok');
    else
        disp('Nope');
    end

catch ME

    % Formatted output
    fprintf('Error: %s\n', ME.identifier);
end
