import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import permutations, product,combinations,accumulate
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
3 3
1 2
1 3
2 3
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・頂点1を始点として全ての頂点を一度だけ訪れるパスは何通りあるか
→dfsで行ける?
・制約的にはbit全探索やN!
・思い付いたのはN!の並び方を全探索してそれがグラフ的に成り立つかを調べるというもの
これっぽい!

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
N,M = MAP()
G = [[False]*N for _ in range(N)]
for _ in range(M):
    a,b = MAP()
    a,b = a-1,b-1
    G[a][b] = True
    G[b][a] = True
elements = list(range(1,N))
ans = 0
for item in permutations(elements,N-1):
    item = [0]+list(item)
    flag = True#全ての頂点がつながっているならTrue
    for i in range(N-1):
        u,v = item[i],item[i+1]
        if not G[u][v]:
            flag = False
    if flag:
        ans += 1
print(ans)
        
