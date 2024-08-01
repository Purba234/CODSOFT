print("Select operation")
print("1.add")
print("2.substract")
print("3.divide")
print("4.multiply")
choice=int(input("Select operation"))
num1=int(input("Enter num1"))
num2=int(input("Enter num2"))
if choice==1:
          print(num1,"+",num2,"=",(num1+num2))
elif choice==2:
          print(num1,"-",num2,"=",(num1-num2))
elif choice==3:
          print(num1,"/",num2,"=",(num1/num2))
elif choice==4:

         print(num1,"*",num2,"=",(num1*num2))
               

         
else :
        print("Enter your right choice")




