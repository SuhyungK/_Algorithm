import sys
sys.stdin = open('SWEA_1210_ladder1.txt')

# 1. 밑에서부터 위로 1을 따라서 올라가는 로직
# 2. 좌, 우를 먼저 검사하고 없으면 위로 올라가도록 짰을 때 좌, 우에 더 이상 1이 없으면 역으로 우, 좌로 해서 왔던 길을 되돌아가게 돼서 실패
# 3. 우선 위로 올라가고 있을 때는 한 칸마다 좌, 우 검사를 하고 없으면 위로 올라가게 함
# 4. 좌우로 갈 때는 if ~elif를 사용해서 더 이상 1이 없으면 idx를 0으로 받게해서 위로 이동할 수 있게 함
# 5. 4번 방법을 하면 좌로 이동하는 게 실패할 때 우로 가는 방법을 건너뛰고(elif니까) 위로 이동할 수 있음
# 6. 원래 이동하는 함수를 따로 만들었는데 어차피 그냥 이동은 계속 할 거고 그 기준이 되는 idx 값이 필요하니까 그것만 반환받는 방법
# 7. 사실 이건 좀 비효율적인 코드같고 실제로 딴 사람들이 짠 거 보니까 arr[x][y-1] 와 같은 방식으로 좌, 우 이동을 하는 것 같다
# 근데 이렇게하려면 양 옆에 0을 붙여주는 padding 이라는 작업을 해야 하는데 난 그냥 그렇게 안 하고도 푸는 방식으로 풀어보고 싶어서

# 상 좌 우
dx = [-1, 0, 0]
dy = [0, -1, 1]

# 이동하고 싶은 칸에 값이 존재하는가를 판단하는 함수
def nav(x, y, idx=0):
    x += dx[idx]
    y += dy[idx]
    if 0 <= x < 100 and 0 <= y < 100 and arr[x][y] == 1:
        return idx
    else:
        return 0

for _ in range(10):
    tc = input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    x = 98

    for i in range(100):
        if arr[99][i] == 2:
            y = i
            break
    
    idx = 0
    # 길 찾기
    while 1:
        # 최상단에 도달하면 탈출
        if x == 0:
            break
        # 위로 올라갈 때
        # 좌우 중 값이 1인게 있으면 그쪽으로 먼저 이동
        # 없다면 위로 이동
        if idx == 0:
            if nav(x, y, 1):
                idx = 1
            elif nav(x, y, 2):
                idx = 2
        # 좌우로 이동하고 있을 때, idx = 1 or 2
        # 더 이상 1이 없으면 무조건 위로 이동
        else:
            if idx == 1:
                idx = nav(x, y, 1)
            elif idx ==2:
                idx = nav(x, y, 2)
        # 위에서 각각 받은 idx 값으로 이동
        x += dx[idx]
        y += dy[idx]


    print('#%s %d' %(tc, y))
    