def fahrenheit(t):
    return ((float(9)/5) * t + 32)

def celcius(t):
    return (float((9)/5) * (t - 32))

temperatures = [0, 22.5, 40, 100]

#method 01
temp = list(map(fahrenheit, temperatures))
print(temp)

#method 02
for temp in map(fahrenheit,temperatures):
    print(temp)

temp_celcius = list(map(celcius, temperatures))
print(temp_celcius)

#lambda
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

result = list(map(lambda x,y:x+y, a, b))
print(result)


