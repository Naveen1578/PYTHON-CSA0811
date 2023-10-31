a = int(input("Enter the starting number: "))
b = int(input("Enter the ending number: "))

for x in range(a, b + 1):
    if x > 1:
        is_prime = True
        for i in range(2, x):
            if (x % i) == 0:
                is_prime = False
                break
        if is_prime:
            print(x)
