def find_gcd(a, b):
    """
    This function finds the GCD of two numbers.
    """
    gcd = 1
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd
def find_lcm(a, b):
    """
    This function finds the LCM of two numbers.
    """
    lcm = (a * b) // find_gcd(a, b)
    return lcm
first = int(input('Enter first number: '))
second = int(input('Enter second number: '))
print('GCD of', first, 'and', second, 'is', find_gcd(first, second))
print('LCM of', first, 'and', second, 'is', find_lcm(first, second))
