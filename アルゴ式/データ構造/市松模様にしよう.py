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
3 3
...
...
...
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・市松模様は２パターンしかないので、開始が白か黒かでそれぞれ反転すべき枚数を求めて、
小さい方が答え

<ポイント>
・市町模様についての場合分けがh+wの偶奇で判定できるのは重要
"""
#--------------------------------------------------------------
H,W = MAP()
grid = [input() for _ in range(H)]
ans1 = 0
ans2 = 0
for h in range(H):
    for w in range(W):
        turn = (h+w)%2
        if turn==0:
            if grid[h][w]=="#":
                ans1 += 1
            else:
                ans2 += 1
        else:
            if grid[h][w]=="#":
                ans2 += 1
            else:
                ans1 += 1
print(min(ans1,ans2))
                
            
            
