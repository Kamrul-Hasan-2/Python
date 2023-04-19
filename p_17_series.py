# 1 + 2 + 3 + .... + n
num = int (input("Enter a last number: "))
sum = 0
for i in range(1, num+1, 1):
    sum += i
print(sum)