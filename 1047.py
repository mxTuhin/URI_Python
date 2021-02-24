inHour, inMin, finHour, finMin = list(map(int, input().split()))

timeDif = ((finHour * 60) + finMin) - ((inHour * 60) + inMin)
if timeDif <= 0:
    timeDif += 24 * 60

hour = timeDif // 60
min = timeDif % 60

print(f"O JOGO DUROU {hour} HORA(S) E {min} MINUTO(S)")
