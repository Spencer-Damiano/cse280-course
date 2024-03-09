
# def fun1(n):
#     # Add recursive code here
#     if n == 0:
#         return 5
#     else:
#         return fun1(n-1) + 3*n


# def fun2(n):
#     # Add recursive code here
#     if n == 0:
#         return 1
#     else:
#         return n**3 + fun2(n-1)


# def fun3(n):
#     # Add recursive code here
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 3
#     else:
#         return fun3(n-1) * (fun3(n-2))


# def fun4(n):
#     # Add recursive code here
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 5
#     else:
#         return fun4(n-1) + fun4(n-2)**2


# print([fun1(n) for n in range(10)]) # [5, 8, 14, 23, 35, 50, 68, 89, 113, 140]
# print([fun2(n) for n in range(10)]) # [1, 2, 10, 37, 101, 226, 442, 785, 1297, 2026]
# print([fun3(n) for n in range(10)]) # [1, 3, 3, 9, 27, 243, 6561, 1594323, 10460353203, 16677181699666569]
# print([fun4(n) for n in range(10)]) # [1, 5, 6, 31, 67, 1028, 5517, 1062301, 31499590, 1128514914191]


seq1 = [n**3 for n in range(1, 54)]

seq2 = [2**n - 2 for n in range(4,28)]# Add list comprehension here

seq3 = [n**5 + 1 for n in range(-3, 19)] # Add list comprehension here

seq4 = [2**n for n in range(-2,8)] # Add list comprehension here

print(sum(seq1)) # 2047761
print(sum(seq2)) # 268435392
print(sum(seq3)) # 6656947
print(sum(seq4)) # 255.75