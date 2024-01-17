lst = input().split()
lst = [int(i) for i in lst]
sum_value = int(input())
lst_sf = []
complements = {}

for i, num in enumerate(lst):
    complement = sum_value - num
    if complement in complements and i != complements[complement]:
        lst_sf.append(i + complements[complement])
    complements[num] = i

if lst_sf:
    lst_sf.sort()
    for i in lst_sf:
        print(i)
else:
    print('Not Found!')