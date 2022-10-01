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
5
1 3 5 10 3



"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・同じやつあったら後に持って行った方が良い

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
N = INT()
a = LIST()
a.sort()
que = deque(a)
que2 = deque()
que3 = deque()
s = set()
for i in que:
    if i not in s:
        s.add(i)
        que2.append(i)
    else:
        que3.append(i)
que4 = que2 + que3

cnt = 0
while que4:
    now = que4.popleft()
    if now!=cnt+1:
        que4.appendleft(now)
        if len(que4)==1:
            break
        que4.pop()
        que4.pop()
        cnt += 1
    else:
        cnt += 1
print(cnt)




