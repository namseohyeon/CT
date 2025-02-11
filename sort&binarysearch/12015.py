import bisect

N = int(input())
A = list(map(int,input().split()))
 
LIS = []

for num in A:
    pos = bisect.bisect_left(LIS, num)

    if pos == len(LIS):
        LIS.append(num)
    else:
        LIS[pos] = num
        
print(len(LIS))
