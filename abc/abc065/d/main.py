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
6
8 3
4 9
12 19
18 1
13 5
7 6




"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・座標(a,b)->(c,d)の移動距離は,min(|a-c|,|b-d|)
・マンハッタン距離とチェビシェフ距離
・最小全域木を求めたい
・X,Y独立にして考える?

<キーワード>

<ポイント>
・最小全域木
・考えるべき辺の数を減らせないか考えるのは定番
→x,y独立にそれぞれ考えた時、隣接した部分だけを考えれば良い->思いついてたのに...


"""
#--------------------------------------------------------------
N = INT()
XY = [LIST()for _ in range(N)]


    