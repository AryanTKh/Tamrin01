n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(100)]
# for row in matrix:
#     print(row)
matrix[0][0] = 1

i = 0
j = 0
b = False
while(True):
    newinput = input()
    if(newinput == "END"):
        break

    if(newinput == "L"):
        if(j - 1>=0):
            j -= 1
    if(newinput == "R"):
        if(j + 1 <= n-1):
            j += 1
    if (newinput == "B"):
        i += 1
    matrix[i][j] = 1


if(j == n-1):
    b = True
for row in matrix:
    if not 1 in row:
        break
    for el in row:
        if el == 1:
            print("*", end=" ")
        else:
            print(".", end=" ")
    print()
if(not b):
    print("There's no way out!")