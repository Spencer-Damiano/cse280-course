import numpy as np

A = np.array([[4,-1,0,0,0,0,-1,-1,-1],
              [-1,3,-1,0,0,0,0,-1,0],
              [0,-1,3,-1,0,0,-1,0,0],
              [0,0,-1,3,-1,0,0,-1,0],
              [0,0,0,-1,3,-1,-1,0,0],
              [0,0,0,0,-1,3,-1,0,-1],
              [-1,0,-1,0,-1,0,4,0,-1],
              [-1,-1,0,-1,0,-1,0,4,0],
              [-1,0,0,0,0,-1,-1,0,3]
              ])

eigenA = (np.linalg.eigvals(A))
eigenAProd = 1.93850115 * 5.76401493 * 3.60366147 * 4.69382246 * 5.8136065 * 1.65707692 * 3.52931658 * 3.0

print(A)
print(eigenA)
print(eigenAProd/9)