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
5
30
-10
20
-10
20
3
1 2
3 5
1 4

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
D = INT()
X = INT()
kabu = [X]
A = [INT() for _ in range(D-1)]
for i in range(D-1):
    kabu.append(kabu[i]+A[i])
    
Q = INT()
for _ in range(Q):
    s,t = MAP()
    s,t = s-1,t-1
    if kabu[s] == kabu[t]:
        print("Same")
    elif kabu[s] > kabu[t]:
        print(s+1)
    else:
        print(t+1)
    