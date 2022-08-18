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
"""
bit全探索はN=23まで間に合いますよ???????
"""
#--------------------------------------------------------------
_INPUT = """\
3 3
1 1 1
1 1 1
1 1 1
1 1
1
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
H1,W1 = MAP()
A = [LIST() for _ in range(H1)]
H2,W2 = MAP()
B = [LIST() for _ in range(H2)]
print()



