import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
INF = float('inf')
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
2 2
2
1 2
2
1 2
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
自分の考察
*同じ筒に２個ある→不可能
*別の筒で向きが異なるグラフ→不可能=閉路があると不可

<ポイント>
*無向グラフの閉路→UnionFindでroot一致したら閉路
*有向グラフの閉路→トポロジカルソートができないとき閉路
*DAG:有向非巡回グラフ
*DAGである(有向グラフ閉路なし)⇔トポロジカルソートできる
if トポロジカルソート後の配列の長さ==N:
    閉路
else:
    閉路ではない
"""
#####################################################
N,M = MAP()
flag = True
G = [[] for _ in range(N)]
for _ in range(M):
    k = INT()
    a = LIST()
    for i in range(k-1):
        G[a[i]-1].append(a[i+1]-1)

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
S = topologicalsort(N,G)  
print(S)
#print(S)       
if len(S)==N:
    print('Yes')
else:
    print('No')








