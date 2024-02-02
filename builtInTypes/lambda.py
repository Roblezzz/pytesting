# This is an example of how lambda functions works, the main objetive of the lambda functions is that can contain multiple arguments but only one expression over those arguments:
my_numbers = list(range(1,11))
my_lambda = list(map(lambda multi: multi * 2, my_numbers))
print(my_lambda)