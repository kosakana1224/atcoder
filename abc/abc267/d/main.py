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
4 2
5 4 -1 8
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・制約か二次元DPっぽいことだけはわかる

<キーワード>
・二次元DP

<再掲(DPについて)>
・まとめられる処理をまとめて、同じ計算を行わないようにする
・探索の拡張と考える（重要）
・DPはpypy
・なにか規則性を見つけて「正しい選び方の法則」のようなものを見つけようとしがち
→すべて探索することが大切、単純に探索すると計算時間が間に合わない場合は、
どのように計算結果をまとめていくかを考えるとよい

<ポイント1>
・DPで求めるもののパターン
1,最小値・最大値 2,数え上げ

・問題を見たらまずやること
1,選択肢を網羅する
2,制約条件があるなら選択肢が制約条件を満たすかチェック
3,制約条件を満たしたやつの中での最大値を求め、制約条件を満たしたら+1して数えていく

・DP問題でクリアすべきこと
1,DPテーブルの定義を考える(これから始めるの当たり前やろ!!!!)
→テーブルの大きさは制約から見えてくるので、欲しい条件からテーブルを考えるのは一つのポイントかも
2,漸化式を考える(遷移を考える)
3,状態、計算量を減らせる部分があったら減らす

<本問題の考察・思考・ポイント>
・制約から二次元DPっぽいのはわかる
↓どういうDPテーブルにしよう???
・DP[部分列の開始地点(N)?][選択個数(M)]:開始地点n,選択個数mの時の求める答えの最大値
↓(部分列の開始地点だとうまく遷移が思いつかない,,,,。)
・DP[i番目の要素を][m番目に選択した時]の最大値
↓(遷移どうする?)
dp[n][m+1] = max({0~n-1番目の中の要素(i番目)で、m番目に選択した時の値}+A[i]*(M+1))????
↓(計算量を減らさないと今のままだとオーダーがO(N^3))
↓(ここから解説AC)
・隣同士を見ればいいじゃん!
・「制約条件を満たした奴の中での最大値を求め、制約条件を満たしたら+1して数えていく」の部分をどう処理するか。
・選択するかしないかの判定をどうするか
選択したらdp[n][m] = (dp[n-1][m-1]+A[n]*m)
選択しない場合は、dp[n][m] = dp[n-1][m]
↓(ACするまでに苦戦したポイント)
・初期値設定が色々おかしい

<+苦戦ポイント>
・dpの初期値及び添字(範囲)は試行錯誤が要必要!
・dp配列は(N+1)(M+1)にして1-indexにした方が解きやすいかも!
"""
#--------------------------------------------------------------
N,M = MAP()
A = LIST()
#DP[i番目の要素を][m番目に選択した時]の最大値
dp = [[-INF]*(M+1) for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = 0 #i番目の要素をm番目に選択した時の最大値

for m in range(1,M+1):
    for n in range(1,N+1):
        dp[n][m] = max(dp[n-1][m],dp[n-1][m-1]+A[n-1]*(m))
ans = -INF
for i in range(1,N+1):
    ans = max(ans,dp[i][M])
print(ans)



