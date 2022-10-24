import io,sys
#--------------------------------------------------------------
_INPUT = """\
6
1 12 23 34 45 67




"""
sys.stdin = io.StringIO(_INPUT)
N = int(input())
b = list(map(int,input().split()))
b.sort()
tousa = (b[-1]-b[0])//N
now = b[0]
for i in range(N):
    if b[i]!=now:
        print(now)
        break
    else:
        now += tousa


