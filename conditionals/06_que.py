#8. Password Strength Checker
#Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

passward = input("Please enter your passward: ")
pass_length = len(passward)
if pass_length < 6:
    pass_strength = "Weak"
elif pass_length <=10:
    pass_strength = "Medium"
else:
    pass_strength = "Strong"

print("Your passward strenght is : ", pass_strength)