n=int(input())
lst=[]
for i in range(n):
    mail=input()
    for str in mail :
        if str=="@":
            ind=mail.index("@") + 1
            lst.append(mail[ind:])
            break

final_list = sorted(list(set(lst)))

for char in final_list:
    print(char)

