numbers = [1, 2, 3, 4, 5]
f_temperatures = [32, 50, 77, 86, 100]
mixed_list = [-3, 4, -1, 8, -2, 9]
chars = ['a', 'B', '1', 'C', '2', 'd']

def cube(x):
    return x ** 3

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def is_positive(x):
    return x > 0

def is_alpha(x):
    return x.isalpha()

cubes_using_map = list(map(cube, numbers))
print("Cubes using map and function:", cubes_using_map)

celsius_using_map = list(map(fahrenheit_to_celsius, f_temperatures))
print("Celsius using map and function:", celsius_using_map)

positive_numbers_using_filter = list(filter(is_positive, mixed_list))
print("Positive numbers using filter and function:", positive_numbers_using_filter)

alphabets_using_filter = list(filter(is_alpha, chars))
print("Alphabets using filter and function:", alphabets_using_filter)

cubes_using_lambda = list(map(lambda x: x ** 3, numbers))
print("Cubes using map and lambda:", cubes_using_lambda)

celsius_using_lambda = list(map(lambda f: (f - 32) * 5 / 9, f_temperatures))
print("Celsius using map and lambda:", celsius_using_lambda)

positive_numbers_using_lambda = list(filter(lambda x: x > 0, mixed_list))
print("Positive numbers using filter and lambda:", positive_numbers_using_lambda)

alphabets_using_lambda = list(filter(lambda x: x.isalpha(), chars))
print("Alphabets using filter and lambda:", alphabets_using_lambda)


cubes_using_comprehension = [x ** 3 for x in numbers]
print("Cubes using list comprehension:", cubes_using_comprehension)

celsius_using_comprehension = [(f - 32) * 5 / 9 for f in f_temperatures]
print("Celsius using list comprehension:", celsius_using_comprehension)

positive_numbers_using_comprehension = [x for x in mixed_list if x > 0]
print("Positive numbers using list comprehension:", positive_numbers_using_comprehension)

alphabets_using_comprehension = [x for x in chars if x.isalpha()]
print("Alphabets using list comprehension:", alphabets_using_comprehension)
