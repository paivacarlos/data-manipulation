def check_pair(value):
    if value % 2 == 0:
        return True
    else:
        return False

my_list = [1, 2, 3, 4, 5 ,6 ,7 ,8 ,9, 10]

result = list(filter(check_pair, my_list))
print(result)

find_number_7 = list(filter(lambda num: num == 7, my_list))
print(find_number_7)