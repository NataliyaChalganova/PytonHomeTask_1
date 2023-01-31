# Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Enter the size of the chocolate: '))
m = int(input('Enter the size of the chocolate: '))
k = int(input("Enter the number of chocolate pieces to be broken off: "))
if k < m*n and (k%m==0 or k%n==0):
    print('yes')
else:
    print('no')