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
3 1 3


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・制約を見ようpartN
・2重ループなので、i,j間の距離をO(1)で求めることができたら問題を解くことができる!!!
・最悪、LCAを使うとN^2*log(N)で無理やり通せそう? -->木じゃないなら無理ですか????

・辺の数はそれぞれ高々1,2本なので、場合分け頑張れば求められそう?
<キーワード>

<ポイント>


"""
#--------------------------------------------------------------
N,X,Y = MAP()
X,Y = X-1,Y-1
G = [[] for _ in range(N)]
for i in range(N-1):
    G[i].append((i+1,1))
G[X].append((Y,1))
G[Y].append((X,1))

ans = [0]*N
for i in range(N):
    for j in range(i+1,N):
        print()
for a in ans:
    print(a)

