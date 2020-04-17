print("CALCULATOR")
num1=int(input("Enter number here:  "))
num2=int(input("Enter number here:  "))
print("what opertion  you have to be performed +,-,*,/ :  ")
symbool=input("enter opertion:  ")


def cal(first_value,sec_value,oper):

    if(oper=="+"):
        return first_value+sec_value
    elif(oper=="-"):
        return first_value-sec_value
    elif (oper == "/"):
        return first_value/sec_value
    elif (oper == "*"):
        return first_value *sec_value
    else:
        print("INVALID OPERATION")
report=cal(num1,num2,symbool)
print("opertion : ",report)
