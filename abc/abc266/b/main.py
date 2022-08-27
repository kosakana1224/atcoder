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
-9982443534


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
N-x = 998244353m
998244353 > x = N - 998244353m >= 0

"""
#--------------------------------------------------------------
N = INT()
m = N//998244353
x = N - (998244353*m)
if 0<=x<998244353:
    print(x)
    exit()

m = (N - 998244353)//998244353
x = N - (998244353*m)
if 0<=x<998244353:
    print(x)
    exit()
