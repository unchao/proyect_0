import sys

try:
    x=int(input("x: "))
    y=int(input("y: "))

except ValueError:
    print("Error: se ingreso una palabra.")
    sys.exit(1)

try:
    resultado= x / y
except ZeroDivisionError:
    print("Error: no se puede dividir por 0.")
    sys.exit(1)

print(f"{x} / {y} = {resultado}")
