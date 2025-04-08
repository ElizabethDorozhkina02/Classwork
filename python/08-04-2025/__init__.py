# a = input("введите слово ")
# print((a+" ")*10)
# выведет написанное слово 10 раз

# a = input("введите слово ")
# n = int(input("введите количество повторений "))
# print((a+" ")*n)
# где n любое количество повторений

# n = int(input("до какого числа выводить целые числа? "))
# a=0
# while a<=n:
#     print(a)
#     a = a + 1

# n = int(input("до какого числа выводить целые числа? "))
# while n>=0:
#     print(n)
#     n = n-1 или n -=1
# считает от большего к меньшему

# a = int(input("num1 "))
# b = int(input("num2 "))
# if a>b:
#     a,b=b,a
# while a<=b:
#     print(a, end=" ")
#     a+=1
# end выводит значения не в столбец, а в строку
# показывает нам результат обязательно по возрастанию

# a = int(input("num1 "))
# b = int(input("num2 "))
# if a>b:
#       a,b=b,a
# while a<=b:
#      print(b, end=" ")
#      b-=1
# показывает нам результат по убыванию

# a = int(input("num: "))
# b = 0
# k = 1
# if a<0:
#     k= -1
# while b!=a:
#     print(b, end=" ")
#     b=b+k
# print(b)
# выводит числа от 0 до числа пользователя
#     while b>=a:
#     print(b)
#     b-=1
# elif a>0:
#     b=0
#     while b<=a:
#     print(b)
#     b+=1

# a=int(input("num1: "))
# b=int(input("num2: "))
# sum = 0
# if a>b:
#     a,b=b,a
# while a<=b:
#     sum+=a
#     a+=1
# print(sum)
# посчитать сумму всех целых чисел от а до б

# a=int(input("num1: "))
# b=int(input("num2: "))
# sum = 0
# if a>b: a,b=b,a
# while a<=b:
#     if a%2:
#         print(a)
#     a+=1
# # либо вайл пишем так
# while a<=b:
#         print(a)
#     a+=2
# # пользователь вводит с клавиатуры два числа. нужно показать все нечетные числа в указ-ом диапазоне

# a=int(input("num1: "))
# b=int(input("num2: "))
# sum = 0
# if a>b:
#      a,b=b,a
# while a<=b:
#      sum+ =a
#      a+=1
# print(sum/(b-a))
# найти среднее арифметическое двух чисел

# x=0
# n=int(input("Введите количество: "))
# while n>0:
#       a=int(input())
#       if a==3:
#          x+=1
#       n-=1
# print(x)
# пользователь вводит n-чисел, надо определить сколько раз пользователь ввел число 3

# sum=0
# n=int(input("Введите количество: "))
# while n>0:
#       a=int(input("введите число: "))
#       sum+=a
#       n-=1
# print(sum)
# пользователь вводит n-чисел, надо определить сумму чисел

# max=0
# n=int(input("Введите количество: "))
# while n>0:
#       a=int(input("введите число: "))
# if max==0:
#       max=a
# if max<a:
#       max=a
#       n-=1
# print(max)
# пользователь вводит n-чисел, надо определить максимальное число

# n=int(input("введите число: "))
# s=0
# while s<=10:
#       print(f"{n}\t * \t{s}\t = {n*s} ")
#       s+=1
# напишите таблицу умножения

# n=int(input("введите число: "))
# fact = 1
# while(n>1):
#     fact*=n
#     n-=1
# print(fact)
# пользователь вводит число.посчитайте факториал числа по формуле n!=1*2*3..*n, где n число для расчета факториала
