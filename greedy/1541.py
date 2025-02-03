expression = input().split('-')
num = []

for i in expression: 
    sum = 0
    tmp = i.split('+')
    for j in tmp:
        sum += int(j)
    num.append(sum)

n = num[0]

for i in range(1, len(num)): #1번째 값부터 n에서 빼준다
    n -= num[i]
print(n)