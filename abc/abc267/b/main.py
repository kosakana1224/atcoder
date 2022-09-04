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
0111111111

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
S = input()
S = "o"+S
if S[1]!="0":
    print("No") 
else:
    retu = [[7],[4],[8,2],[5,1],[9,3],[6],[10]]
    for idx,re in enumerate(retu):
        #print(f"idx{idx}")
        if idx==0 or idx==len(retu)-1:
            continue
        flag = True #列が全て倒れてたらTrue
        for a in re:
            if S[a]=="1":
                flag = False
        left = False #左に立っているピンが一本以上存在したらTrue
        for i in range(idx):
            #print(f"left:{i}")
            for a in retu[i]:
                if S[a]=="1":
                    left = True
        right = False
        for i in range(idx+1,len(retu)):
            #print(f"right:{i}")
            for a in retu[i]:
                if S[a]=="1":
                    right = True
        if flag and right and left:
            print("Yes")
            exit()
    print("No")
                
            