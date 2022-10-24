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
4
1 3 5 2


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
N = INT()
A = LIST()
ans = [-1]*(2*N+2)
ans[1] = 0
Ameba = []
for i in range(N):
    Ameba.append((i+1,A[i]))#i番目はAiが分裂して、2iと2i+1に
Ameba.sort(key=lambda x:x[1])
for i,ai in Ameba:
    if 2*i<=2*N+1:
        ans[2*i] = ans[ai] + 1
    if 2*i+1<=2*N+1:
        ans[2*i+1] = ans[ai] + 1
for a in ans[1:]:
    print(a)


