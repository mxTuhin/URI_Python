_in, inDay = list(map(str, input().split()))
inHour, inMin, inSec = list(map(int, input().split(":")))
_fin, finDay=list(map(str, input().split()))
finHour, finMin, finSec = list(map(int, input().split(":")))

diff= ((int(finDay)*86400)+(finHour*3600)+(finMin*60)+finSec) - ((int(inDay)*86400)+(inHour*3600)+(inMin*60)+inSec)

if(diff<=0):
    diff += 24 * 3600

day=diff//86400
diff=diff%86400
hour=diff//3600
diff=diff%3600
min=diff//60
diff=diff%60
sec=diff%60
print(f"{day} dia(s)")
print(f"{hour} hora(s)")
print(f"{min} minuto(s)")
print(f"{sec} segundo(s)")
