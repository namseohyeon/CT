N, K = map(int,input().split())

A = []
sum = 0
for i in range(N):
    x = int(input())
    A.append(x)
    # print(A)

for i in range (len(A)-1,-1,-1):
    sum += K//A[i]
    K = K%A[i]
print(sum)