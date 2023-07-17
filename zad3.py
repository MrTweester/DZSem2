# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите число: "))
stop = 0
step = 2
for i in range(n):
    if stop != 1:
        step = step ** i
        if step <= n:
            print(step, end=' ')
            step = 2
        else:
            stop = 1
    else:
        i = n








# step = int(2)
# res = 2
# count = 1
# while n>step:
#     count=res*step
#     step+=1
#     print(count, "в степени", step, "равно: ",  )