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
2 1
1 1
0 1
1 0
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・循環セールスマン問題っぽい
N個の街は全て通る+M個の宝箱を取るかもしれないので最大でN+M=17の階乗
->これはこれはいわゆるbitDP

<キーワード>
bitDP
https://www.youtube.com/watch?v=Oc1JP9XmIsU
<ポイント>
わかりやすそうなの
https://atcoder.jp/contests/abc274/submissions/35963948

"""
#--------------------------------------------------------------
N,M = MAP()
XY = [LIST() for _ in range(N+M)]
def f(i,j):
    return math.sqrt((XY[i][0]-XY[j][0])**2+(XY[i][1]-XY[j][1])**2)
#mの個数をそれぞれの場合で調べる
ans = INF
for m in range(M+1):
    dp = [[INF]*(N+m) for _ in range(2**(N+m))]
    dp[0][0] = 0
    for S in range(2**(N+m)):
        for v in range(N+m):
            if (S>>v & 1) == 0 and S!=0:#S=0の場合は例外?
                continue
            for u in range(N+m):
                if (S>>u & 1)==0:
                    dp[S|(1<<u)][u] = min(dp[S|(1<<u)][u],dp[S][v]+f(v,u))
    ans = min(ans,dp[2**(N+m)-1][0])
    print(dp[2**(N+m)-1][0])
print(ans)






