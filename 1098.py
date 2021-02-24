i, j = 0, 1
while i <= 2:
    for t in range(3):
        if i>=1.9 or i<=0 or i==1:
            print(f"I={i:.0f} J={j:.0f}")
        else:
            print(f"I={i:.1f} J={j:.1f}")
        j += 1
    i += 0.2
    j=1+i
