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
mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
2 1 0



"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・問題概要:
長さNの配列であり、大きさが1~M,配列間の差がabs(Ai-Ai+1)>=Kのものという条件を
満たす配列の個数は何通りあるか
→何通りかを求める問題といえば、DPでいけそう(制約的にも)
制約から二次元DPまでいけそう

DP問題?を解く(流れに沿って)
・dp[i][m]:配列のi番目の大きさがmの時何通りあるか
・遷移を考える
・貰うDPで一旦考えてみる。
dp[i][m] += dp[i-1][1~m-K and m+K~N]でいけそう
それぞれのdp[i][m]を調べるのにオーダーO(N^2)で、遷移にO(N)掛かると制約オーバー:(
→遷移の部分をどうにかしてO(1)にしたい。
→累積和をうまく使えないか考える
アイデア
・dp[i][m]列目の処理が終わった段階で、累積和をとる(新たなDP配列を作る(DP2としてみる))→その必要もないかも?
・dp[i-1][1~M-K]はdp[i-1][M-K]一発、dp[i-1][m+K~M]はdp[i-1][M]-dp[i-1][m+K-1]で行けるのでは?
→これにより、累積和をうまく使うことにより遷移の部分をO(1)で処理できるので、全体をO(NM)で解くことが可能になった
実装しましょう

・2WAでた!どこやねん
→

"""
#--------------------------------------------------------------
N,M,K = MAP()
dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(1,M+1):
    dp[1][i] = 1
#累積和取り方(2~N)まで累積和取ればいい
for i in range(2,M+1):
    dp[1][i] += dp[1][i-1]
for i in range(2,N+1):
    #遷移
    for m in range(1,M+1):
        if m-K>=1:
            dp[i][m] += dp[i-1][m-K]
        if m+K<=M:
            dp[i][m] += dp[i-1][M]-dp[i-1][m+K-1]
        dp[i][m] %= mod
    #累積和をとる
    for m in range(2,M+1):
        dp[i][m] += dp[i][m-1]
        dp[i][m] %= mod
print(dp[N][M]%mod)
        
