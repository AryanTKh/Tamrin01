str_input=input()
str_input=str_input.split()
dic={}
for str in str_input:
    val=str[0]
    num=str[1:]
    dic[num]=val

sort_dic = sorted(dic.items(), key=lambda x: int(x[0]) )
m=''
for i in sort_dic:
	m = m + i[1]

print(m)