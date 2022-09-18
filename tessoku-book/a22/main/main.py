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
7
2 4 4 7 6 7
3 5 6 7 7 7

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・masu[i]:i番目のマスにいる時の合計スコアの最大値
・普通にDPしても
・DAGじゃないからだめ?
→トポロジカルソートしましょう?
・貰うDPを考えることによりDAG順で考えることができるのでは?

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
N = INT()
A = [0]+LIST()
B = [0]+LIST()
Anew = [[] for _ in range(N+1)]
Bnew = [[] for _ in range(N+1)]
for i in range(N):
    Anew[A[i]].append(i)
    Bnew[B[i]].append(i)
#dp[i]:iマスに辿り着くまでに得られる合計の最大値
#print(Anew)
#print(Bnew)
dp = [-INF]*(N+1)
dp[1] = 0
for i in range(2,N+1):
    for a in Anew[i]:
        #print(f"a{i} {a}")
        dp[i] = max(dp[i],dp[a]+100)
    for b in Bnew[i]:
        #print(f"b{i} {b}")
        dp[i] = max(dp[i],dp[b]+150)
print(dp[N])
#print(dp)

