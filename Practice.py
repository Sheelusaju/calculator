print ("AVAILABLE OPERATIONS \n 1:addition\n 2:substraction \n 3:Multiplication \n 4:Division \n")
inputMenu = input ("Enter any one choice of operation \n 1/2/3/4 \n")

def addition(a,b) :
         x= a+b
         return x
         
   
def substraction(a,b) :
         x= a-b
         return x
        

def multiplication(a,b) :
         x= a*b
         return x
         

def division(a,b) :
         x= a/b 
         return x
         
if inputMenu in ["1","2","3","4"]:
    input1 = input("Enter First Number:\n")
    input2 = input("Enter Second Number:\n")
    if input1.isnumeric() and input2.isnumeric() :
        a= float(input1)
        b=float(input2)
        if inputMenu=='1':
            print("sum is ", addition(a,b))
        elif inputMenu=='2':
            print("difference is ", substraction(a,b))
        elif inputMenu=='3':
            print("product is ", multiplication(a,b))
        elif inputMenu=='4':
            if b!=0:
                print("quotient is ", division(a,b))
            else:
                  print("divisor cannot be zero")
        else :
            print("Please select a option in list")  

    else:

        print("Inputs are not numbers")
else:
      print("invalid input")