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
dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
15 8
1 1 2 3 4 4 4 5 5 6 7 7 8 9 10
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・ソートしてにぶたん?
a+b=m
b=m-a aを全探索してb=m-aとなるbを二分探索する
→二分探索するまでもなく、連想配列で取り出せばいいだけ

<ポイント>
整数 i と M−i のペアを選ぶ総数は、counter[i] から 1 個、
counter[M−i] から 1 個選ぶ方法の、 計 counter[i]×counter[M−i] 通りと基本的には表せます。
"""
#-------------------------------------------------------------
N,M = MAP()
A = LIST()
d = defaultdict(int)
for a in A:
    d[a] += 1
ans = 0
for a in A:
    b = M-a
    if b!=a:
        ans += d[b]
    else:
        ans += max(0,d[b]-1)
print(ans//2)

    