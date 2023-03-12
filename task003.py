# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

bilet = input('Введите шестизначный номер билета: ')

if len(bilet) != 6:
    print('Вы ввели некорректное число')
else:
    sum1 = int(bilet[0]) + int(bilet[1]) + int(bilet[2])
    sum2 = int(bilet[3]) + int(bilet[4]) + int(bilet[5])
    if sum1 == sum2:
        print("Билет счастливый")
    else:
        print('Билет не счастливый ')
