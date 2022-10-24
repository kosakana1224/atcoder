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
2
400 500 100 600 300 200


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
N = INT()
A = LIST()
ato = []
for i in range(3*N):
    ato.append([i,A[i]])
ato.sort(key=lambda x:x[1])
tmp = []
for i in range(N,2*N):
    tmp.append(ato[i][0])
tmp.sort()
for i in tmp:
    print(i+1)