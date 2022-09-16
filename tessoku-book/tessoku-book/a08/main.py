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
5 5
2 0 0 5 1
1 0 3 0 0
0 8 5 0 2
4 1 0 0 6
0 9 2 7 0
2
2 2 4 5
1 1 5 5

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・各クエリあたりO(1)で解かなければならない
・左向きに累積和を取った後、上か下向に累積和を取ればいいのでは
・O(HW+Q)なら間に合う
・累積和を取るときは配列を大きめにとらないとおかしくなるので注意が必要

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
H,W = MAP()
X = [LIST() for _ in range(H)]
ruisekiX = [[0]*(W+1) for _ in range(H+1)]
Q = INT()
for h in range(H):
    for w in range(W):
        ruisekiX[h+1][w+1] = X[h][w]
for h in range(H+1):
    for w in range(W):
        ruisekiX[h][w+1] += ruisekiX[h][w]
for w in range(W+1):
    for h in range(H):
        ruisekiX[h+1][w] += ruisekiX[h][w]
for _ in range(Q):
    a,b,c,d = MAP()
    print(ruisekiX[c][d]-ruisekiX[c][b-1]-ruisekiX[a-1][d]+ruisekiX[a-1][b-1])