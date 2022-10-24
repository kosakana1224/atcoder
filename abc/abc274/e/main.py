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
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・奇数回目のときx軸方向、偶数回目の時y軸方向に移動することができる
・x,yの座標方面だけ考えれば良い??

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
N,x,y = MAP()
A = LIST()
xArray = []
yArray = []

for i in range(N):
    if i%2==0:
        xArray.append(A[i])
    else:
        yArray.append(A[i])

sx,sy = 0,0
for dx in xArray:
    


