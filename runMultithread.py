import csv
import threading
import time
from datetime import datetime

A=[]
B=[]
C_R=[]
with open("matrixA.csv", "r") as csvf:
    rows = csv.reader(csvf)
    for row in rows:
        numeric_row = [float(x) for x in row]
        A.append(numeric_row)

with open("matrixB.csv", "r") as csvf:
    rows = csv.reader(csvf)
    for row in rows:
        numeric_row = [float(x) for x in row]
        B.append(numeric_row)

with open("matrixC_R.csv", "r") as csvf:
    rows = csv.reader(csvf)
    for row in rows:
        numeric_row = [float(x) for x in row]
        C_R.append(numeric_row)

print("Matrix A & B read successfully.")

while True:
    splitX=input("Please input how many THREAD that you want to split in each cal.")
    splitY=input("Please input how many THREAD that you want to split in each row.")
    splitX=int(splitX)
    splitY=int(splitY)
    if 50%splitX==0 and 50%splitY==0:
        Xindex=50//splitX
        Yindex=50//splitY
        print("Xindex: ", Xindex)
        print("Yindex: ", Yindex)
        break

ready = 0
start_event = threading.Event()
threads = [[0] * 50 for _ in range(50)]
C = [[0] * 50 for _ in range(50)]      #C50x50


def matrixTimes(X, Y, rangeX, rangeY, number, start_event):
    global ready
    #print(X, Y, rangeX, rangeY, number)
    print("Thread", number, "is ready")
    ready += 1
    start_event.wait()
    for i in range(rangeX):
        for j in range(rangeY):
            for k in range(80):
                C[i+X][j+Y] += A[i+X][k] * B[k][j+Y]


number = 0
for i in range(0,splitX):
    for j in range(0,splitY):
        number += 1
        threads[i][j] = threading.Thread(target = matrixTimes, args = (i * Xindex, j * Yindex, Xindex, Yindex, number, start_event))
        threads[i][j].start()

while ready < splitX * splitY:
    print("Waiting for all threads to be ready")
    time.sleep(0.1)
print("All threads are ready")

while input("Waitting for user cheak to start(y to start)") != "y":
    print("Waiting for user to check")

print("All threads are running now")
saveSystemTime = datetime.now()
start_event.set()

for i in range(0,splitX):
    for j in range(0,splitY):
        threads[i][j].join()

runningTime = datetime.now() - saveSystemTime
print("Running time: ", runningTime)
print("Done")

if C == C_R:
    print("Matrix C is correct.")
else:
    print("Matrix C is incorrect.")


