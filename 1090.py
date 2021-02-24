n=int(input())
total, rabbit, rat, frog=0, 0, 0, 0;
for i in range(0, n):
    a, b=list(map(str, input().split()))
    a=int(a)
    total+=a
    if b=="C":
        rabbit+=a
    elif b=="R":
        rat+=a
    elif b=="S":
        frog+=a

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {rabbit}\n"
      f"Total de ratos: {rat}\n"
      f"Total de sapos: {frog}\n"
      f"Percentual de coelhos: {(rabbit/total)*100:.2f} %\n"
      f"Percentual de ratos: {(rat/total)*100:.2f} %\n"
      f"Percentual de sapos: {(frog/total)*100:.2f} %")