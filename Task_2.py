# Задача 2: Найдите сумму цифр трехзначного числа.
#  123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Введите трехзначное число "))
sum = 0 
while number > 0:
     remainder = number % 10 
     sum += remainder 
     number //= 10 
print(sum)