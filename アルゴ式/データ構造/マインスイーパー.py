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
4 5
.##.#
##...
..#..
.....
3
1 2
0 0
3 4
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
やるだけ
なお、上から x 行目 (0 始まり)、左から y 列目 (0 始まり) のマスを (x,y) と表すこととします。
を見逃して大変なことに。。。

"""
#--------------------------------------------------------------
H,W = map(int,input().split())
grid = [list(input()) for _ in range(H)]
Q = int(input())
for _ in range(Q):
    y,x = map(int,input().split())
    cnt = 0
    for dx,dy in dirc:
        nx,ny = x + dx,y + dy
        if not (0<=nx<W and 0<=ny<H):
            continue
        if grid[ny][nx]=="#":
            cnt += 1
    print(cnt)