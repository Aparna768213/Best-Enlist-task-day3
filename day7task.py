def math(num1,num2):
    print("Addition of two numbers",num1+num2)
    print("Subtraction of two numbers",num1-num2)
    print("Multiplication of two numbers",num1*num2)
    print("Division of two numbers",num1/num2)
num1 = float(input("Enter 1st number:"))
num2 = float(input("Enter 2nd num:"))
math(num1,num2)


#Create a function covid()& it should accept patient name ,and body temperature ,by default the body temparature should be 98 degree.
def covid(patient_name, body_temperature):
    if body_temperature < str(0):
        default=str(98)
        print("Patient name is",patient_name," Body temperature is",default)
    else:
        print("Patient name is",patient_name," Body temperature is",body_temperature)
covid("Aparna","")
covid("Aparna","99")



    
