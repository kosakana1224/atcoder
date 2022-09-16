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
8
5
2 3
3 6
5 7
3 7
1 5

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・いもす法は配列のとる大きさに注意が必要?

<キーワード>

<ポイント>
・いもす法は適当に大きめの配列を取りましょう
・累積和を考える時はsum[0]=0にすることで、1番端のケースも対応できるようになる

"""
#--------------------------------------------------------------
D = INT()
N = INT()
day = [0]*(D+5)
for _ in range(N):
    l,r = MAP()
    day[l] += 1
    day[r+1] -= 1
for i in range(D):
    day[i+1] += day[i] 
for d in day[1:D+1]:
    print(d)