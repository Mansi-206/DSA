#4. Find the sum of numbers from 1 to n

n = int(input("Enter number:"))
sum = 0

for i in range(1, n + 1):
    sum += i

print("Sum:", sum)
