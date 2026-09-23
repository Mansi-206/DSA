#7. Reverse a number using a loop

num = int(input("ENter any number do youwant to reverse:"))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse:", reverse)
