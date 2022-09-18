import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
from bisect import bisect_right,bisect_left 
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
<考察>

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
N = INT()
C = 0
D = N+1
A = 0
B = N+1
while (B-A)>1:
    mid = (B + A)//2
    print(f"? {1} {mid} {1} {N}")
    cnt = INT()
    if mid==cnt:#1~midの間になかったら
        A = mid
    else:
        B = mid
        
while (D-C)>1:
    mid = (C + D)//2
    print(f"? {1} {N} {1} {mid}")
    cnt = INT()
    if mid==cnt:#1~midの間になかったら
        C = mid
    else:
        D = mid

print(f"! {B} {D}")
 