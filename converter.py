print("Welcome to the temperature converter")
temperature = float(input("Type the temperature:"))
type_temp = input("Type (F) for Fahrenheit to Celcius and (C) for Celcius to Fahrenheit: ").upper()

if type_temp == "C":
    c_formula = ((temperature * 9) /5) + 32
    print(c_formula)
elif type_temp == "F":
    f_formula = ((temperature - 32) * 5) / 9
    print(f_formula)
else: print("invalid input") 