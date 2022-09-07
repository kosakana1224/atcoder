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
・毎回ソートすると、制約オーバー
・ソート後の先頭の要素は最小値、ソート時点の配列の大きさの範囲までは昇順であることが保証できる

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
Q = INT()
A = []
for _ in range(Q):
    query = LIST()
    if query[0]==1:
        #Aの最後尾にxを追加する
        x = query[1]
        
    elif query[0]==2:
        #Aの最初の要素を出力し、その後その要素を削除する
    else:
        #Aを昇順にソートする
        