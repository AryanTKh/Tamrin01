a = int(input())
b = int(input())

j = bin(b)[2:].zfill(32) + bin(a)[2:].zfill(32)

n = int(input())

for i in range(n):
    d = int(input())
    if d <= 0 or d > 63:
        print("no")
    elif j[63 - d] == '0':
        print("no")
    elif j[63 - d] == '1':
        print("yes")
        





