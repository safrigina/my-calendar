import calendar
print("Узнаем день недели и число дней в месяце")
days=["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]
year=int(input("Введите год: "))
month=int(input("Введите месяц: "))
result = calendar.monthrange(year,month)
short=["Пн","Вт","Ср","Чт","Пт","Сб","Вс"]
for d in short:
    print(d,end=" ")
print()
cell=0
while cell<result[0]:
    print("  ",end=" ")
    cell+=1
for day in range(1,result[1]+1):
    print(f"{day:2}", end=" ")
    cell += 1
    if cell == 7:
        print()
        cell = 0
print()
print("В",year,"году было",result[1],"Первый день месяца:",days[result[0]])