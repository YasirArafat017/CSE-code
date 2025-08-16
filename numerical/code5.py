X = int(input("Enter 1st Num  "))
Y= int (input("Enter 2nd Num  "))
print("What oparation u do (+,-,*,/)")
 x= input("Enter the operator: ")
if(x=='+'):
    sum=X+Y
    print("Sum: ",sum)
elif(x=='-'):
    sub=X-Y
    print("Sub: ",sub)
elif(x=='*'):
    mul=X*Y
    print("Mul: ",mul)
elif(x=='/'):
    if Y!=0:
        div=X/Y
        print("Div: ",div)
    else:
        print(" not posible division by Zero!")

            
