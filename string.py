chai = '0123456789'
print(chai[0:9]) # 9 include nahi hog
print(chai[1:10:2]) # 2 lihka to 1 number ki hoping hoti hai 
print(chai[0:10:3]) # 3 likha to 2 number ki hoping hogi means value aayegi [0369] last jo 10 likha hia wo inclusive nahi hota
#String are immutable

chai = "Karan, Hinal, Rathod, Sheetal, Yashwant"
print(chai.split(", ")) # string will convert onto list with any parametrs
print(chai.count("a"))
a = "masala chai"
print(a.replace("chai", "papad"))
# Place holders
first_name = 'Karan'
second_name = 'Rathod'
full_name = 'My name is {} and my surname is {}.'
print(full_name.format(first_name, second_name))
lists = ['karan', "hello", "nuifutfdc", "jgdcg"]
stringss = " ".join(lists) # according to our parameter like (spaces, comas, etc)
print(stringss)
#row string
n_rows = "karan\nrathod"
r_rows = r"rathod\nkaran"
print("normal string is{", n_rows, "}and row string is", r_rows)