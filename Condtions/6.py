#6. Check whether a number is divisible by 5 and 11

num = int(input("Enter any number:"))

if num % 5 == 0 and num % 11 == 0:
    print("Number is divisible by 5 and 11")
else:
    print("Number is not divisible by 5 and 11")
