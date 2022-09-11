import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate,permutations
from bisect import bisect_right,bisect_left 
import itertools
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
#--------------------------------------------------------------
_INPUT = """\
4 4
ab
cd
ef
gh
hoge
fuga
____
_ab_cd_ef_gh_













"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・N-1ヶ所-を入れる場所がある
最大16個までなので、(16-N)個をN-1ヶ所に割り当てる必要がある

8!=4*10**4
<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
import random
N,M = MAP()
X = ""
S = []
slen = 0
for _ in range(N):
    s = input()
    S.append(s)
    slen += len(s)
d = defaultdict(int)
for _ in range(M):
    t = input()
    d[t] += 1
cnt = 0
while True:
    for seq in permutations(S):
        X = []
        for i in range(N):
            cnt += 1
            X.append(seq[i])
            if i!=N-1:
                X.append("_"*random.randint(1,5))
        X = "".join(X)
        if 3<=len(X)<=16 and d[X]==0:
            print(X)
            exit()
    if cnt==5*10**6:
        break
print(-1)
    
    