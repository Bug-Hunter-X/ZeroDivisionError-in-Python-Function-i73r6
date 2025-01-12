def my_function(x):
    try:
        if x == 0:
            return 0
        else:
            return 1 / x
    except ZeroDivisionError:
        return float('inf') # Or handle it in a more application-specific way