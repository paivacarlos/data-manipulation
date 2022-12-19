from functools import reduce

my_list = [10, 20, 30, 40]

def sum(first_value, second_value):
    return first_value + second_value

result = reduce(sum, my_list)
print(result)

#using lambda with reduce
max_find = lambda x,y: x if (x > y) else y
result_2 = reduce(max_find, my_list)
print(result_2)