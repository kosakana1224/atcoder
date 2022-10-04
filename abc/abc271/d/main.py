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
3 11
1 4
2 3
5 7
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
dp = [[False]*(S+1) for _ in range(N+1)]
dp[0][0] = True
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
    exit()

now = S
ans = ""
"""
while now!=0:
    for i in range(1,N+1)[::-1]:
        for s in range(S+1)[::-1]:
            if now == s + AB[i-1][0] and dp[i][now] and dp[i-1][s]:
                ans += "H"
                now -= AB[i-1][0]
                break
            elif now == s + AB[i-1][1] and dp[i][now] and dp[i-1][s]:
                ans += "T"
                now -= AB[i-1][1]
                break
"""
for i in range(N-1,-1,-1):
    a,b = AB[i]
    if dp[i][now-a]:
        now -= a
        ans += "H"
    else:
        now -= b
        ans += "T"
print(ans[::-1])


