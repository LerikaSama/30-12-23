#Задание 1
#start = int(input("Введите начало диапазона: "))
#end = int(input("Введите конец диапазона: "))

#chet_sum = 0
#nechet_sum = 0
#kr9_sum = 0

#for num in range(start, end + 1):
#   if num % 2 == 0:
#       chet_sum += num
#   else:
#       nechet_sum += num
#   if num % 9 == 0:
#       kr9_sum += num

#print(f"Сумма четных чисел в диапазоне от {start} до {end} равна {chet_sum}")
#print(f"Сумма нечетных чисел в диапазоне от {start} до {end} равна {nechet_sum}")
#print(f"Сумма чисел, кратных 9, в диапазоне от {start} до {end} равна {kr9_sum}")


#Задание 2

#lin = int(input("Введите длину линии: "))
#simvol = input("Введите символ, чтобы заполнить строку: ")

#or i in range(lin):
#    print(simvol)


#Задание 3


#while True:

#   number = int(input("Введите число для проверки"))

#   if number > 0:
#       print('Number is positive')

#   elif number < 0:
#       print('Number is negative')

#   else:
#       print('Number is equal to zero')

#   if number == 7:
#       print('Good bye!')

#       exit()


#Задание 4


a = 0
a_max = 0
a_min = 0

while (True):
    b = int(input("Введите числа (или 7 для завершения):"))
    if b == 7:
        print("Good bye!")
        break
    elif b > a_max:
        a_max = a
        a = a + b
    elif b < a_min:
        a_min = b

print("Сумма введенных чисел равна ", a)
print("Максиммальное из введенных чисел это - ", a_max)
print("Минимальное из введеных чисел это - ", a_min)
