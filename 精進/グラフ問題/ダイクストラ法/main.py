import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
from bisect import bisect_right,bisect_left 
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
INF = float('inf')
import math
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
4 7
1 2 10
2 3 30
1 4 15
3 4 25
3 4 20
4 3 20
4 3 30
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・毎回bfsして?
・重み付きだからダイクストラ?→これが正解。
"""
#--------------------------------------------------------------
def dijkstra(G,start):
    N = len(G)
    #距離の管理
    INF = float('inf')
    dist = [INF]*N #スタート地点以外の値は∞で初期化
    #スタート地点の重み（距離）
    #dist[start] = 0 #スタートは0で初期化
    pq = [(INF,start)] #ヒープには(その頂点へのコスト：頂点)の情報が入っている
    cnt = 0
    while pq:
        #ヒープから取り出し
        cnt += 1
        cost,v = heappop(pq)
        if dist[v] != cost: continue
        #最もコストが小さい頂点を探す
        for v,d in G[v]:#G[u]にはつながっている頂点番号とそこへのコストが入っている
            if cnt==1:
                new_cost = d
            else:
                new_cost = cost + d
            #更新条件
            if dist[v] > new_cost: 
                dist[v] = new_cost
                heappush(pq,(new_cost,v)) #pqに(new_cost,v)
    return dist

N,M = MAP()
G = [[]*N for _ in range(N)]
for _ in range(M):
    a,b,c = MAP()
    a,b = a-1,b-1
    G[a].append((b,c))
    
for i in range(N):    
    ans = dijkstra(G,i)[i]
    if ans==INF:
        print(-1)
    else:
        print(ans)

"""
for i in range(N):
    dist = [INF]*N
    que = deque()
    que.append(i)
    flag = False
    while que:
        now = que.popleft()
        for nxt,cost in G[now]:
            if dist[nxt]==INF:
                if now==i:
                    dist[nxt] = cost
                else:
                    dist[nxt] = min(dist[now] + cost,dist[nxt])
                que.append(nxt)
    print(dist[i])
"""