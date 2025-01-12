# ZeroDivisionError Bug in Python

This repository demonstrates a common Python error: the `ZeroDivisionError`. The `bug.py` file contains a function that can raise this error, while `bugSolution.py` provides a solution.

## Bug Description
The function `my_function` calculates the reciprocal of a number.  If the input is 0, it leads to division by zero, resulting in a `ZeroDivisionError`.

## Solution
The solution involves adding error handling to check for the zero input and gracefully handle the exception.