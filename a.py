from collections import deque

# 入力の受け取り
N = int(input())
G = [[] for _ in range(N)]    # グラフを表現する隣接リスト
for i in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

# 頂点 0 を根とする
r = 0
# 根を始点として幅優先探索を行う
dist = [-1 for _ in range(N)]   # dist[i]：根から頂点 i までの距離
que = deque([]) # これから調べるべき頂点を管理するキュー
# 根を始点として登録する
dist[r] = 0
que.append(r)

# キューが空になるまで、探索を続ける
while len(que) > 0:
    # 次に調べるべき頂点を v とする
    v = que.popleft()

    # 頂点 v に隣接する頂点 nv について、
    for nv in G[v]:
        # 頂点 nv が探索済みならば、スキップする
        if dist[nv] != -1: continue
        # そうでないならば、dist[nv] を確定させてキューに nv を挿入する
        dist[nv] = dist[v] + 1
        que.append(nv)
# print(G)
# print(dist)
# dist の中の最大値が答え
ans = max(dist)
print(ans)