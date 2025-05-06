# students=["Иван","Олег","Катя","Виктор"]
# print(students[len(students)-1])

# students=["Иван","Олег","Катя","Виктор"]
# students[2]="tttt"
# for i in range (len(students)):
#     students[i]+="oooo"
#     print(students[i])
# # выведет все имена по порядку
# # если хоти менять сами значения в списке, то обращаемся к ним по индексу
#
#
# for i in students:
#     print(i)
# # если хотим применить значение списка
# print(students)


# необходимо вывести список чисел, где покажутся только четные
# number=[1,2,3,4,5,6,7,8,9,10]
# # for i in number:
# #     if(i%2==0):
# #     print(i)
#
# for i in range(len(number)):
#     if (number[i]%2==0):
#         print(number[i])


# # необходимо определить сколько раз число встречается в списке
# number=[1,2,3,4,5,6,7,8,9,10]
# num=int(input())
# counter=0
# for i in number:
#     if (i==num):
#         counter+=1
#     print(counter)

# ввести число и х-раз вывести случайные числа
# import random
# number=[1,2,3,4,5,6,7,8,9,10]
# count = int(input())
# for i in range (count):
#     print(number[random.randint(0,len(number)-1)], end=" ")

# вывести все значения данного списка из конца в начало
# number=[1,2,3,4,5,6,7,8,9,10]
# for i in range (len(number)-1, -1, -1):
#     print(number[i], end=" ")

# в списке целых чисел вычислить сумму отриц, сумму четных, сумму нечетных, произведение с индексами кратными 3,
# произв.эл. между мин и макс,сумму эл. между 1 и послед.положит.эл

number=[4,5,7,45,86,74,-12,90,34,1,7,9,98,22]
summ_negative = 0
summ_odd = 0
summ_even = 0
for i in number:
    if i%2==0: summ_odd+=i
    else: summ_even+=i
    if i<0: summ_negative+=i
for i in range(0, len(number), 3):
    print(number[i])
max = number[0]
min = number[0]
min_index = 0
max_index = 0
for i in range (0, len(number)-1):
    if (min > number[i]):
        min = number[i]
        min_index = i
    if (max < number[i]):
        max = number[i]
        max_index = i
if min_index>max_index: min_index,max_index=max_index,min_index
mult = 1
for i in range (min_index+1, max_index):
    mult *= number[i]
print(mult)
print(min)
print(max)
first_index = 0
for i in range (0, len(number)):
    first_index = i
    break
last_index = 0
for i in range (len(number)-1, 0, -1):
    last_index = i
    break
sum = 0
for i in range (first_index+1, last_index):
    sum += number[i]
print(sum)





