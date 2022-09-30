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
4 5 30
1 100 2 180
2 200 3 300
1 80 3 360
3 400 3 410
3 450 4 600

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・有向グラフかつ(重みつき?)
・向きがあるからDAGで考えたい。
・制約的には重み付きグラフとして考えないと間に合わない
・最大で何本の飛行機に乗ることができるかについて、なので、
・制約的に探索は一回しかできない

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
N,M,K = MAP()
G = [[] for _ in range(N)]

for _ in range(M):
    a,s,b,t = MAP()
    a,b = a-1,b-1
    G[a].append((b,s,t))
    


