num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
while num1 <= 0 or num2 <= 0 or num3 <= 0:
    print("Please enter positive numbers.")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
total = 0

for i in range(3):
    total += num1
    if i == 1:
        for j in range(1):
            total += num2
            if j == 0:
                for k in range(1):
                    total += num3

print(f"The sum of {num1}, {num2}, and {num3} is: {total}")
