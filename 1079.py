n = int(input())
for i in range(0, n):
    a, b, c = list(map(float, input().split()))
    avg= ((a*2) + (b*3) + (c*5)) / 10
    print(f"{avg:.1f}")