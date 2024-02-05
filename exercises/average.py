# Create a list of numbers to work with
numbers = [1, 2, 3, 4, 5]

def sum_and_average(n):
   """Calculates the sum and average of a list of numbers.

   Args:
       n: A list of numbers.

   Returns:
       A dictionary containing the sum and average of the numbers.
       
		 There's an option to complete this example in one single line and is by returning a dictionary made of a list with lists inside, where the value of the keys are the logical operation:
   
   return dict([['sum',sum(n)], ['average',sum(n) / len(n)]]) 
   """

   # Calculate the sum of the numbers using the built-in sum() function
   add = sum(n)

   # Calculate the average by dividing the sum by the number of elements
   average = add / len(n)

   # Create a dictionary to store the results
   results = {
       "sum": add,  # Store the calculated sum
       "average": average  # Store the calculated average
   }

   return results  # Return the dictionary containing the results

# Call the sum_and_average function with the list of numbers
result = sum_and_average(numbers)

# Print the sum and average from the returned dictionary
print("sum:", result["sum"])
print("average:", result["average"])