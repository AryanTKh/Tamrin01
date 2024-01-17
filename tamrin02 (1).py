def maqsoom(num):
    sum=0
    for i in range(1,num+1):
        if num%i == 0:
            sum=sum+i
    return sum

def decimal_to_base(num, base):
    result = ""
    while num > 0:
        remainder = num % base
        result = str(remainder) + result
        num = num // base
    return result
q=0
while 1:

    num1, num2 = map(int, input().split())
    if num1==-1 and num2==-1:
        break
    if num2>9:
        print("invalid base!")
        break
    if num2<2:
        print("invalid base!")
        break
    m = maqsoom(num1)
    result = decimal_to_base(m, num2)
    q=q+int(result)
if q!=0:
    print(q)




