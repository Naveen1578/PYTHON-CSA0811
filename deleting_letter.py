def delchar(s, c):
    if len(c) != 1:
        return s
    else:
        return s.replace(c, '')

s = "Hello world"
c = "l"
print("String after the character is removed:", delchar(s, c))
