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
4 5 10
2 5 12
1 5 12
2 3 15
1 2 20
1 1 28
2 4 26
3 2 27
4 5 21
3 5 10
1 3 10
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・拾うことができるアイテムの価値の合計の最大値
→ぱっと見DP(多次元)
・DP[R][C]:マス(R,C)でのアイテムの価値の合計の最大値
ただし、三個までしかアイテムを拾うことができないという制約がある
-通ったマスにアイテムがある場合に、そのアイテムを拾わないという選択もすることはできるらしい
・DP[i][R][C]:マス(R,C)でi回個アイテムを拾った時の、アイテムの価値の合計の最大値
・なんか全然合わない
↓
はいーーー問題誤読ーーーーーー
マス目の同じ行,横の列では、アイテムが3個までしか取れない
↓
・DP[i][R][C]:マス(R,C)でR行におけるアイテムを拾った回数がi回の時の、アイテムの価値の合計の最大値
↓
うまく遷移をごちゃごちゃしてなんとかサンプルは全てAC!
↓
TLEぴえん
R*C*4 = 3000*3000*4=3.6*10^7でアウト?
実際には、最大をとるときに最大要素数5個を比較しているので1.8*10^8となり、これは確実に3secでもTLE
↓
やっぱり3次元配列まで行っちゃうと速度遅くなる???
一旦次元圧縮してみる(もしかしたら計算量を改善することができるかも)

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
R,C,K = MAP()
grid = [[0]*C for _ in range(R)]
for _ in range(K):
    r,c,v = MAP()
    r,c = r-1,c-1
    grid[r][c] = v
dp = [[[0]*C for _ in range(R)] for _ in range(4)]
dp[1][0][0] = grid[0][0]
dp[2][0][0] = grid[0][0]
dp[3][0][0] = grid[0][0]
for r in range(R):
    for c in range(C):
        for i in range(4):
            if r==R-1 and c==C-1:
                continue
            elif r==R-1:#一番下の時
                dp[i][r][c+1] = max(dp[i][r][c],dp[i][r][c+1])
                if i!=3:
                    dp[i+1][r][c+1] = max(dp[i][r][c]+grid[r][c+1],dp[i+1][r][c+1])
            elif c==C-1:#一番右の時
                dp[i][r+1][c] = max(dp[i][r+1][c],dp[0][r][c],dp[1][r][c],dp[2][r][c],dp[3][r][c])
                if i!=3:
                    dp[1][r+1][c] = max(max(dp[0][r][c],dp[1][r][c],dp[2][r][c],dp[3][r][c])+grid[r+1][c],dp[1][r+1][c])
            else:
                dp[i][r+1][c] = max(dp[i][r+1][c],dp[0][r][c],dp[1][r][c],dp[2][r][c],dp[3][r][c])
                dp[i][r][c+1] = max(dp[i][r][c],dp[i][r][c+1])
                if i!=3:
                    dp[i+1][r][c+1] = max(dp[i][r][c]+grid[r][c+1],dp[i+1][r][c+1])
                    dp[1][r+1][c] = max(max(dp[0][r][c],dp[1][r][c],dp[2][r][c],dp[3][r][c])+grid[r+1][c],dp[1][r+1][c])
ans = 0
for i in range(4):  
    ans = max(ans,dp[i][R-1][C-1])
print(ans)
    
