# mat2py
Moving from MATLAB to Python

What's the difference between MATLAB an Python?
$2,250

Euclid's Algorithm

       Topic            MATLAB                    Python
ex0  Syntax      %, ;, ~, end, disp        #, \n, !, sp, :, print
ex1  Functions   function, (after), %      def, (before), """
ex2  Libraries   (built-in *toolbox)       import (library)
ex3  Arrays      (vector)                  (list --> numpy array)
ex4  Indexing    (), 1                     [], 0
ex5  Loops       :,length                  range, len
ex6  Classes     classdef, (const)         class, __init__()__
ex7  Plots
ex8  Misc        (&&/||, empty values, booleans, exceptions)

## Trivial Differences

### Comments (single & multiline)
### Spaces and Semicolons (instead of "end")
### Variables (and objects)
### Conditionals (and/or vs &&/||)
### Loops
### Classes & Objects
### Empty value (None, closest is [])
### Booleans
### Libraries
### Plots (pyplot)

## Key Differences

### Variables (value vs. reference, mutable, copying)
### Collections (arrays, lists, Numpy, cell arrays)
### Indexing & slicing (end, negative, in loops, slices of ndarrays)
### Reallocation
### Objects ("properties" vs "attributes", private/protected vs public and "_...")

## Not Covered

### List composition
### Code/module/library paths
### IDE (editor, "MATLAB GUI", debugger)
### Command Line
### Traditional naming conventions
### Building GUI applications, notebooks, libraries
### Compiled code
### Packaging & distribution
### Virtual environments

## Reference:
- [NumPy for MATLAB users](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html)
- [Python Buildin Functions](https://docs.python.org/3/library/functions.html)
- [MATLAB Builtin Functions](https://www.mathworks.com/help/matlab/referencelist.html?type=function&category=index&s_tid=CRUX_lftnav_function_index)
- [NumPy: the absolute basics for beginners](https://numpy.org/devdocs/user/absolute_beginners.html)
