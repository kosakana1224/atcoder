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

"""
#--------------------------------------------------------------
N,M,T = MAP()
A = LIST()
bonus = [-1]*(N)
for _ in range(M):
    x,y = MAP()
    x = x-1
    bonus[x] = y

now = T 
flag = True
for i in range(N-1):
    now -= A[i]
    if now<=0 and i!=N-2:
        flag = False
    if bonus[i+1]!=-1:
        now += bonus[i+1]

if flag:
    print("Yes")
else:
    print("No")
    