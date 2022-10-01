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
1
5



"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
N = INT()
a = LIST()
a.sort()
dp = [-1]*(N+1)#i冊目に到達することはできるか
dp[0] = 0
cnt = 1
for i in range(N):
    if a[i]==cnt:

    



