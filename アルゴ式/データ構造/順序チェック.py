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
3
2 1 3
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
aiはNよりも大きい可能性を考慮する必要がある!
→超えたらスキップするか、制約いっぱいの配列を作って調べる時はNまでのどちらか。

別解としてソートしてそれぞれ==iになるかを調べる方法もあり。

"""
#--------------------------------------------------------------
N = INT()
A = LIST()
dic = [0]*N
for a in A:
    a -= 1
    if a>=N:
        continue
    dic[a] += 1
flag = True
for i in range(N):
    if dic[i]!=1:
        flag = False
if flag:
    print("Yes")
else:
    print("No")
