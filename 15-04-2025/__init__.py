# begin=int(input("num1: "))
# end=int(input("num2: "))
# if begin>end: begin, end = end, begin
# while begin<=end:
#     if begin%4==0:
#         print(begin)
#         begin+=4
#     else:
# вывести числа, которые кратны 4

# n=int(input())
# counter=0
# while counter<=n:
#     print(counter)
#     counter+=1
# вывод всех чисел в диапазоне от 0 до n


# for i in range(0, 10, 1):
#     print(i, end=" ")
# запись вверху и внизу идентичны
# i=0
# while i<10:
#     print(i, end=" ")
#     i+=1


# a=int(input("num1: "))
# b=int(input("num2: "))
# if a>b: a,b=b,a
# for i in range (b, a-1, -1):
#     print(i, end=" ")
# вывести все целые числа в диапазоне от а до б в порядке убывания


# a=int(input("num1: "))
# b=int(input("num2: "))
# if a>b: a,b=b,a
# if a%2: a+=1
# for i in range (a, b+1, 2):
#     print(i, end=" ")


# a=int(input("num1: "))
# b=int(input("num2: "))
# if a>b:
#      a,b=b,a
# sum = 0
# for i in range (a, b+1, 1):
#     sum+=i
# print(sum)
# вывести сумму всех целых чисел в диапазоне от а до б


# a=int(input("num: "))
# sum=0
# while a:
#       sum+=a%10
#       a=a//10
# print(sum)
# пользователь вводит число, необходимо посчитать сумму цифр этого числа (кол-во разрядов не знаем)


# n=int(input())
# for i in range (n):
#     print("hello", end=" ")
# вывести n-ое количество раз слово hello через for


# n=int(input())
# sum=0
# for i in range (n):
#     sum+=int(input())
# print(sum/n)
# ввести n чисел и посчитать их среднее арифметическое


# n=int(input())
# count=0
# for i in range(n):
#     num=int(input())
#     if n%2==0:
#        count+=1
# print(count)
# посчитайте количество четных чисел, введенных пользователем


# n=int(input("введите число: "))
# for i in range(1, 10):
#     print(n, "*", i, "=", n*i)
# напишите таблицу умножения с тем числом, которое выведет пользователь через цикл for

# import random
# a = random.randint(1,9)
# print(a)
# выведет рандомное число в промежутке от 1 до 9 включительно

# import random
# a=random.randint(10, 99)
# print("загаданное число", a)
# num=int(input("введите число: "))
# if num>a:
#     print("введенное число больше загаданного")
# elif num<a:
#     print("введенное число меньше загаданного")
# else:
#     print("ура")
# комп загадывает число в диапазоне от 10 до 99, нам необходимо угадать число

# import random
# a=random.randint(10, 99)
# print("загаданное число", a)
# flag = True
# while flag:
#     num = int(input("введите число: "))
#     if num>a:
#         print("введенное число больше загаданного")
#     elif num<a:
#         print("введенное число меньше загаданного")
#     else:
#         print("ура")
#         flag=False
# комп загадывает число в диапазоне от 10 до 99, нам необходимо угадать число, отгадываем число до тех пор пока не угадаем


# import random
# count=0
# a=random.randint(10, 99)
# print("загаданное число", a)
# flag = True
# while flag:
#     count+=1
#     num = int(input("введите число: "))
#     if num>a:
#         print("введенное число больше загаданного")
#     elif num<a:
#         print("введенное число меньше загаданного")
#     else:
#         print("ура")
#         flag=False
# print("Вы сделали", count, "попыток")
# комп загадывает число в диапазоне от 10 до 99, нам необходимо угадать число, отгадываем число до тех пор пока не угадаем
# модернизируйте программу так, чтобы в конце она писала еще и за сколько попыток число было отгадано


# import random
# count=0
# a=random.randint(10, 99)
# print("загаданное число", a)
# for i in range(5):
#     count+=1
#     num = int(input("введите число: "))
#     if num>a:
#         print("введенное число больше загаданного")
#     elif num<a:
#         print("введенное число меньше загаданного")
#     else:
#         print("ура")
#         break
# if (count==5):
#     print("вы проиграли")
# print("Вы сделали", count, "попыток")
# комп загадывает число в диапазоне от 10 до 99, нам необходимо угадать число, отгадываем число до тех пор пока не угадаем
# модернизируйте код так, чтобы стояло ограничение на количество попыток 5 и после 5 неудачных было написано "вы проиграли"
#-- если мы хотим в какой то момент выйти из цикла, то пишем break, после этой строчки мы сразу выходим из цикла


import random
count=0
flag = True
while flag:
    a=random.randint(10, 99)
    print("загаданное число", a)
    for i in range(5):
        count+=1
        num = int(input("введите число: "))
        if num>a:
            print("введенное число больше загаданного")
        elif num<a:
            print("введенное число меньше загаданного")
        else:
            print("ура")
            break
    if (count==5):
        print("вы проиграли")
    print("Вы сделали", count, "попыток")
    vibor=input("yes/no ")
    if (vibor!="yes"):
        break

# добавьте к прошлому заданию такой код, чтобы комп предложил сыграть еще раз

0 камень, 1 ножницы, 2 бумага
сравниваем со значениями
это для дз