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
4
100 150 130 120


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
・frag1と同じ
・添字ミスに気をつける
"""
#--------------------------------------------------------------
N = INT()
A = LIST()
dp = [INF]*(N+1)
dp[1] = 0
dp[2] = abs(A[1]-A[0])
for i in range(3,N+1):
    dp[i] = min(dp[i-1]+abs(A[i-1]-A[i-1-1]),dp[i-2]+abs(A[i-1]-A[i-2-1]))
print(dp)
