number = int(input("Entyer your number: "))
factorial = 1
while number > 0:
    factorial = factorial * number
    number -= 1

print("Factorial is",factorial)