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
dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
7
100 101 110 111 1000000 100 100
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<ポイント>
・連想配列を使えば、必要な場所だけの登場回数を知ることができる

"""
#--------------------------------------------------------------
N = INT()
A = LIST()
d = defaultdict(int)
for a in A:
    d[a] += 1
ans = 0
for i,k in d.items():
    if i>k:
        ans += k
    elif i<k:
        ans += k-i
print(ans)