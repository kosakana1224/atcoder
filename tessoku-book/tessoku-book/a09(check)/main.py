import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
INF = float('inf')
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
5 5 2
1 1 3 3
2 2 4 4

"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
二次元にもす法
区間の重なる領域を前処理をすることでO(N+HW)で可能に！

・左上と右下を+1,左下と右上を-1する
・右下の座標を使う点に関しては座標を+1してから加算する(累積和をとる関係で)
・配列は大きめにとる
"""
######################################################
H,W,N = MAP()
grid = [[0]*(W+5) for _ in range(H+5)]
for _ in range(N):
    ly,lx,ry,rx = MAP()
    #ここの前処理ミスってた(アホ)
    grid[ly][lx] += 1
    grid[ly][rx+1] -=1
    grid[ry+1][rx+1] += 1
    grid[ry+1][lx] -=1

#横方向に累積和
for y in range(1,H+1):
    for x in range(1,W+3):
        grid[y][x+1] += grid[y][x]

#縦方向に累積和
for x in range(1,W+1):
    for y in range(H+3):
        grid[y+1][x] += grid[y][x]

for h in range(1,H+1):
    for w in range(1,W+1):
        print(grid[h][w],end=" ")
    print()
    