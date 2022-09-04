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
dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
15
0 1
0 6
0 14
1 2
1 4
3 5
3 6
3 7
6 9
8 10
8 14
9 12
9 13
11 14
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""

"""
#--------------------------------------------------------------
N = INT()
G = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = MAP()
    G[a].append(b)
    G[b].append(a)
    
que = deque([0])
dist = [-1]*N
dist[0] = 0
ans = INF

while que:
    now = que.popleft()
    if len(G[now])==0:
        ans = min(ans,dist[now])
    for nxt in G[now]:
        if dist[nxt]==-1:
            dist[nxt] = dist[now] + 1
            que.append(nxt)

print(ans)