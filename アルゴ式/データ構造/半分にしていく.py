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
dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
4 1
6 7 5 3
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
pythonのヒープは自作クラス使うと楽ですよ!

"""
#--------------------------------------------------------------
import heapq
class Heapq:
    #最大値を取り出したいときは、desc=Trueにする
    def __init__(self, arr, desc=True):
        if desc:
            arr = [-a for a in arr]
        self.sign = -1 if desc else 1
        self.hq = arr
        heapq.heapify(self.hq)
    #最大or最小を取り出す
    def pop(self):
        return heapq.heappop(self.hq) * self.sign
    #値を追加する
    def push(self, a):
        heapq.heappush(self.hq, a * self.sign)
    #最大or最小を参照するだけ(なくならない)
    def top(self):
        return self.hq[0] * self.sign
    
N,K = MAP()
A = LIST()
hq = Heapq(A)
for _ in range(K):
    amax = hq.pop()
    amax //= 2
    hq.push(amax)
ans = 0
for _ in range(N):
    ans += hq.pop()
print(ans)