# Найдите сумму трёхзначного числа

number = input("Введите трехзначное число: ")
#Проверка ввода по длинне
print(number)
if len(number) > 3:
    print("Вы ввели не трехзначное число, попробуйте ещё раз")
elif len(number) <= 2:
    print("Вы ввели не трехзначное число, попробуйте ещё раз")
else:
    # Вытаскиваем число под первым индексом и переводим его в int
    fitrst_number = int(number[0])
    # Вытаскиваем число под сторм индексом и переводим его в int
    second_number = int(number[1])
    # Вытаскиваем число под третьим индексом и переводим его в int
    third_number = int(number[2])
    #Находим их сумму
    sum_of_numbers = fitrst_number + second_number + third_number
    #Выводим сумму на экран
    print('Сумма всех чисел в числе = ', sum_of_numbers)
