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
0 0

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
A,B = MAP()
if A==0:
    toketaA = [0]
    
elif A==1:
    toketaA = [1]
elif A==2:
    toketaA = [2]
elif A==3:
    toketaA = [1,2]
elif A==4:
    toketaA = [4]
elif A==5:
    toketaA = [1,4]
elif A==6:
    toketaA = [2,4]
else:
    toketaA = [1,2,4]
    
if B==1:
    toketaB = [1]
elif B==0:
    toketaB = [0]
elif B==2:
    toketaB = [2]
elif B==3:
    toketaB = [1,2]
elif B==4:
    toketaB = [4]
elif B==5:
    toketaB = [1,4]
elif B==6:
    toketaB = [2,4]
else:
    toketaB = [1,2,4]

toketaA = set(toketaA)
toketaB = set(toketaB)
c = toketaA | toketaB
print()
ans = sum(c)
print(ans)

