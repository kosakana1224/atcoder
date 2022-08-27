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
1 0
1 1
0 1




"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""

"""
#--------------------------------------------------------------
import numpy as np
Ax,Ay = MAP()
Bx,By = MAP()
Cx,Cy = MAP()
Dx,Dy = MAP()

A = 0
B = 0
C = 0
D = 0
#２次元空間の場合
def f(x0,y0,x1,y1,x2,y2):
    #角度の中心位置
    x0,y0=0,0
    #方向指定1
    x1,y1=90,0
    #方向指定2
    x2,y2=0,90
    #角度計算開始
    vec1=[x1-x0,y1-y0]
    vec2=[x2-x0,y2-y0]
    absvec1=np.linalg.norm(vec1)
    absvec2=np.linalg.norm(vec2)
    inner=np.inner(vec1,vec2)
    cos_theta=inner/(absvec1*absvec2)
    theta=math.degrees(math.acos(cos_theta))
    return theta

def S(Px,Py,Cx,Cy,Qx,Qy):
    return (Px - Cx) * (Qy - Cy) - (Py - Cy) * (Qx - Cx)

A = f(Ax,Ay,Dx,Dy,Bx,By)
BS = S(Ax,Ay,Bx,By,Cx,Cy)
B = f(Bx,By,Ax,Ay,Cx,Cy)
CS = S(Bx,By,Cx,Cy,Dx,Dy)
C = f(Cx,Cy,Bx,By,Dx,Dy)
DS = S(Cx,Cy,Dx,Dy,Ax,Ay)
D = f(Dx,Dy,Cx,Cy,Ax,Ay)
AS = S(Dx,Dy,Ax,Ay,Bx,By)
if AS>0:
    A = 360 - A
if BS>0:
    B = 360 - B
if CS>0:
    C = 360 - C
if DS>0:
    D = 360 - D
if A<180 and B<180 and C<180 and D<180:
    print("Yes")
else:
    print("No")