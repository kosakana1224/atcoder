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
5
19 0 42 169 389
7
1 3
0 198344926 34802
0 30067915 69027
1 100000
0 0 2678
1 20493
1 905
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・愚直にやると制約オーバになるので情報圧縮が必要!
・連続データとして二次元配列をdequeで持つ定番のやーつ

<ポイント>
・要素数sizeを毎回管理するともっと楽に実装できるかも
・Aはrleしなくてもよかったかも
"""
#--------------------------------------------------------------
def rle(s): #ランレングス圧縮したときの数値部分のリストを返す
    n = len(s)
    block = []
    num = 0
    for i in range(n):
        num += 1
        if i < n-1 and s[i] != s[i+1]:
            block.append((s[i],num))
            num = 0
    else:
        block.append((s[n-1],num))
    return block

N = INT()
A = LIST()
que = deque(rle(A))
Q = INT()
for _ in range(Q):
    query = LIST()
    if query[0]==0:
        v,k = query[1],query[2]
        if len(que)!=0:
            a,cnt = que.pop()
            if a==v:
                que.append((a,cnt+k))
            else:
                que.append((a,cnt))
                que.append((v,k)) 
        else:
            que.append((a,cnt))
            que.append((v,k))
    else:
        k = query[1]
        ksum = 0
        cnt = 0
        rm = []
        flag = False
        while True:
            if len(que)==0:
                flag = True
                break
            a,t = que.pop()
            rm.append((a,t))
            cnt += t
            if cnt==k:
                ksum += a*t
                break
            elif cnt>k:
                ksum += (t-(cnt-k))*a
                que.append((a,cnt-k))
                break
            else:
                ksum += a*t
        if flag:
            print("Error")
            rm.reverse()
            que.extend(rm)
        else:
            print(ksum)
                
                
                
    