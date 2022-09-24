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

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
def yakusu(N):
    # 答えを表す集合
    res = []
    # 各整数 i が N の約数かどうかを調べる
    for i in range(1, N + 1):
        # √N で打ち切り
        if i * i > N:
            break
        # i が N の約数でない場合はスキップ
        if N % i != 0:
            continue
        # i は約数である
        res.append(i)
        # N ÷ i も約数である (重複に注意)
        if N // i != i:
            res.append(N // i)
    # 約数を小さい順に並び替えて出力
    res.sort()
    return res

N = INT()
ans = yakusu(N)
for a in ans:
    print(a)