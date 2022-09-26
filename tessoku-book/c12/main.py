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
6 4 3
3 4
3 5
2 5
1 6

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・制約は小さい
・アルゴリズム的なものは思いつかないのでまずは全探索を考えてみる
→工夫できそうだったらDPで計算量を改善する

・情報として知りたい値はどの区間に繋がりが何個あるか
→言い換えると重なりの問題のようにも感じられるのでいもす的に考えることができるのでは?
・普通に無理です

・３重ループまではできる
・区間について考えるので区間DPですか?

・dp[l][r][K]:区間l,rをK個の小説で分割するときの小説の良さの最大値

--うーんわからんfin
<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
N,M,K = MAP()
AB = [LIST() for _ in range(M)]
dp = []




    