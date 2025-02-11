import sys

# 입력 받기
data = sys.stdin.read().split()  # 모든 입력을 한 번에 읽어와 리스트로 변환
N, C = map(int, data[:2])  # 첫 두 개 값을 정수로 변환
house = list(map(int, data[2:N+2]))  # 나머지 N개의 값을 정수 리스트로 변환

# 1️⃣ 집 위치 정렬
house.sort()

# 2️⃣ 이분 탐색 설정
left = 1  # 공유기 간 최소 거리
right = house[-1] - house[0]  # 최대 거리
answer = 0  # 최적 거리 저장

# 3️⃣ 이분 탐색 시작
while left <= right:
    mid = (left + right) // 2  # 공유기 간 거리 (중간값)
    count = 1  # 첫 번째 집에 공유기 설치
    last_installed = house[0]  # 마지막으로 공유기 설치한 위치

    # 4️⃣ 공유기 배치 시뮬레이션
    for i in range(1, N):
        if house[i] - last_installed >= mid:
            count += 1
            last_installed = house[i]  # 공유기 설치 위치 갱신

    # 5️⃣ 공유기 개수에 따라 탐색 범위 조정
    if count >= C:  # C개 이상 설치 가능하면 거리 늘리기
        answer = mid  # 최적 거리 갱신
        left = mid + 1
    else:  # C개 설치 불가능하면 거리 줄이기
        right = mid - 1

# 결과 출력
print(answer)
