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
2 3 1
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<point>
・遷移をよく見ると区間和になっているDP→累積和を求めておくと高速化できる
・累積和で高速化する場合は[貰うDP]で考える!!!!!
・ある範囲からある範囲までの値を貰うときに貰う部分のDPの値の累積和を計算しておく
→先に累積和を求めておくと計算量を減らすことができる
→遷移の数をM→1に大きく減らすことができる
"""
#--------------------------------------------------------------
# pypyで提出

# 入力の受け取り
N,M,K=map(int,input().split())
# 余りの定義
Mod=998244353
# (1)表を作る
dp=[[0]*(M+1) for i in range(N+1)]
# (2)すぐにわかるところを埋める
# ・(1≤x≤M)dp[1][x]=1
# i=1~M
for i in range(1,M+1):
    # 1を埋める
    dp[1][i]=1
# (3)表の小さい方から答えにたどり着くまで埋める
# i=2~N
for i in range(2,N+1):
    # 累積和の計算
    CumSum=[0]*(M+1)
    # x=1~M
    for x in range(1,M+1):
        CumSum[x]=CumSum[x-1]+dp[i-1][x]
        CumSum[x]%=Mod
    print(CumSum)
    # x=1~M
    for x in range(1,M+1):
        # K=0
        # ・(2≤i)dp[i][x]=CumSum[M]
        if K==0:
            dp[i][x]=CumSum[M]
        # 0<K
        else:
            # ・(2≤i,x-K<1)dp[i][x]=CumSum[M]-CumSum[x+K-1]
            # ・(2≤i,M<x+K)dp[i][x]=CumSum[x-K]
            # ・(2≤i,それ以外)dp[i][x]=(CumSum[M]-CumSum[x+K-1])+CumSum[x-K]
            if 1<=x-K:
                dp[i][x]+=CumSum[x-K]
            if x+K<=M:
                dp[i][x]+=CumSum[M]-CumSum[x+K-1]
        # 余りを取る
        dp[i][x]%=Mod
    print(dp)
# (4)答えを出力する
# 答え
ans=0
# dp[N][1]~dp[N][M]の和
# x=1~M
for x in range(1,M+1):
    ans+=dp[N][x]
    # 余りを取る
    ans%=Mod

# 答えの出力
print(ans)





