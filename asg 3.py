a11= int(input("enter number for a11:"))
a12= int(input("enter number for a12:"))
a21= int(input("enter number for a21:"))
a22= int(input("enter number for a22:"))
b11= int(input("enter number for b11:"))
b12= int(input("enter number for b12:"))
b21= int(input("enter number for b21:"))
b22= int(input("enter number for b22:"))
A= [[a11,a12],
    [a21,a22]]
B= [[b11,b12],
    [b21,b22]]
C= [[0,0]for i in range(2)]
for i in range(2):
    for j in range(2):
        C[i][j]=A[i][j]+B[i][j]
        print("addition of two matrix is:", C)
for i in range(2):
    for j in range(2):
        C[i][j]=A[i][j]-B[i][j]
        print("subtraction of two matrix is:", C)
for i in range(2):
    for j in range(2):
        for k in range(2):
         C[i][j] += A[i][k]*B[k][j]
        print("multiplication of two matrix is:", C)
for i in range(2):
    for j in range(2):
        C[i][j]=A[j][i]
        print("Transpose of matrix A is:" , C)
for i in range(2):
    for j in range(2):
        C[i][j]=B[j][i]
        print("Transpose of matrix B is:" , C)
        
    
      
