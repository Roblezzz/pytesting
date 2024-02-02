# This is an example of how MAP function works:
# The Map functions are used to mapping an existing function over other elements and objects

def multiply(num):
   return num * 2

my_numbers = list(range(1,11))
my_multiplied_numbers = list(map(multiply, my_numbers))
print(my_numbers,my_multiplied_numbers)
