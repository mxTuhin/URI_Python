salary=float(input())
readjustRate=0

if salary>0 and salary<=400:
    readjustRate=15
elif salary<=800:
    readjustRate=12
elif salary<=1200:
    readjustRate=10
elif salary<=2000:
    readjustRate=7
elif salary>2000:
    readjustRate=4

newSalary = salary+(salary*(readjustRate/100))
print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {} %".format(newSalary, newSalary-salary, readjustRate))