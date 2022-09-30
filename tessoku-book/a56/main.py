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
mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
7 3
abcbabc
1 3 5 7
1 5 2 6
1 2 6 7

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>

<キーワード>
・ローリングハッシュ

<ポイント>
・ローリングハッシュをお借りしました
https://tjkendev.github.io/procon-library/python/string/rolling_hash.html
・1-indexですか?
"""
#--------------------------------------------------------------
class RollingHash():
    def __init__(self, s, base, mod):
        self.mod = mod
        self.pw = pw = [1]*(len(s)+1)
        self.length = l = len(s)
        self.h = h = [0]*(l+1)
 
        v = 0
        for i in range(l): h[i+1] = v = (v * base + ord(s[i])) % mod
        v = 1
        for i in range(l): pw[i+1] = v = v * base % mod
 
    def get(self, l, r):
        # 閉区間[l,r]
        return (self.h[r] - self.h[l-1] * self.pw[r-l+1]) % self.mod
    
    def all(self):
        return self.get(0, self.length)
    
N,Q = MAP()
S = input()
RH = RollingHash(S,37,(1<<61)-1)
for _ in range(Q):
    a,b,c,d = MAP()
    if RH.get(a,b)==RH.get(c,d):
        print("Yes")
    else:
        print("No")
    