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
4 10 3
##...#.##.
.#....#...
##.####..#
#..######.

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・各マスを調べて行って、黒>白の数が大きいものから順番に消していく(最大K回まで)?
→色々実装してみたけど違いそう
・貪欲だとダメでなんか法則があるかも
↓だけどわからない
BFSで全てのパターンについて遷移できそう?
(H+w)^10
→無理やんけ

<キーワード>
・制約に注目する
・操作順序に問わない
・bit全探索

<ポイント>
・Hの制約が小さいので、H方向の選び方は全探索できる→bit全探索
・W方向について、最適なものを順番に選べばよい

"""
#--------------------------------------------------------------
H,W,K = MAP()
grid = [list(input()) for _ in range(H)]
