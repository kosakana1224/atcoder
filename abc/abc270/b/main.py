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
10 -10 1

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
X,Y,Z = MAP()
if 0<X<Y:
    print(X)
elif 0<Y<X:
    if 0<Z<Y:
        print(X)
    elif Z<0:
        print(2*abs(Z)+X)
    else:
        print(-1)
elif Y<0<X:
    print(X)
elif X<0<Y:
    print(-X)
elif Y<X<0:
    print(-X)
elif X<Y<0:
    if Y<Z<0:
        print(-X)
    elif Z>0:
        print(2*abs(Z)+abs(X))
    else:
        print(-1)
else:
    print(-1)