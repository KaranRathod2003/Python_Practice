number  = int(input("Enter nunber: "))
# is_prime = True
if number  > 1:
    for i in range(2, number):
        if (number % i) == 0:
            # is_prime = False
            print(number, "is not prime number")
            break
print(number,"is prime number")