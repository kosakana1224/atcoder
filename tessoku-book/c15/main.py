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
5
0
0 4
1 2
3 7
5 9
7 8

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・dp[i]:i秒時点で出席できる会議の最大値
・区間スケジューリング問題の応用みたみたいなやつ?

問題の問いに答えるならdp[i]:i番目の会議に出席しなければならない時の最大の会議出席数
・一つの問いだけだったら、答えることができる?
↓
お手上げですわ~

<キーワード>
・問題を分割して考える
・区間スケジューリング
・前計算することにより計算量改善

<ポイント>
・答え=i番目の会議の開始時刻以前での最大の会議の出席回数+1+i番目の会議の終了時刻以降の最大の
会議の出席回数
・二つの出席する会議の間にはK秒以降空ける必要がある->終了時刻に+Kするだけで解消することができる

"""
#--------------------------------------------------------------
N = INT()
K = INT()
LR = []
for _ in range(N):
    l,r = MAP()
    LR.append((l,r+K))
LRsorted = sorted(LR,key=lambda x:x[1])
meeting_cnt = [0]*87000

now = 0
for l,r in LRsorted:
    if r>=now:
        now = r
        meeting_cnt[l] += 1
        meeting_cnt[r+1] -= 1
for i in range(86500):
    meeting_cnt[i+1] += meeting_cnt[i]

for i in range(86500):
    meeting_cnt[i+1] += meeting_cnt[i]



print(f"last:{meeting_cnt[LRsorted[-1][1]]}")


for i in range(N):
    start = LR[i][0]
    goal = LR[i][1]
    if i==0:
        print(1+meeting_cnt[86400]-meeting_cnt[goal])
    elif i==N-1:
        print(1+meeting_cnt[start]-meeting_cnt[0])
    else:
        print(1+meeting_cnt[start]-meeting_cnt[0]+meeting_cnt[86400]-meeting_cnt[goal])

    
