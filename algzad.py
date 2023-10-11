

# a = int(input("Укажите число:"))
# b = int(input("Укажите число:"))
# while a <= b:
#     print("правильно")
#     break
# else:
#     print("не правильно Осталась 1 попытка")
#     a = int(input("Укажите целое число:"))
#     b = int(input("Укажите целое число:"))
# for j in range(a, b+1):
#     print(j)



# a = int(input("Укажите целое число:"))
# b = int(input("Укажите целое число:"))
# while a <= b:
#     print("правильно a<=b ")
#     for j in range(a, b + 1):
#         print(j)
#     break
# else:
#     if a >= b:
#         print("правильно a>=b ")
#         for j in range(a, b - 1, -1):
#             print(j)



# x = int(input("число:"))
# y = int(input("число:"))
# days = 0
# while Y - X >= 0:
#     X *= 0,1
#     days += 1
# print(days)



# p = 0
# while int(input("число:")) != 0:
#     p += 1
# print(p)



# a=int(input("число:"))
# b=int(input("число:"))
# k=0
# if b>a:
#     k+=1
# a=b
# while b!=0:
#     b=int(input("число:"))
#     if b>a:
#         k+=1
#     a=b
# print(k)



# a=int(input("число:"))
# b=int(input("число:"))
# if a>b:
#     max1=a
#     max2=b
# else:
#     max1=b
#     max2=a
# while b!=0:
#     b=int(input("число:"))
#     if b>max1:
#         max2=max1
#         max1=b
#     elif b>max2:
#         max2=b
# print(max2)



# fib1 = 1
# fib2 = 1
#
# n = input("Номер Фибоначчи: ")
# n = int(n)
#
# i = 0
# while i < n - 2:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1
#
# print("элемент:", fib2)



# p=int(input("число:"))
# c=1
# b=0
# while p!=0:
#     v=int(input())
#     p,v=v,p
#     if v==p:
#         c+=1
#     if c>b:
#         b=c
#     if p!=v:
#         c=1
# print(b)



# n = input("число:").split()
# chet = []
# for i in range(len(n)):
#     n[i] = int(n[i])
#     if (i - 1) % 2 != 0:
#         chet.append(str(n[i]))
# print(' '.join(chet))



# a = [int(s) for s in input().split()]
# for i in range(1,len(a)):
#     if a[i]>a[i-1]:
#         print(a[i])



# a = [int(s) for s in input("число:").split()]
# mx=a[0]
# mi=0
# for i in range(1,len(a)):
#     if a[i]>mx:
#         mx=a[i]
#         mi=i
# print(mx,mi)



# a = [int(i) for i in input("число:").split()]
# x = int(input("число:"))
# pos = 0
# while pos < len(a) and a[pos] >= x:
#     pos += 1
# print(pos + 1)



# a= [ 1, 2, 5, 0, 7, 3, 2 ]
# print( a )
#
# for i in range( 0, len( a ) - 1, 2 ):
#     a[ i ], a[i + 1] = a[i + 1], a[i]
#
# print( a )



# a = [{min(a): max(a), max(a): min(a)}.get(x, x) for x in a]



# a = [7, 6, 5, 4, 3, 2, 1]
# k = 2
# result = a[:k] + a[k + 1:]
# print(result)



# a=[int(i) for i in input().split()]
# k,c=[int(e) for e in input().split()]
# a.insert(k,c)
# a=(" ".join([str(i)for i in a]))
# print(a)



# n = 8
# x = [0] * n
# y = [0] * n
# result = 'NO'
# for i in range(n):
#     x[i], y[i] = [int(j) for j in input().split()]
# for i in range (n):
#     for j in range(i+1,n):
#         if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
#             result = 'YES'
# print(result)