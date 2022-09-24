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
3
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・全ての頂点の次数が2であるような連結な無向グラフをひとつ作成せよ
→こういう問題は楽なパターンを考えると良い

・頂点番号順に一直線のグラフ+端と端を結ぶと良いのでは?
<キーワード>

<ポイント>
"""
#--------------------------------------------------------------
N = INT()
print(N)
for i in range(1,N):
    print(i,i+1)
print(1,N)
