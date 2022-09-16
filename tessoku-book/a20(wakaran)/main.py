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
7
2 4 4 7 6 7
3 5 6 7 7 7

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・masu[i]:i番目のマスにいる時の合計スコアの最大値
・普通にDPしても
・DAGじゃないからだめ?
→トポロジカルソートしましょう?

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
N = INT()
A = [0]+LIST()
B = [0]+LIST()
G1 = [[] for _ in range(N+1)]
G2 = [[] for _ in range(N+1)]
for i in range(1,N):
    G1[i].append(A[i])
    G2[i].append(B[i])

def topologicalsort(N, G):
    import heapq
    in_number = [0] * N #各頂点の枝の本数をカウントするためのリストを用意する
    for i in G:
        for v in i:
            in_number[v] += 1 #頂点vの入次数をカウントする
    S = [] #手順1:空のリストを用意する。
    queue = [i for i in range(N) if in_number[i] == 0] #入次数が0の頂点を記録するためのリストを用意
    heapq.heapify(queue) # リストを優先度付きキューへ
    while queue:
        u = heapq.heappop(queue) #手順2.1：入次数が0の頂点でかつ最小の頂点uを取り出す
        S.append(u) #手順2.2：手順1で作ったリストSに追加しています。
        for u2 in G[u]:
            in_number[u2] -= 1 #手順2.3：uから出ている辺（枝）を削除
            if in_number[u2] == 0: #uから出ている辺を削除していく作業で頂点u2の入次数が0となった場合
                heapq.heappush(queue, u2) #u2はuの候補となる
    return S
S1 = topologicalsort(N+1,G1)
S2 = topologicalsort(N+1,G2)
masu = [-INF]*(N+1)
masu[1] = 0

for i in range(1,N):
    masu[A[S1[i]]] = max(masu[A[S1[i]]],masu[S1[i]]+100)
    masu[B[S2[i]]] = max(masu[B[S2[i]]],masu[S2[i]]+150)
"""
for s in S1:
    s -= 1
    masu[A[s]] = max(masu[A[s]],masu[s]+100)

for s in S2:
    s -= 1
    masu[B[s]] = max(masu[B[s]],masu[s]+150)
"""
print(masu[N])
