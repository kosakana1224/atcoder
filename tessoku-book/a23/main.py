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
・クーポン券の買い方をbit全探索すると2^100最大でかかってしまう

<キーワード>
・bitDPの出番
-集合の推移を考える時に使う
-集合を管理するときは、2進数⇄10進数でbitを立てて考える
-n個の要素の順列 (n!通りあります) としてありうるものの中から,
最適なものを求めたい場面でしばしば使えるテクニック

<ポイント>
・dp[m][S]:m番目までのクーポン券を選択した時,状態が{S}である時の最小のクーポン数
の手数

"""
#--------------------------------------------------------------
N,M = MAP()
A = [LIST() for _ in range(M)]
dp = [[INF]*(M+1) for _ in range(2**N+1)]
dp[0][0] = 0
for m in range(1,M+1):
    for i in range(2**N+1):
        pass
print(dp[M][2**N])

