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
#転倒数を高速に求めることができる関数
def tentousu(A):#A:list
    class Bit:
        def __init__(self, n):
            self.size = n
            self.tree = [0]*(n+1)
        def sum(self, i):
            # [0, i) の要素の総和を返す
            if not (0 <= i <= self.size): raise ValueError("error!")
            s = 0
            while i>0:
                s += self.tree[i]
                i -= i & -i
            return s
        def add(self, i, x):
            if not (0 <= i < self.size): raise ValueError("error!")
            i += 1
            while i <= self.size:
                self.tree[i] += x
                i += i & -i 
    bit = Bit(max(A)+1)
    ans = 0
    for i, a in enumerate(A):
        ans += i - bit.sum(a+1)
        bit.add(a, 1)
    return ans
N = INT()
A = LIST()
print(tentousu(A))

