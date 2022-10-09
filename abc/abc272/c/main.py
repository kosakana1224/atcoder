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
<考察>
・偶数と奇数に分けて考える

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
N = INT()
A = LIST()
guusu = []
kisuu = []
for a in A:
    if a%2==0:
        guusu.append(a)
    else:
        kisuu.append(a)
if len(guusu)<=1 and len(kisuu)<=1:
    print(-1)
else:
    ans = []
    if len(guusu)>=2:
        guusu.sort(reverse=True)
        ans.append(guusu[0]+guusu[1])
    if len(kisuu)>=2:
        kisuu.sort(reverse=True)
        ans.append(kisuu[0]+kisuu[1])
    print(max(ans))
