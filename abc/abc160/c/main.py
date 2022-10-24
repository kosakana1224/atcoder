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
20 3
0 5 15




"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・今いる場所から最も遠い場所への距離の最小値を求めたい?
-なんか違う?
-円環の問題は2周する?
-普通に考えて後戻り(=来た道を戻る)はする必要がない
-2周する部分の処理をミスっていた....。

<キーワード>
・円環は2倍して考えるテクを使うだけ

<ポイント>
・円環を2倍するテクを使う時は-を考えるのではなく、さらにプラスした部分を作る
-じゃないとコードがバグります!!!!!!!!!!!!!!!!!!!!!!

"""
#--------------------------------------------------------------
K,N = MAP()
A = LIST()
B = []
for a in A:
    B.append(a)
for a in A:
    B.append(a+K)
ans = INF
for i in range(N+1):
    ans = min(ans,B[i+N-1]-B[i])
print(ans)




