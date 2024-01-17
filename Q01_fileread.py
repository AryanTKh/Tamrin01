import numpy as np

filename = input()

matrices = []
with open(filename, 'r') as file:
    num_matrices, matrix_dim = map(int, file.readline().split())
    for _ in range(num_matrices):
        matrix = []
        for _ in range(matrix_dim):
            row = list(map(int, file.readline().split()))
            matrix.append(row)
        matrices.append(matrix)

matrices = np.array(matrices)

m = 0
ii = 0
jj = 0
for i in range(num_matrices):
    for j in range(num_matrices):
        if (i!=j):
            z = np.dot( matrices[i] , matrices[j] )
            b = np.linalg.det(z)
            if b > m :
                ii , jj = i , j
                m = b
D_1 = np.linalg.det(matrices[ii])
D_2 = np.linalg.det(matrices[jj])
if ( D_1 >= D_2 ):
    D = np.dot( matrices[ii] , matrices[jj] )
if ( D_2 > D_1 ):
    D = np.dot( matrices[jj] , matrices[ii] )

b=np.linalg.inv(D)
for i in range(matrix_dim):
    for j in range(matrix_dim):
        print( '{:.3f}'.format( b[i][j])  , end = " " )
    print('')




