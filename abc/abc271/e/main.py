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
3 2 3
1 2 1
2 3 1
2 1 1

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・Eの部分列を通る経路が良い経路
・通る長さの合計の最小値→基本的に、短い道の方が早いに決まっている
・都市1からNまでいく経路のお話
・良い経路の中で1~Nに到達できるルートを探す?

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
N,M,K = MAP()
G = [[] for _ in range(N)]
ES = [(0,0,0)]
for i in range(M):
    a,b,c = MAP()
    a,b = a-1,b-1
    ES.append((a,b,c))
    G[a].append((b,c,i))
E = LIST()

def dijkstra(G,start,s,s2,pre):
  """
  ダイクストラ法(優先度付きキュー使用)
  from heapq import heappop,heappushの使用を忘れずに！
  引数：グラフ（重み付き）、スタート地点
  返り値：頂点の個数分の配列を返し、スタートから配列のindexまでの最短距離を求めることが出来る
  """
  N = len(G)
  #距離の管理
  INF = float('inf')
  dist = [INF]*N #スタート地点以外の値は∞で初期化  
  #スタート地点の重み（距離）
  dist[start] = 0 #スタートは0で初期化
  pq = [(0,start)] #ヒープには(その頂点へのコスト：頂点)の情報が入っている
  while pq:
    #ヒープから取り出し
    cost,v = heappop(pq)
    if dist[v] != cost: continue
    #最もコストが小さい頂点を探す
    for u,d,i in G[v]:#G[u]にはつながっている頂点番号とそこへのコストが入っている
      new_cost = cost + d
      #更新条件
      if dist[u] > new_cost and (i+1 in s2) or ((pre,i+1) in s): 
        pre = i+1
        dist[u] = new_cost
        heappush(pq,(new_cost,u)) #pqに(new_cost,v)
  return dist
s = set() 
s2 = set()
for i in range(K-1):
    a,b = E[i],E[i+1]
    s.add((a,b))
for i in range(K):
    s2.add(E[i])

dist = dijkstra(G,0,s,s2,-1)
if dist[N-1]==INF:
    print(-1)
else:   
    print(dist[N-1])





