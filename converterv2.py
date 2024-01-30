print("Welcome to the temperature converter")

temperature = float(input("Type the temperature:"))

type_temp = input("Type (F) for Fahrenheit to Celcius and (C) for Celcius to Fahrenheit: ").upper()

def c_formula(t):
    formula = ((t * 9) /5) + 32
    return formula
    
def f_formula(t):
    formula = ((t - 32) * 5) / 9
    return formula

if type_temp == "C":
    print(c_formula(temperature))
elif type_temp == "F":
    print(f_formula(temperature))
else: print("Invalid input")