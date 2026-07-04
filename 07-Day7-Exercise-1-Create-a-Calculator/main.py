# a=15
# b=8
# obj1=a+b
# print("The sum of",a,"and",b,"is",obj1)
# obj2=a-b
# print("The difference of",a,"and",b,"is",obj2)
# obj3=a*b
# print("The multiplication of",a,"and",b,"is",obj3)
# obj4=a/b
# print("The division of",a,"and",b,"is",obj4)
# obj5=a%b
# print("The modulus of",a,"and",b,"is",obj5)
# obj6=a//b
# print("The floor division of",a,"and",b,"is", obj6)

a=int(input("Enter first number: "))
b=(input("Enter any arithmetic operator:"))
c=int(input("Enter second number: "))
if b== "+" :
  print("The output is:",a+c)
elif b== "-" :
  print("The output is:",a-c)
elif b== "*" :
  print("The output is:",a*c)
elif b== "/" :
  print("The output is:",a/b)
else:
  print("Invalid operator")