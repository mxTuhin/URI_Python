salary=float(input())

if salary>0 and salary<=2000:
    print("Isento")
elif salary>2000 and salary<=3000:
    tax=(salary-2000)*(8/100)
    print(f"R$ {tax:.2f}")
elif salary>3000 and salary<=4500:
    tax=((salary-3000)*(18/100))+(1000*(8/100))
    print(f"R$ {tax:.2f}")
elif salary>4500:
    tax=((salary-4500)*(28/100))+(1500*(18/100))+(1000*(8/100))
    print(f"R$ {tax:.2f}")