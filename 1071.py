X=int(input())
Y=int(input())
sum=0

if X==Y:
    print(0)
if X<Y:
    for i in range (X+1, Y):
        if i%2==1:
            sum+=i
    print(sum)
elif X>Y:
    for i in range(Y+1, X):
        if i%2==1:
            sum+=i
    print(sum)

