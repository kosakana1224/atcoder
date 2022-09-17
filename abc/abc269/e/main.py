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
"""
<考察>

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
grid = [".....#..",
        "#.......",
        "....#...",
        ".#......",
        ".......#",
        "..#.....",
        "......#.",
        "........"]
def q(A,B,C,D):
    A,B,C,D = A-1,B-1,C-1,D-1
    cnt = 0
    for h in range(A,B+1):
        for w in range(C,D+1):
            if grid[h][w]=="#":
                cnt += 1
    return cnt
N = 8
ngx = 0
okx = N+1
ngy = 0
oky = N+1
for _ in range(20):
    if not abs(ngx-okx)>1 and not abs(ngy-oky)>1:
        print(f"! {okx} {oky}")
        exit()
    elif abs(ngx-okx)>1 and not abs(ngy-oky)>1:
        mid = (ngx + okx)//2
        print(f"? {1} {N} {1} {mid}")
        cnt = INT()
        if mid==cnt:#1~midの間になかったら
            okx = mid
        else:
            ngx = mid
    elif not abs(ngx-okx)>1 and abs(ngy-oky)>1:
        mid = (ngy + oky)//2
        cnt = INT()
        print(f"? {1} {mid} {1} {N}")
        if mid==cnt:#1~midの間になかったら
            oky = mid
        else:
            ngy = mid
    else:
        mid = (ngx + okx)//2
        print(f"? {1} {N} {1} {mid}")
        cnt = INT()
        if mid==cnt:#1~midの間になかったら
            okx = mid
        else:
            ngx = mid
        
        
    
