from collections import deque

n = int(input())
q = deque()
qt = deque()
result = []
koof1 = 0
koof2 = 0

for i in range(n):
    t1 = input().split()
    if  "-" in t1:
        result.append(q.popleft())
        koof1 -= 1
    elif  '+' in t1:
        qt.append(t1[-1])
        koof2 += 1
    else :
        qt.appendleft(t1[-1])
        koof2 += 1
    if koof1 < koof2:
        q.append(qt.popleft())
        koof2 -= 1
        koof1 += 1   
print(*result, sep='\n')