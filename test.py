import sys

n = int(sys.stdin.readline().strip())
x = []
y = []
for i in range(n): 
    u = list(map(str,sys.stdin.readline().strip().split(' ')))
    x.append(round(float(u[0]),6))
    y.append(round(float(u[1]),6))
