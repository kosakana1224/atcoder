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
3 3
1 2 3
2 4 5
1 2 3
2 3
1 2 3
1 2 3
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
3 5


"""
#--------------------------------------------------------------
H1,W1 = MAP()
A = [LIST() for _ in range(H1)]
H2,W2 = MAP()
B = [LIST() for _ in range(H2)]
info = [[[-1,-1]]*W2 for _ in range(H2)]
for h in range(H2):
    for w in range(W2):
        for y in range(H1):
            for x in range(W1):
                if B[h][w]==A[y][x]:
                    if info[h][w]==[-1,-1]:
                        info[h][w]=[]
                        info[h][w].append([y,x])
                    else:
                        info[h][w].append([y,x])
flag = True
for h in range(H2):
    for w in range(W2):
        if info[h][w]==[-1,-1]:
            flag = False
        print(info[h][w],end=" ")
    print()
if flag==False:
    print("No")
    exit()
else:
    for h in range(H2):
        cnt = 0
        start = None
        tmp_flag = True
        for w in range(W2):
            if cnt==0:
                start = info[h][w][0]
            else:
                if start != info[h][w][0]:
                    tmp_flag = False
            cnt += 1
        if tmp_flag == False:
            flag = False
            
    for w in range(W2):
        cnt = 0
        start = None
        tmp_flag = True
        for h in range(H2):
            if cnt==0:
                start = info[h][w][1]
            else:
                if start != info[h][w][1]:
                    tmp_flag = False
            cnt += 1
        if tmp_flag == False:
            flag = False
            
    cflag = False
    for h in range(H2):
        for w in range(W2):
            
   
if flag:
    print("Yes")
else:
    print("No")     

    
        
        
                
    
            
