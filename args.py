def sum_numbers(*args):
    return sum(args)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
print("Sum of numbers:", sum_numbers(*numbers))