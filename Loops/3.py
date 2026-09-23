#5 Print the multiplication table of a number

num = int(input("Enter any number:"))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
