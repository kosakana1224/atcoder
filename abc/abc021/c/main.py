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
mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
7
1 7
8
1 2
1 3
4 2
4 3
4 5
4 6
7 5
7 6



"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・aからbへの最短経路の数
・DP

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
N = INT()
a,b = MAP()
a,b = a-1,b-1
M = INT()
G = [[] for _ in range(N)]
for _ in range(M):
    x,y = MAP()
    x,y = x-1,y-1
    G[x].append(y)
    G[y].append(x)
que = deque([a])
dist = [-1]*N
cnt = [0]*N
dist[a] = 0
cnt[a] = 1
while que:
    now = que.popleft()
    for nxt in G[now]:
        if dist[nxt]==-1:
            dist[nxt] = dist[now]+1
            cnt[nxt] = cnt[now]
            que.append(nxt)
        else:
            if (dist[nxt]==dist[now]+1):
                cnt[nxt] += cnt[now]
print(cnt[b]%mod)