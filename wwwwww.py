a = int(input())
s = input().strip("،.:").split()
w = input()
lst=[]
for i in s:
    m = w
    z=i
    num = 0
    if len(z)>len(m):
        m+= "_"*(abs(len(i)-len(m)))
    if len(m)>len(z):
        z+= "$"*(abs(len(z)-len(m)))
    for j in range(len(z)):
        x = z[j]
        y = m[j]
        if x!=y:
            num+=1
    if num<=a:
        lst.append(i)

for i in lst:
    print(i.strip("،.:"))




