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
・循環セールスマン問題っぽい
N個の街は全て通る+M個の宝箱を取るかもしれないので最大でN+M=17の階乗
->これはこれはいわゆるbitDP

<キーワード>
bitDP
https://www.youtube.com/watch?v=Oc1JP9XmIsU
<ポイント>

"""
#--------------------------------------------------------------
N,M = MAP()
XY = [LIST() for _ in range(N)]
PQ = [LIST() for _ in range(M)]
dp = [[INF]*(N+M) for _ in range(2**(N+M))]





