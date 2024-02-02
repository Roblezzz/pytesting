# Define a function that returns a number if it is positive or zero
def positve(number):
    if number >= 0:
        return number
    
# Call the positve function with 0 as argument and print the result
print(positve(0))

# Define a list with both negative and positive numbers
list1 = [1,-234,-2,23,345,56,3,-26,-7,10,15,30]

# Use the filter function to create a new list with only the positive numbers from list1
# Use the positve function as the filter condition
list2 = list(filter(positve, list1))

# Use the filter function to create another list with only the negative numbers from list1
# Use a lambda expression as the filter condition
list3 = list(filter(lambda number: number <= 0, list1))

# Print the three lists and their descriptions
print("{} is a list with both negative and positive numbers".format(list1))
print("{} is a list with positive numbers".format(list2))
print("{} is a list with negative numbers".format(list3))
