N = int(input())
P = list(map(int, input().split()))

time = 0
P.sort()

for n in range(N):
    cnt = 0
    for i in range(n+1):
        cnt += P[i]
    time += cnt

print(time)