max=0
index=None
for i in range(0, 100):
    n=int(input())
    if(n>max):
        max=n
        index = i

print(max)
print(index+1)