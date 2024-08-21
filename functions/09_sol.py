def even_num_generator_func(limit):
    for i in range(2, limit + 1, 2):
        # return i  does not save the state of function and by calling it simultaneously it will return same value i.e first value
        yield i


for num in even_num_generator_func(10):
    print(num)