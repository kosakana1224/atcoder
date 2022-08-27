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
10
1 4 602436426
2 1 623690081
3 3 262703497
4 4 628894325
5 3 450968417
6 1 161735902
7 1 707723857
8 2 802329211
9 0 317063340
10 2 125660016

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
dp[t][i]:i番目をt秒に取った時の大きさの合計の最大値

"""
#--------------------------------------------------------------
N = INT()
TXA = [LIST() for _ in range(N)]
dp = [[0]*5 for _ in range(TXA[N-1][0]+1)]
sunuke = [[0]*5 for _ in range(TXA[N-1][0]+1)]
for t,x,a in TXA:
    sunuke[t][x] = max(sunuke[t][x],a)
#for i in range(len(sunuke)):
    #print(sunuke[i])
for t in range(1,TXA[N-1][0]+1):
    for i in range(5):
        if t==1:
            if i==2:
                break
        if t==2:
            if i==3:
                break
        if t==3:
            if i==4:
                break
        if i==0:
            dp[t][i] = max(dp[t-1][i],dp[t-1][i+1]) + sunuke[t][i]            
        elif i==4:
            dp[t][i] = max(dp[t-1][i],dp[t-1][i-1]) + sunuke[t][i]
        else:
            dp[t][i] = max(dp[t-1][i],dp[t-1][i-1],dp[t-1][i+1]) + sunuke[t][i]
ans = 0
for i in range(5):
    ans = max(ans,dp[TXA[N-1][0]][i])
print(ans)
    
            
        
    
    


