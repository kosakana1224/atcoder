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
300 100 400 100 500
3
500
250
40
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・最大何個の商品を取れるか
→DPでやるのが良い?
・にぶたんで求める?
・小さい順に貪欲していけば良い?
→累積和求めていたら楽そう

<キーワード>

<ポイント>
ソートして累積和2分探索

"""
#--------------------------------------------------------------
N = INT()
C = LIST()
C.sort()
Ccum = list(accumulate(C))
Q = INT()
for _ in range(Q):
    x = INT()
    idx = bisect_right(Ccum,x)
    print(idx)
    
    

    
    