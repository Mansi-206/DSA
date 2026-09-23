#8. Count the digits of a number

num = int(input("Enter any digit number:"))
count = 0

while num > 0:
    num = num // 10
    count += 1

print("Number of digits:", count)
