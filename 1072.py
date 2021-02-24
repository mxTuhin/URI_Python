n=int(input())
inCounter, outCounter=0, 0
for i in range(0, n):
    a=int(input())
    if a>=10 and a<=20:
        inCounter+=1
    else:
        outCounter+=1

print(f"{inCounter} in")
print(f"{outCounter} out")
