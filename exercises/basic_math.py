a = 10
b = 3
def operaciones_matematicas(a,b):
    operaciones = [a+b, a-b, a*b, a/b, a%b]
    return operaciones
    
resultado = operaciones_matematicas(a,b)
print("Suma:", resultado[0])
print("Resta:", resultado[1])
print("Multiplicación:", resultado[2])
print("División:", resultado[3])
print("Residuo:", resultado[4])