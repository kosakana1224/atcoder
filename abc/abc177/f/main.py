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
4 4
2 4
1 1
2 3
2 4

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・右か下にしか移動することができない
・最小の移動回数について各マス調べる
・各行について、各行に到達するのにかかる最小回数を調べる
・#の部分は上からは通ることができないが、横からはすり抜けできる(今回のgridだと)
・後グリッドを作ると計算量がO(4*10^10)となりOUT
↓
さあどうしよう。
まるで目処が立たないって黄diffかーいそりゃ無理やわ(終了)

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
H,W = MAP()
AB = [LIST() for _ in range(H)]
#サンプル例
"""
....
.###
#...
.##.
.###

(4 4)
2 4 開始が1じゃなかったら1,そうでなければ、終点が=Wでなければ、終点+2,そうでなければ-1
1 1 前回の位置とかぶっていなければ1,そうでなければ、終点と比較、同じ感じ。
2 3
2 4
"""
