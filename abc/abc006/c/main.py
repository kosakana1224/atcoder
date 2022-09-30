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
3 9
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
人間N人
大人・老人・赤ちゃんの三種
足の数がM本,大人の足は2,老人3,赤ちゃん4
存在する組み合わせを出力
部分点1:全て全探索
部分点2:全探索の計算量工夫
満点解法:
二つの式があるから変数を一つ減らすことができる
otona*2+roujin*3+akatyan*4 = M
otona*2 + roujin*2 + akatyan*2 = 2*N 
--------------------------------------
roujin + akatyan*2 = M-2*N
roujin = (M-2*N)-(2*akatyan) とすることができるため,
赤ちゃんの個数を全探索することでこれを満たすかどうかを考えるだけで良くなる?

<キーワード>
・工夫して全探索
・計算量を改善するのに、条件を満たす式を立式してみると、意外と答えが見えてくるかも?

<ポイント>
・出力の順番を間違えて2WAしてしまいました
"""
#--------------------------------------------------------------
N,M = MAP()
for akatyan in range(N+1):
    roujin = (M-2*N)-(2*akatyan)
    otona = N - (akatyan+roujin)
    if 0<=roujin<=N and 0<=otona<=N:
        print(f"{otona} {roujin} {akatyan}")
        exit()
print(f"-1 -1 -1")
        
