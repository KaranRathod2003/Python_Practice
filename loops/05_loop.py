input_str = "teeter"
for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("First Non repeated character is ", char)
        break   #optimization