# 쉬운 최단거리

# 2의 위치를 찾고 & 갈 수 없는 곳의 visited 값을 0으로 초기화
def _init():
    si = sj = -1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                si, sj = i, j
            elif not arr[i][j]:
                visited[i][j] = 0
    return si, sj

# bfs 탐색으로 각 칸에 대해 2에서부터의 최단 거리 구하기
def bfs(si, sj):
    queue = [(si, sj)]
    
    visited[si][sj] = 0
    while queue:
        i, j = queue.pop(0)

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni<0 or nj<0 or ni>=n or nj>=m or visited[ni][nj] != -1:
                continue
                
            if arr[ni][nj] == 0:
                visited[ni][nj] = 0
                continue

            visited[ni][nj] = visited[i][j] + 1
            queue.append((ni, nj))


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

si, sj = _init()
di = (0, 1, -1, 0)
dj = (1, 0, 0, -1)

bfs(si, sj)

for row in visited:
    print(*row)