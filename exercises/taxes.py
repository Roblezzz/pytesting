# Ask the user to type their monthly revenue in euros as a float
revenue = float(input("Please type your monthly revenue in euros: €"))

# Define a function that calculates the monthly taxes based on the revenue
def tax_calculator(r):
    # Use conditional statements to check the revenue range
    # Return a string with the corresponding tax percentage
    if r <= 10000:
        return "your monthly taxes are the 5% of your revenue"
    elif r > 10000 and r <= 20000:
        return "your monthly taxes are the 15% of your revenue"
    elif r > 20000 and r <= 35000:
        return "your monthly taxes are the 20% of your revenue"
    elif r > 35000 and r <= 60000:
        return "your monthly taxes are the 30% of your revenue"
    elif r > 60000:
        return "your monthly taxes are the 45% of your revenue"

# Call the tax_calculator function with the revenue as argument
# Print the result
print(tax_calculator(revenue))
