def my_function(x):
    if x == 0:
        return float('inf') # Or handle it in a more suitable way for your application
    else:
        return 1 / x

print(my_function(0))