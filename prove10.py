def gcd(x,y):
    for n in range(min(x,y),1,-1):
        if x % n == 0 and y % n == 0:
            return n
    return 1

def lcm(x, y):
    # Add your code here
    return x * y // gcd(x,y)

print(gcd(74,66)) # 3
# print(gcd(12,24)) # 12
# print(gcd(12,18)) # 6 
# print(gcd(7,13))  # 1
# print(gcd(1,2))   # 1
# print(gcd(5,5))   # 5
print("===================")
# print(lcm(12,15)) # 60
# print(lcm(12,24)) # 24
# print(lcm(12,18)) # 36 
# print(lcm(7,13))  # 91
# print(lcm(1,2))   # 2
# print(lcm(5,5))   # 5

print(f'{2**26 + 3**26 + 2**10 + 3**10}  == {2**36 + 3**36}') # True