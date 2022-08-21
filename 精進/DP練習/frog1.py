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
○DPの流れの復習
・DP配列全体をDPの種類に応じた初期値で初期化
・初期条件を入力
・ループを回す
・テーブルから解を得て出力

○初期化する値について
・最小化問題　INF
・最大化問題 -INF
・数え上げ/確率問題　0
・Yes/No判定 False

○ポイント
dp[i] には i 番目までの探索過程がまとめられている

"""
#--------------------------------------------------------------
N = int(input())
H = list(map(int,input().split()))
dp = [-1]*(N+1)
dp[1] = 0
dp[2] = abs(H[0]-H[1])
for i in range(3,N+1):
    dp[i] = min(dp[i-1]+abs(H[i-1-1]-H[i-1]),dp[i-2]+abs(H[i-2-1]-H[i-1]))
print(dp[N])

