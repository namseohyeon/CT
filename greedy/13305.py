N = int(input())
road_length=list(map(int,input().split()))
cost = list(map(int, input().split()))
sum = 0
min_cost = cost[0]


for i in range(N-1):
    if cost[i] < min_cost:
        min_cost = cost[i]
    sum += min_cost*road_length[i]

print(sum)


