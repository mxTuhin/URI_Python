a, b, c, d=0, 0, 0, 0
for i in range(0,5):
    num=float(input())
    if num%2==0:
        a+=1
    else:
        b+=1
    if num>0:
        c+=1
    elif num<0:
        d+=1
print(f"{a} valor(es) par(es)")
print(f"{b} valor(es) impar(es)")
print(f"{c} valor(es) positivo(s)")
print(f"{d} valor(es) negativo(s)")