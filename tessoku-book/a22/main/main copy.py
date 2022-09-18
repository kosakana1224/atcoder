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
・masu[i]:i番目のマスにいる時の合計スコアの最大値

<キーワード>
・普通のDP

<ポイント>
・初期値-INFだとだめ?
普通にジャッジのミスでした。


"""
#--------------------------------------------------------------
N = INT()
A = [0]+LIST()
B = [0]+LIST()
masu = [0]*(N+1)
masu[1] = 0
for i in range(1,N):
    masu[A[i]] = max(masu[A[i]],masu[i]+100)
    masu[B[i]] = max(masu[B[i]],masu[i]+150)
print(masu[N])

