import math
type=input()
x=[]
while 1:
    n=input()
    if n=="end":
        break
    else:
        try:
            x.append(int(n))
        except ValueError:
            print("Invalid command")


###################  SUM
if type=="sum":
    print(sum(x))

###################  AVERAGE
if type == "average":
    m=sum(x)
    b=len(x)
    avg=float(m/b)
    avg = round(avg, 2)
    print(avg)

###################  LCD
if type == "lcd":
    tt=True
    for p in x:
        if p<0:
            tt=False
    if tt==True:
        lcm = x[0]
        for number in x[1:]:
            lcm = lcm * number // math.gcd(lcm, number)
        print(lcm)
    else:
        print("Invalid command")

###################  GCD
if type == "gcd":
    ttt=True
    for p in x:
        if p<0:
            ttt=False
    if ttt==True:
        gcd = x[0]
        for number in x[1:]:
            gcd = math.gcd(gcd, number)
        print(gcd)
    else:
        print("Invalid command")

###################  MIN
if type == "min":
    print(min(x))

###################  MAX
if type == "max":
    print(max(x))
