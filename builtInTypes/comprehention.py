
# The following is an example of list comprehentions, that is used to create a list from another one:

list1 = list(range(1,6))
list2 = [number * 2 for number in list1]
print(list1, list2)