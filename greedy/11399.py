import sys
peoples= []
sum = 0
time = 0

#N = int(sys.stdin.readline().rstrip())
N = int(input())
peoples = list(map(int, input().split()))
#peoples = sys.stdin.readline().rstrip().split()
peoples.sort()

for i in range(N):
    time += int(peoples[i]) #각자 처리 시간
    sum += time #각자 처리 시간을 모두 합한 값값
print(sum)