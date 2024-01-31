# Define a function that implements the fizzbuzz algorithm
def fizzbuzz():
    # Create an empty list
    my_list = []
    
    # Use a for loop to iterate over the numbers from 1 to 100
    for i in range(1, 101):
        
        # If the number is divisible by both 3 and 5, append "FizzBuzz" to the list
        if i % 3 == 0 and i % 5 == 0:
            my_list.append("FizzBuzz")

        # If the number is divisible by only 3, append "Fizz" to the list
        elif i % 3 == 0:
            my_list.append("Fizz")

        # If the number is divisible by only 5, append "Buzz" to the list
        elif i % 5 == 0:
            my_list.append("Buzz")
        # Otherwise, append the number itself to the list
        else: my_list.append(i)
        
    # Return the list
    return my_list

# Call the fizzbuzz function and print the result
print(fizzbuzz())
