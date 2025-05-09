A=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
B=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
C=[[0]*len(B[0]) for _ in range(len(A))]      #C50x50
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]
print(C)