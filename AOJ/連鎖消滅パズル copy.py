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
1
6 9 9 9 9
5
5 9 5 5 9
5 5 6 9 9
4 6 3 6 9
3 3 2 9 9
2 2 1 1 1
10
3 5 6 5 6
2 2 2 8 3
6 2 5 9 2
7 7 7 6 1
4 6 6 4 9
8 9 1 1 8
5 6 1 8 1
6 8 2 1 2
9 6 3 3 5
5 3 8 8 8
5
1 2 3 4 5
6 7 8 9 1
2 3 4 5 6
7 8 9 1 2
3 4 5 6 7
3
2 2 8 7 4
6 5 7 7 7
8 8 9 9 9
0

"""
#--------------------------------------------------------------
"""
<考察>
制約W=5,H=0~10(0のとき処理終了)
ブヨブヨと異なり、今回は水平に3個以上並んだときのみ、消す
数字は1~9まで、空白は-1で表現するとする.

実装鬼だるくて笑う
おちものパズルのアルゴリズムの勉強も時間あったらあったらやる

<キーワード>

<ポイント>
"""
#--------------------------------------------------------------
while True:
    H = INT()
    if H==0:
        exit()
    else:
        grid = [LIST() for _ in range(H)]
        def debug():
            for h in range(H):
                for w in range(5):
                    print(grid[h][w],end=" ")
                print()
        ans = 0
        cnt = 0
        while True:
            cnt += 1
            for h in range(H)[::-1]:
                for w in range(5-2):#4~以降はみる必要がない
                    now = grid[h][w]
                    if now == -1:
                        continue
                    flag = True #3つ以上連続するかどうか
                    rencnt = 1
                    for dw in range(1,5-w):
                        if now != grid[h][w+dw]:
                            break
                        else:
                            rencnt += 1
                    if rencnt<3: flag = False
                    #空白の判定作成部分
                    if flag:
                        all_flag = False
                        now = grid[h][w]
                        cnt = 0
                        for dw in range(0,5-w):
                            if now!=grid[h][w+dw]:
                                break
                            cnt += 1
                            grid[h][w+dw] = -1
                        ans += now*cnt
                        break #これ以上、この列で石が消えることはないので打ち切る
            #print(grid)
            #石を落とす操作を書く
            #空白が連続する場合の処理が足りない(now)
            #今の石からその上に空白ある個数だけ石を上からずらしていく(-1にあたったら終わり)
            if H!=1:
                for h in range(1,H)[::-1]:
                    for w in range(5):
                        if grid[h][w]==-1:
                            now = h-1#一個上のマスから見る
                            kuhakuCnt = 1
                            while grid[now][w]==-1:
                                if now==0:
                                    break
                                now -= 1
                            if now>=0:
                                grid[h][w] = grid[now][w]
                                grid[now][w] = -1
                            else:
                                grid[h][w] = -1
            #終了判定
            #消すマスが-1しかないときかつ数字があるマスが1行だけだったらTrue
            if H==1:
                break
            if cnt == H+5:#大きめに見る
                break
        print(ans)
        #debug()
            
        
