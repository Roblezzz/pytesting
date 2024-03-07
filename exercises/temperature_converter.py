# Print a welcome message
print("Welcome to the temperature converter")

# Ask the user to type the temperature as a float
temperature = float(input("Type the temperature:"))

# Ask the user to type the type of conversion they want to do
# F for Fahrenheit to Celsius and C for Celsius to Fahrenheit
# Convert the input to uppercase
type_temp = input("Type (F) for Fahrenheit to Celcius and (C) for Celcius to Fahrenheit: ").upper()

# Define a function that converts Celsius to Fahrenheit
# Use the formula: F = (C * 9/5) + 32
def c_formula(c):
    f = ((c * 9) /5) + 32
    return f
    
# Define a function that converts Fahrenheit to Celsius
# Use the formula: C = (F - 32) * 5/9
def f_formula(f):
    c = ((f - 32) * 5) / 9
    return c

# Check the type of conversion the user wants to do
# If it is C, call the c_formula function with the temperature as argument
# If it is F, call the f_formula function with the temperature as argument
# If it is neither, print an error message
if type_temp == "C":
    print(c_formula(temperature))
elif type_temp == "F":
    print(f_formula(temperature))
else: print("Invalid input")
