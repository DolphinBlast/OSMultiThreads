import math
import csv


def Amatrix(i, j):
    return round(10 * math.sin(math.radians(i)) - 0.6 * j, 5)

def Bmatrix(i, j):
    return round(7 - 12 * math.cos(math.radians(5 * j)) + 1.8 * i, 5)

A =  [[0] * 80 for _ in range(50)]      #A50x80
B =  [[0] * 50 for _ in range(80)]      #B80x50

for i in range(0,50,1):
    for j in range(0,80,1):
        A[i][j] = Amatrix(i+1, j+1)

for i in range(0,80,1):
    for j in range(0,50,1):
        B[i][j] = Bmatrix(i+1, j+1)

print(A)


with open("matrixA.csv", "w", newline="") as csvf:
    writer = csv.writer(csvf)
    writer.writerows(A)

with open("matrixB.csv", "w", newline="") as csvf:
    writer = csv.writer(csvf)
    writer.writerows(B)