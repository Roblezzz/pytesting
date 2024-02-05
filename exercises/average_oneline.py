#List of numbers to work with
numbers = [1, 2, 3, 4, 5]

#Function to sum the numbers in the list and calculate the average
def sum_and_average(n):
#Returns a dictionary made of a list with lists, where the values of the keys are the math operations to sum and calculate the average
   return dict([['sum',sum(n)], ['average',sum(n) / len(n)]]) 

#Calling the function using the list as the argument and storing it in a variable 
result = sum_and_average(numbers)

#Printing the results by calling the keys of the dictionary
print("sum:", result["sum"])
print("average:", result["average"])