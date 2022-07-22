def primeorNot(num): 
 if num > 1:
   for i in range(2,num):
    if (num % i) == 0:
     print(num,"is not a prime number")
    #  print(i,"times",num//i,"is",num)
     break
    else:
      print(num,"is a prime number")
#  else:
#   print(num,"is not a prime number")
# primeorNot(406)
num=int(input("enter the num"))
primeorNot(num)


# def number():
#     num=0
#     i=1
#     while i<=n:
#         if n%i==0:
#             num=num+1
#         i=i+1
#     if num==2:
#         print("prime number")
#     else:
#         print("not prime number")
# n=int(input("enter the number"))
# number()