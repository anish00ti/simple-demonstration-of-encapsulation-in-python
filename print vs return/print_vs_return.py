# sum_function.py
# Simple example to show difference between print and return with operations

def add_and_print(x, y):
    # Prints sum inside function, but doesn't return anything
    print("Sum inside function (print):", x + y)

def add_and_return(x, y):
    # Returns sum so you can use it outside
    return x + y

# Call function that prints sum (no value returned)
add_and_print(5, 6)

# Call function that returns sum and save it to 'result'
result = add_and_return(5, 6)

# Now we can do more operations with 'result'
print("Sum outside function (return):", result)
print("Sum plus 10:", result + 10)
print("Sum times 2:", result * 2)
