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
import math
#dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<焼き鈍し法>
・山登り法では点数が良くなった場合のみ変化を受け入れるが、焼きなまし法では
点数が低くなってもある確率が受け入れる

1.山登り法 2.温度関数(どの時間帯にはどの程度のスコアの悪化を許すか) 
3.遷移確率関数(新たな状態に遷移する確率を決定する関数)

<ポイント>
・相性のいい問題:状態Aと状態A'の関係性がなるべく近い状態であり、
各状態間のスコア変化がなめらかな問題

"""
#--------------------------------------------------------------
start_temp = 20
end_temp = 5
def temperature(経過時間, 制限時間):# 温度関数
    x = 経過時間 / 制限時間
    return pow(start_temp, 1 - x) * pow(end_temp, x)

def prob(score, new_score, 経過時間, 制限時間): # 確率関数
    d = new_score - score
    if d >= 0:
        return 1
    return exp(d / temperature(経過時間, 制限時間))

state = 初期状態を作る
score = 初期状態のスコアを計算する
while 現在までの実行時間 < 制限時間:
    new_state = 近傍を取る
    new_score = 近傍のスコアを計算する
    if prob(score, new_score, 経過時間, 制限時間) > random():
        state = new_state
        score = new_score





