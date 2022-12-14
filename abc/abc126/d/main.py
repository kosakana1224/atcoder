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
3
1 2 2
2 3 1

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・根から距離が偶数のところは黒、そうでない奇数部分は白で塗れば良い。
→AC!

<キーワード>
・木
・bfs

<ポイント>

"""
#--------------------------------------------------------------
N = INT()
G = [[] for _ in range(N)]
for _ in range(N-1):
    u,v,w = MAP()
    u,v = u-1,v-1
    G[u].append((v,w))
    G[v].append((u,w))

Vcolor = [-1]*N
Vcolor[0] = 0
print(Vcolor)
que = deque()
que.append([0,0])#(頂点番号,根からの距離)
while que:
    now,total_dist = que.popleft()
    for nxt,w in G[now]:
        if Vcolor[nxt]==-1:
            nxt_dist = total_dist + w
            if nxt_dist%2==0:
                Vcolor[nxt] = 0
            else:
                Vcolor[nxt] = 1
            que.append((nxt,nxt_dist))
for a in Vcolor:
    print(a)
                