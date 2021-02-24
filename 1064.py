counter=0
sum=0
for i in range(0,6):
    num=float(input())
    if num>0:
        counter+=1
        sum+=num
print(f"{counter} valores positivos")
print(f"{sum/counter:.1f}")