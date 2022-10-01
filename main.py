from RentOperations import *
from ReturnOperations import *
from allOther import *
from DateTime import *

#creating function for home screen
def mainFunction():

    print("#####################################################################")
    print("#                   Welcome to Haku Costume Rentals                 #")
    print("#####################################################################")
    
    Loop = True

    while Loop == True:
        print("\nSelect an option:\n")
        print(" 1) Enter 1 to rent costume.")
        print(" 2) Enter 2 to return costume.")
        print(" 3) Enter 3 to exit.\n")
            
        try:
            
            uInput = int(input("Enter an option mentioned above: "))

            #calling functions corresponding to the input 
            if uInput == 1:
                    
                rent()
                    
            elif uInput == 2:
                    
                ret()
                    
            elif uInput == 3:

                print("\n===================================================================")
                print("\n                 Thank you for using our application!\n")
                print("===================================================================")
                Loop = False

            else:
                
                print("\n===================================================================")
                print("                Invalid Input!!! Chose a valid option!")
                print("===================================================================")

        except:
            
            print("\n***********************")
            print("*Null or Invalid Input*")
            print("***********************")

mainFunction()
