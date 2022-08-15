"""
Write a recursive Python program to calculate the value of 'a' to the power 'b'
Test Data :
(power(3,4) -> 81
"""

## BASE CASES
# B == 0 (return 1)
# A == 0 (return 0)
# B == 1 (return a)

def power(a,b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a * power(a, b-1)

print(power(3,4))