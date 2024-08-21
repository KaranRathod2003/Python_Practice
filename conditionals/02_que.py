# 2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = int(input("Enter Age: "))
# day = str(input("Enter Day: "))
day = "Wednesday"

price = 12 if age>=18 else 8

if day == "Wednesday":
    price -= 2
    # price = price - 2
print("Your Ticket will cost $", price)
# else:
#     print("original ticket price with discount")





