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
mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
10 3
3 1 4 1 5 9 2 6 5 3
3 8
4 5
2 4
6 8
6 10
2 9
2 7
1 7
1 10
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
- N頂点の無向木は、頂点iに整数aiが書かれてある
- cが含まれる
"""
#--------------------------------------------------------------
N,K = MAP()
A = LIST()
G = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = MAP()
    a,b = a-1,b-1
    G[a].append(b)
    G[b].append(a)

for i in range(N):
    ans = 0
    dist = [-1]*N
    dist[i] = A[i]
    que = deque([i])
    while que:
        now = que.popleft()
        for nxt in G[now]:
            if dist[nxt] == -1:
                dist[nxt] = A[nxt]
                dist[nxt] += dist[now]
                que.append(nxt)
    for k in range(N):
        if dist[k]!=-1:
            ans += pow(dist[k],K,mod)
    if len(G[i])==1:
        print(ans%mod)
        continue
    que = deque([i])
    flag = [False]*N
    flag[i] = True
    tmp = []
    while que:
        now = que.popleft()
        cnt = 0
        for nxt in G[now]:
            if flag[nxt]==False:
                cnt += 1
                flag[nxt] = True
                que.append(nxt)
        if cnt==0:
            tmp.append(dist[now])
    tmpsum = sum(tmp)
    ans += tmpsum - A[i]
    print(ans%mod)





