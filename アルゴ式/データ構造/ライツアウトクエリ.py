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
dirc = [(0,1),(0,-1),(1,0),(-1,0),(0,0)]
dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
3 2
..
..
..
5
1 1 0
0 0 1
0 1 1
0 2 1
1 1 0
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・クエリ処理がO(logN)でやらないと間に合わないのでは?
・クエリ内容：上下左右全体の黒ますの個数、上下左右隣接マスを反転
・差分計算のやつやん!!!!
"""
#--------------------------------------------------------------
H,W = MAP()
grid = [list(input()) for _ in range(H)]
Q = INT()
Hcnt = [0]*H
Wcnt = [0]*W
for h in range(H):
    cnt = 0
    for w in range(W):
        if grid[h][w]=="#":
            cnt +=1
    Hcnt[h] += cnt
    
for w in range(W):
    cnt = 0
    for h in range(H):
        if grid[h][w]=="#":
            cnt += 1
    Wcnt[w] += cnt

for _ in range(Q):
    a,p,q = MAP()
    if a==0:
        for dx,dy in dirc:
            ny = p+dy
            nx = q+dx
            if not (0<=ny<H and 0<=nx<W):
                continue
            if grid[ny][nx]=="#":
                grid[ny][nx] = "."
                Wcnt[nx] -= 1
                Hcnt[ny] -= 1
            else:
                grid[ny][nx] = "#"
                Wcnt[nx] += 1
                Hcnt[ny] += 1
    else:
        cnt = Hcnt[p]+Wcnt[q]
        if grid[p][q]=="#":
            cnt -= 1
        print(cnt)
        