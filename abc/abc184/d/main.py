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
31 41 59


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・いずれかの種類の硬貨が100枚になるまで、以下の操作を繰り返す
・操作回数の期待値を求める
・袋の中から硬貨をランダムに一枚取り出し、取り出した硬貨と同じ種類の硬貨を２枚袋に戻す

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
A,B,C = MAP()

