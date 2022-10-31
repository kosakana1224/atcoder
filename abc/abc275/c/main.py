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
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・4か所のポーンの選び方は高々、81C4=4.4*10**7でこれは間に合う.
判定部分をO(1)で書けば良い。

<キーワード>
・全探索
・正方形の判定方法

<ポイント>
・正方形の頂点間の　距離として考えられるのは高々6本,それと小さい順にソートして、
大きい2本は√2kになればよい。

"""
#--------------------------------------------------------------