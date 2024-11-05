n = 3
def transpose(A,B):
    for i in range(n):
        for j in range(n):
            B[i][j]  = A[j][i]
A = [[1,2,3],
     [3,4,5],
     [6,7,8]]

B = [[0] * n for _ in range(n)]

print("The original matrix is: ")
for i in range(n):
    for j in range(n):
        print(A[i][j],"",end = " ")
    print()

transpose(A,B)

print("The resultant matrix is: ")
for i in range(n):
    for j in range(n):
        print(B[i][j],"",end = " ")
    print()