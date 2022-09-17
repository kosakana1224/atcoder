N,K = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))
C = set(map(int,input().split()))
D = set(map(int,input().split()))
E = set()
F = set()
for a in A:
    for b in B:
        E.add(a+b)
for c in C:
    for d in D:
        F.add(c+d)
flag = False
for e in E:
    if K-e in F:
        flag = True
if flag:
    print("Yes")
else:
    print("No")