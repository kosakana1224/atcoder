import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
INF = float('inf')
import random
import math
import time
import copy
#dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
mod = 10**9+7
#mod = 998244353
#random.seed(314)

#--------------------------------------------------------------
"""

"""
#--------------------------------------------------------------
start_time = time.perf_counter()
tiles = [list(input()) for _ in range(30)]
first_tiles = copy.deepcopy(tiles)
ans = ''
to = [
    [1, 0, -1, -1],
    [3, -1, -1, 0],
    [-1, -1, 3, 2],
    [-1, 2, 1, -1],
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [2, -1, 0, -1],
    [-1, 3, -1, 1],
]
di = [0,-1,0,1]
dj = [-1,0,1,0]
#(si, sj) のタイルにsd方向のタイルから侵入した状態からスタートして環状線の長さを求める
def scoring(si,sj,sd):
    i = si
    j = sj
    d = sd
    length = 0
    while(1):
        d2 = to[int(tiles[i][j])][d]
        if (d2 == -1): 
            return 0
        i += di[d2]
        j += dj[d2]
        if (i < 0 or i >= 30 or j < 0 or j >= 30):
            return 0
        d = (d2 + 2) % 4
        length += 1
        if (i == si and j == sj and d == sd):
            return length

def all_score():
    now_score = 0
    for y in range(30):
        for x in range(30):
            for k in range(4):
                if scoring(y,x,k)!=None:
                    now_score = max(now_score,scoring(y,x,k))
    return now_score
def change(tiles):
    for _ in range(5):
        idx_y,idx_x = random.randint(5,25),random.randint(5,25)
        if (tiles[idx_y][idx_x]) == '7':
            tiles[idx_y][idx_x] = str(6)
        elif tiles[idx_y][idx_x] == '6':
            tiles[idx_y][idx_x] = str(7)
        elif 0<=int(tiles[idx_y][idx_x])<4: 
            tiles[idx_y][idx_x] = str(random.randint(0,3))
        else:
            tiles[idx_y][idx_x] = str(random.randint(4,5))
    return tiles

score = all_score()
end_time = time.perf_counter()
now_time = end_time - start_time
while now_time < 1.8:
    start_time = time.perf_counter()
    new_tiles = change(tiles)
    new_score = all_score()
    if new_score > score:
        tiles = new_tiles
        score = new_score
    end_time = time.perf_counter()
    now_time += (end_time - start_time)

ans = ''
for y in range(30):
    for x in range(30):
        if first_tiles[y][x]==tiles[y][x]:
            ans += '0'
        elif first_tiles[y][x]=='7' and tiles[y][x]=='6':
            ans += '1'
        elif first_tiles[y][x]=='6' and tiles[y][x]=='7':
            ans += '1'
        elif first_tiles[y][x]=='5' and tiles[y][x]=='4':
            ans += '1'
        elif first_tiles[y][x]=='4' and tiles[y][x]=='5':
            ans += '1'
        elif first_tiles[y][x]=='3' and tiles[y][x]=='2':
            ans += '3'
        elif first_tiles[y][x]=='3' and tiles[y][x]=='1':
            ans += '2'
        elif first_tiles[y][x]=='3' and tiles[y][x]=='0':
            ans += '1'  
        elif first_tiles[y][x]=='2' and tiles[y][x]=='1':
            ans += '3'
        elif first_tiles[y][x]=='2' and tiles[y][x]=='0':
            ans += '2'
        elif first_tiles[y][x]=='2' and tiles[y][x]=='3':
            ans += '1'   
        elif first_tiles[y][x]=='1' and tiles[y][x]=='0':
            ans += '3'
        elif first_tiles[y][x]=='1' and tiles[y][x]=='3':
            ans += '2'
        elif first_tiles[y][x]=='1' and tiles[y][x]=='2':
            ans += '1' 
        elif first_tiles[y][x]=='0' and tiles[y][x]=='1':
            ans += '1'
        elif first_tiles[y][x]=='0' and tiles[y][x]=='2':
            ans += '2'
        elif first_tiles[y][x]=='0' and tiles[y][x]=='3':
            ans += '3'   
print(ans)
        






