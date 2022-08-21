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
使いカードの条件は大きい３枚であっているが、並べる順番は大きい整数をそのまま
並べるとは限らない

"""
#--------------------------------------------------------------
N = INT()
A = LIST()
A.sort(reverse=True)
ans = []
ans.append(int(str(A[0])+str(A[1])+str(A[2])))
ans.append(int(str(A[0])+str(A[2])+str(A[1])))
ans.append(int(str(A[1])+str(A[0])+str(A[2])))
ans.append(int(str(A[1])+str(A[2])+str(A[0])))
ans.append(int(str(A[2])+str(A[0])+str(A[1])))
ans.append(int(str(A[2])+str(A[1])+str(A[0])))
ans.sort(reverse=True)
print(ans[0])