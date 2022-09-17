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
..........
..........
..........
..........
...######.
...######.
...######.
...######.
..........
..........

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
grid = [list(input()) for _ in range(10)]
flag = False
for h in range(10):
    for w in range(10):
        if flag==False and grid[h][w]=="#":
            flag = True
            A,C = h,w
cntx = 0
for x in range(C,10):
    if grid[A][x]=="#":
        cntx += 1
cnty = 0
for y in range(A,10):
    if grid[y][C]=="#":
        cnty += 1
B = A+cnty-1
D = C+cntx-1
print(f"{A+1} {B+1}")
print(f"{C+1} {D+1}")
    
        
