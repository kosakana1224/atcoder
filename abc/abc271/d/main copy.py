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
5 25
2 8
9 3
4 11
5 1
12 6


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・dp復元するだけでは?

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
N,S = MAP()
AB = [LIST() for _ in range(N)]
dp = [[[False]*(N+1) for _ in range(S+1)] for _ in range(2)]
dp[0][0][0] = True
dp[1][0][0] = False
print(dp)
for i in range(N):
    for s in range(S+1):
        if dp[i][s]:
            if s+AB[i][0]<=S:
                dp[i+1][s+AB[i][0]] = True
            if s+AB[i][1]<=S:
                dp[i+1][s+AB[i][1]] = True
def debeg():
    for i in range(N):
        for s in range(S+1):
            print(dp[i][s],end=" ")
        print()

if dp[N][S]:
    print("Yes")
else:
    print("No")
