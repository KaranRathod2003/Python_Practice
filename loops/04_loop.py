input_str = str(input("Enter a string: "))
reversed_str = ""
for char in input_str:
    reversed_str = char + reversed_str
    if input_str == reversed_str:
        print("Palindrome")
print("Reversed string for '", input_str, "'is", reversed_str)