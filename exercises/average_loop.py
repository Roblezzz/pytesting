numbers = [1, 2, 3, 4, 5]

def sum_and_average(n):
    """Calculates the sum and average of a list of numbers using a for loop."""

    sum_of_numbers = 0  # Initialize the sum to 0
    count = 0  # Initialize a counter to track the number of elements

    for number in n:
        sum_of_numbers += number  # Add each number to the sum
        count += 1  # Increment the counter for each element

    average = sum_of_numbers / count  # Calculate the average after the loop

    results = {
        "sum": sum_of_numbers,
        "average": average
    }

    return results

result = sum_and_average(numbers)
print("sum:", result["sum"])
print("average:", result["average"])
