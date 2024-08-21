def sum_of_numbers(*args):
    print(args)
    # for i in args:
    #     print(i * 2)
    return sum(args)
print(sum_of_numbers(1, 2, 3, 8, 0, 8, 7))