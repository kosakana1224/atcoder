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
"""
<考察>

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
grid = [".....#..",
        "#.......",
        "....#...",
        ".#......",
        ".......#",
        "..#.....",
        "......#.",
        "........"]
grid2 = [".#",
         ".."]
def q(A,B,C,D):
    A,B,C,D = A-1,B-1,C-1,D-1
    cnt = 0
    for h in range(A,B+1):
        for w in range(C,D+1):
            if grid[h][w]=="#":
                cnt += 1
    return cnt
#めぐる式二分探索
def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    pass

def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok
N = 8
ngx = 1
okx = N
ngy = 1
oky = N
for _ in range(20):
    if not abs(ngx-okx)>1 and not abs(ngy-oky)>1:
        print(f"! {okx} {oky}")
        exit()
    elif abs(ngx-okx)>1 and not abs(ngy-oky)>1:
        mid = (ngx + okx)//2
        print(f"x? {1} {N} {ngx} {mid}")
        cnt = q(1,N,ngx,mid)
        print(cnt,mid-ngx+1)
        if mid-ngx+1==cnt:#1~midの間になかったら
            okx = mid
        else:
            ngx = mid
    elif not abs(ngx-okx)>1 and abs(ngy-oky)>1:
        mid = (ngy + oky)//2
        print(f"y? {ngy} {mid} {1} {N}")
        cnt = q(ngy,mid,1,N)
        if mid-ngy+1==cnt:#1~midの間になかったら
            oky = mid
        else:
            ngy = mid
    else:
        mid = (ngx + okx)//2
        print(f"x? {1} {N} {ngx} {mid}")
        cnt = q(1,N,ngx,mid)
        print(cnt,mid-ngx+1)
        if mid-ngx+1==cnt:#1~midの間になかったら
            okx = mid
        else:
            ngx = mid