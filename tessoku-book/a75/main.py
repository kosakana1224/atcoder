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
4
20 70
30 20
30 100
20 60

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・所謂区間スケジューリング問題では?
-期限が短いやつでかつかかる時間が短い問題から解いていくという方針。
→7WAでた

別の方針を考えてみる
・Ti,Diが極端に小さい→二次元ぐらいのDPだったら解ける範囲
・dp[i]:i分

<キーワード>
・問題を解く上でのポイント
-少しずつヒントを見つけていく
・問題設定を変えて考えてみる

<ポイント>
・問題設定を変えてヒントを得る
-今回の問題では、最大で何問正解できるかではなく最後の問題まで到達することができるかという簡単な設定を考える
・すると、最後の問題まで到達することができるかは問題を順番にみてDPすればいけそうだとわかり、
・何分,i問目の地点で何問解けているかのDPを考えていきたくなる
・問題を解くか解かないかの遷移ができ、また問題の締め切りが小さい順に当然したくなるため、ソートする必要も出てくるだろう

このように問題設定を変えてみるとヒントが出てきたり、今まで解いたことのあるような問題を似た問題に置き換えることができるように
なるだろう。

"""
#--------------------------------------------------------------
N = INT()
TD = [LIST() for _ in range(N)]
TD.sort(key = lambda x:(x[1],x[0]))
now = 0
idx = 0
ans = 0
while idx<N:
    if now+TD[idx][0]<=TD[idx][1]:
        now += TD[idx][0]
        idx += 1
        ans += 1
    else:
        idx += 1
print(ans)
    