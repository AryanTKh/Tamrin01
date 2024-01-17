a=int(input())
b=int(input())
diff = a ^ b
bit_count = bin(diff).count('1')
print(bit_count)