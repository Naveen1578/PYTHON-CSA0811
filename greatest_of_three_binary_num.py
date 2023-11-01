def greatest_of_three_binary_numbers(a, b, c):
    decimal_a = int(a, 2)
    decimal_b = int(b, 2)
    decimal_c = int(c, 2)
    return bin(max(decimal_a, decimal_b, decimal_c))[2:]

a = "1010"
b = "1101"
c = "1001"
print(greatest_of_three_binary_numbers(a, b, c))
