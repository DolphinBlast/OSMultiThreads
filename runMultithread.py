import csv
import threading
import time

A=[]
B=[]
with open("matrixA.csv", "r") as csvf:
    rows = csv.reader(csvf)
    for row in rows:
        A.append(row)

with open("matrixB.csv", "r") as csvf:
    rows = csv.reader(csvf)
    for row in rows:
        B.append(row)
print(A)
print(len(A))
print(len(A[0]))
print(B)
print(len(B))
print(len(B[0]))


print("Matrix A & B read successfully.")



splitX=input("Please input how many THREAD that you want to split in each cal.")
splitY=input("Please input how many THREAD that you want to split in each row.")

splitX=int(splitX)
splitY=int(splitY)

ready=0
threads=[[]]
def matrixTimes(i, j):
    time.sleep(10)
    

for i in range(0,splitX):
    for j in range(0,splitY):
        threads[i].append(threading.Thread(target = matrixTimes, args = (i, j)))
        threads[i][j].start()


for i in threads:
    i.join()

print("Done")



