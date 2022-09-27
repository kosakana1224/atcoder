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
・どの時間帯にもM人以上が勤務して、かつ、10時間までそれぞれ働くことができる場合
それが実現可能か。

・単純に貪欲に実装してみるが、めんどくさそう
・多分貪欲解はWA

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
N,M = MAP()
C = [LIST() for _ in range(N)]
remain_time = [10]*N #i番目の人があと何回働くことができるか
for i in range(N):
