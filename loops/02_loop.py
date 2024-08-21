n = int(input("Enter Yor range: "))
sum_even = 0
for num in range(1, n+1):
    if num%2==0:
        sum_even += num
print("sums of even number till",n,"is: ",sum_even)