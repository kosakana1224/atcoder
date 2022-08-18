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
N,M,E = MAP()
G = [[] for _ in range(N+M)]
H = []
for _ in range(E):
    u,v = MAP()
    u,v = u-1,v-1
    H.append((u,v))
Q =  INT()
X = LIST()
for i in range(E):
    u,v = H[i][0],H[i][1]
    if i+1 not in X:
        G[u].append(v)
        G[v].append(u)
        
    
    
