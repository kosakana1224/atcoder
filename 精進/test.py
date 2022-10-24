import io
import sys
from pprint import pprint
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
mod = 998244353
"""
#-



N = int(input())
AB = [LIST() for _ in range(N)]
ans = 0
for bit in product([0,1],repeat=N):
    print(bit)
    takahashi = 0
    aoki = 0
    for idx,i in enumerate(bit):
        if i==0:
            takahashi += AB[idx][0]
            aoki += 
        else:
            aoki += AB[idx][1]
            takahashi += AB[idx][1]
    if takahashi == aoki:
        ans += 1
        ans %= mod
print(ans%mod)
"""

A = [1,5,3]
for idx,a in enumerate(A):
    print(idx,a)

pprint(A)


