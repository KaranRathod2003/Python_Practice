# Conditional statements

print("\\**  Conditional Statements  **\\")


# 1. Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).
age = int(input("Enter your age: "))
if age<=13:
    # or less than 13 -> (age < 13)
    print("Childern")
elif 13<=age<=19:
    # or less than 20 -> (age < 20)
    print("Teenager")
elif 20<=age<=59:
    # or less than 60 -> (age < 60)
    print("Adult")
else:
    print("Senior")





