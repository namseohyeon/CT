import sys

#N = int(input())
N = int(sys.stdin.readline().rstrip())
arr = []
count = 0
EP = 0

for i in range (N):
    #ST, ET = map(int,input().split())
    ST, ET = map(int, sys.stdin.readline().rstrip().split())
    arr.append([ST,ET])

arr.sort(key=lambda x: (x[1], x[0]))
# print(arr)

for NS, NE in arr:
    if EP <= NS:
        count += 1
        EP=NE
print(count)
    

