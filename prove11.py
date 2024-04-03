def gcd(x,y):
    r = y % x
    while r!= 0:
        x = y
        y = r
        r = x % y
        print(x, y, r)

gcd(39,501)

import math

print(math.gcd(39,501))

# def extended_euclid(a, b):
#     """
#     This function returns the gcd of a and b followed by
#     the coefficients x and y of the equation ax + by = gcd(a, b)
#     """
#     if a == 0:
#         return b, 0, 1
#     else:
#         g, x1, y1 = extended_euclid(b % a, a)
#         # Update x and y using results of recursive call
#         x = y1 - (b // a) * x1
#         y = x1
#         return g, x, y

# # Example usage
# if __name__ == "__main__":
#     # You can replace these values with the numbers from your first three problems
#     a, b = 110,765
#     gcd, x, y = extended_euclid(a, b)
#     print(f"The GCD of {a} and {b} is {gcd}, which can be expressed as ({a})*({x}) + ({b})*({y}) = {gcd}")

# p = 137
# q = 211
# e = 65537
# N = 28907
# phi = 28560
# d = 3953

# # Message to be encrypted
# m = 5645

# # Encrypt the message
# c = pow(m, e, N)  # Encrypted message
# print(f"Encrypted message: {c}")

# # Decrypt the message
# decrypted_m = pow(c, d, N)  # Decrypted message, should be equal to m
# print(f"Decrypted message: {decrypted_m}")