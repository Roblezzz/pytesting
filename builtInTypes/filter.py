
# This one is an example of how FILTER function works
my_numbers = list(range(1,11))
filter_list = list(filter(lambda module: module % 2 == 0, my_numbers))
print(filter_list)
