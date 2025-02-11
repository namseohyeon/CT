import heapq
import sys

input =sys.stdin.read
data = list(map(int, input().split()))
n = data[0]
cards = data[1:]

if n==1:
    print(0)
    exit()

# 최소 힙(우선순위 큐)사용용
heapq.heapify(cards)

total_cost = 0

while len(cards) > 1:
    first = heapq.heappop(cards)
    second = heapq.heappop(cards)
    cost = first + second
    total_cost += cost

    heapq.heappush(cards, cost)

print(total_cost)