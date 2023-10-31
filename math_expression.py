import re
test_str = "45 + 98-10"
print("The original string is : " + test_str)
res = sum(map(int, re.findall(r'[+-]?\d+', test_str))) 
print("The evaluated result is : " + str(res)) 
