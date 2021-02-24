i, j=1, 7
while i<=9:
    print(f"I={i} J={j}")
    if j==i+4:
        j=j+4
        i+=2
    else:
        j -= 1