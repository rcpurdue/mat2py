% ex8: Misc., MATLAB

a = 1;      % Boolean value (alt: "true")
b = [];     % Empty value
c = 'abc';  % Character array

% Exception handling
try

    % Expressions
    if a || (isempty(b) && strcmp(c, 'abc'))   % alt: c == "abc"
        disp('Ok');
    else
        disp('Nope');
    end

catch ME

    % Formatted output
    fprintf('Error: %s\n', ME.identifier);
end
