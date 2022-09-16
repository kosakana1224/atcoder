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
"""
<考察>

<キーワード>
・DP復元について

<ポイント>

"""
#--------------------------------------------------------------
N = INT()
A = [0]+LIST()
B = [0]+[0]+LIST()
dp = [INF]*(N)
dp[1] = A[1]
dp[2] = min(dp[1]+A[2],B[2])
for i in range(3,N):
    dp[i] = min(dp[i],dp[i-1]+A[i],dp[i-2]+B[i])
now = N-1
ans = [N]
while not (now==1 or now==2):
    if dp[now]==dp[now-2]+B[now]:
        now -= 2
    elif dp[now]==dp[now-1]+A[now]:
        now -= 1
    ans.append(now+1)
ans.append(1)
ans.reverse()
ans = list(set(ans))
print(len(ans))
print(*ans)