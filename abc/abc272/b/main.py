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
3 3
2 1 2
2 2 3
2 1 3
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>


<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
N,M = MAP()
s = set()
for _ in range(M):
    KX = LIST()
    K = KX[0]
    X = KX[1:]
    for i in range(K):
        for j in range(i+1,K):
            s.add((X[i],X[j]))
            s.add((X[j],X[i]))

flag = True
for i in range(N):
    for j in range(i+1,N):
        if (i+1,j+1) not in s:
            flag = False
        if (j+1,i+1) not in s:
            flag = False
if flag:
    print("Yes")
else:
    print("No")