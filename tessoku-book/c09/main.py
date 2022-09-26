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
5
2 5 3 3 1

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・遷移が単純なDPでした。

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
N = INT()
A = LIST()
#dp[se][i]
dp = [[0]*2 for _ in range(N+1)]
#dp[0][1] = A[0]
for i in range(1,N+1):
    dp[i][0] = dp[i-1][1]+A[i-1]
    dp[i][1] = max(dp[i-1][0],dp[i-1][1])
print(max(dp[N][0],dp[N][1]))
