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
4 7
3 13
3 17
5 29
1 10

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・N=10**2,W=10**5,O(NW)はOK!
・dp[N][1~W]:N個選んで、重さが1~Wの時の価値の合計の最大値
・配るDP

<キーワード>

<ポイント>
・自力ACやったね
"""
#--------------------------------------------------------------
N,W = MAP()
dp = [[0]*(W+1) for _ in range(N+1)]
WV = [LIST() for _ in range(N)]
for i in range(N):#i番目の品を選ぶ
    for w in range(W+1):
        #品物を選ぶ
        if w+WV[i][0]<=W:
            dp[i+1][w+WV[i][0]] = dp[i][w] + WV[i][1]
        #品物を選ばないとき
        if w+1<=W:
            dp[i][w+1] = max(dp[i][w],dp[i][w+1])
        if i+1<=N:
            dp[i+1][w] = max(dp[i][w],dp[i+1][w])
print(max(dp[N]))
        

