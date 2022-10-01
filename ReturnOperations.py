import os
from allOther import *
from DateTime import *

#Function for displaying all the available costumes
def printReturnCostumes():
    contentOfFile = getcontentOfFile()
    mainData = getDictionary(contentOfFile)

    print("\n-----------------------------------------")
    print("|S.N","\t","Costume Name","\t","Brand","\t\t|")
    print("-----------------------------------------")
    
    for key,value in mainData.items():
        
        print("|",key,"\t",value[0],"\t",value[1],"\t|")
        
    print("-----------------------------------------")

#Function for validating the SNO  
def getRetSNO(mainData):
    vData = False
    
    while vData == False:
        
        try: 
            rSNO = (input("\nEnter the costume you want to return.\n(Type 'cancel' to Exit to main menu): ")).lower()

            #checking if sno input is 'cancel'
            if rSNO == "cancel":
                
                return "cancel"

            else: #can be written as elif rSNO != "cancel"

                rSNO = int(rSNO) #converting input of sno to int datatype
                
                if rSNO > 0 and rSNO <= len(mainData):
                
                    vData = True
                
                    return rSNO

                else:
                
                    print("\n=====================================================================")
                    print("          Invalid Input!!! Chose a valid option!")
                    print("=====================================================================")
                
        except:
            
            print("\n************************************")
            print("*No Strings Allowed except 'cancel'*")
            print("************************************")
            
#Function for validating quantity
def getRetQty(mainData, rSNO):
    continueLoop = True

    while continueLoop == True:

        try:
            QTYreturn = input("\nHow many would you like to return?\n(Enter 'none' to cancel): ")

            for key,value in mainData.items():

                if key == rSNO:

                    #checking if input of quantity is none
                    if QTYreturn == "none":

                        return "none"

                    else: #equivalent to QTYreturn != "none"
                        
                        QTYreturn = int(QTYreturn) 

                        if QTYreturn <= 0:
                            
                            print("\n*****************************")
                            print("*Cannot return",QTYreturn,"costumes*")
                            print("*****************************")
                            
                        else:
                            
                            print("\n=====================================================================")
                            print("                Successfully returned ", QTYreturn,value[0])
                            print("=====================================================================")

                            return QTYreturn

        except:
            
            print("\n**********************************")
            print("*No Strings allowed except 'none'*")
            print("**********************************")

#Function for updating the quantity in txt file   
def writeReturnFunction(mainData, rSNO, QTYreturn):
    try:
        
        mainData[rSNO][3] = str(int(mainData[rSNO][3]) + QTYreturn)
        
        file = open("costume.txt","w")
        
        for value in mainData.values():
            
            writeData = value[0]+","+value[1]+","+value[2]+","+value[3]+"\n"
            
            file.write(writeData)
            
        file.close()
        
    except:
        
        return

#Function for printing bill if returned on time
def printBillOnTime(mainData,contentOfFile,cart2,date,time,date_time,name,contact):
    xTotal = 0
    
    filePath = os.path.abspath("Bill/"+name+date_time+"RETURNED_BILL"+".txt") #declaring os path

    txtFile = open(filePath, "w")
                        
    txtFile.write("\n##################################################################\n")
    txtFile.write("\n                              BILLING\n")
    txtFile.write("\n..................................................................\n")
    txtFile.write("\nName: "+ name)
    txtFile.write("\nContact: "+ contact)
    txtFile.write("\nDate: "+ date)
    txtFile.write("\nTime: "+ time + "\n")

    txtFile.write("\n*******************************************************************\n")
    txtFile.write("            THE FOLLOWING COSTUMES HAVE BEEN RETURNED!")
    txtFile.write("\n*******************************************************************\n")
                            
    txtFile.write("\n------------------------------------------------------------------\n")
    txtFile.write("|S.N"+"\t"+"Costume Name"+"\t"+"Brand"+"\t\t"+"Quantity"+"\t"+"Price"+"\t |")
    txtFile.write("\n------------------------------------------------------------------")
        
    for index in range(len(cart2)):
                            
        xID = int(cart2[index][0])
        xName = mainData[xID][0]
        xBrand = mainData[xID][1]
        xQuantity = int(cart2[index][1])
        xPrice = float(mainData[xID][2])* xQuantity 
        xTotal = xTotal + xPrice
                                
        txtFile.write("\n\n|"+str(index+1)+"\t"+xName+"\t"+xBrand+"\t\t"+str(xQuantity)+"\t\t"+str(xPrice)+"\t |")
        txtFile.write("\n\n------------------------------------------------------------------")
                            
    txtFile.write("\n\n#"+"\t\t" + "        Total is:       " + str(xTotal)+ "\n")
    txtFile.write("\n##################################################################")
    txtFile.close()

    file = open(filePath, "r")
    contentOfFileBill = file.read()
    print(contentOfFileBill)
    file.close()

#Function for printing bill if not returned on time
def printBillNotOnTime(mainData,contentOfFile,cart2,date,time,date_time,name,contact,days):
    xTotal = 0
    
    filePath = os.path.abspath("Bill/"+name+date_time+"RETURNED_BILL"+".txt")#declaring os path

    txtFile = open(filePath, "w")
                        
    txtFile.write("\n##################################################################\n")
    txtFile.write("\n                              BILLING\n")
    txtFile.write("\n..................................................................\n")
    txtFile.write("\nName: "+ name)
    txtFile.write("\nContact: "+ contact)
    txtFile.write("\nDate: "+ date)
    txtFile.write("\nTime: "+ time + "\n")

    txtFile.write("\n*******************************************************************\n")
    txtFile.write("            THE FOLLOWING COSTUMES HAVE BEEN RETURNED!")
    txtFile.write("\n*******************************************************************\n")
                            
    txtFile.write("\n------------------------------------------------------------------\n")
    txtFile.write("|S.N"+"\t"+"Costume Name"+"\t"+"Brand"+"\t\t"+"Quantity"+"\t"+"Price"+"\t |")
    txtFile.write("\n------------------------------------------------------------------")
        
    for index in range(len(cart2)):
                            
        xID = int(cart2[index][0])
        xName = mainData[xID][0]
        xBrand = mainData[xID][1]
        xQuantity = int(cart2[index][1])
        xPrice = float(mainData[xID][2])* xQuantity 
        xTotal = xTotal + xPrice
        xFine = float(5*days)
        xGrandTotal = xTotal + xFine
                                
        txtFile.write("\n\n|"+str(index+1)+"\t"+xName+"\t"+xBrand+"\t\t"+str(xQuantity)+"\t\t"+str(xPrice)+"\t |")
        txtFile.write("\n\n------------------------------------------------------------------")
                            
    txtFile.write("\n\n#"+"\t" + "Total without including fine:   " + str(xTotal))
    txtFile.write("\n#"+"\t" + "Total Fine: \t\t        " + str(xFine))
    txtFile.write("\n#"+"\t" + "Grand Total: \t\t        " + str(xGrandTotal))
    txtFile.write("\n\n##################################################################")
    txtFile.close()

    file = open(filePath, "r")
    contentOfFileBill = file.read()
    print(contentOfFileBill)
    file.close()

#Function for returning more costumes
def returnMore(mainData,contentOfFile,cart2,date,time,date_time):
    
    print("\n*******************************************************************")
    print("\n               Select which costume you want to return.\n")
    print("*******************************************************************")
        
    printReturnCostumes()

    rSNO = getRetSNO(mainData)

    #checking if input of sno is "cancel"
    if rSNO == "cancel":

        return
    
    else:
        
        QTYreturn = getRetQty(mainData, rSNO)

        #checking if input of quantity is "none"   
        if QTYreturn == "none":
                
            return ret()
        
        else:

            #adding items to list and rewriting the quantity in the text file
            cart2.append([rSNO, QTYreturn])
            
            writeReturnFunction(mainData, rSNO, QTYreturn)
            
            continueLoop = True
            
            while continueLoop == True:

                #returning more costumes
                returnMore = input("\nDo you wish to return more costumes?(y/n): ")
                
                if returnMore == "n":
                    
                    continueLoop = False
                    
                    name = input("\nYour name?: ")
                    contact = input("\nYour contact number?: ")
                    
                    onTimeLoop = True

                    while onTimeLoop == True:
                        
                        onTime = (input("\nIs the costume returned in time?(y/n): ")).lower()

                        #checking if costume was returned on time
                        if onTime == "y":

                            onTimeLoop = False
                            
                            printBillOnTime(mainData,contentOfFile,cart2,date,time,date_time,name,contact)
                            
                            
                        elif onTime == "n":
                            
                            onTimeLoop = False

                            daysLoop = True

                            while daysLoop == True:
                                try:
                                    days = int(input("\nHow many days late?(5 fine per day): "))

                                    if days >= 0:
                                        daysLoop = False

                                        printBillNotOnTime(mainData,contentOfFile,cart2,date,time,date_time,name,contact,days)
                                        
                                    else:
                                        
                                        print("\n*****************************************")
                                        print("*Values cannot be in decimal or negative*")
                                        print("*****************************************")
                                        
                                except:
                                    
                                    print("\n*********************")
                                    print("*No Strings Allowed.*")
                                    print("*********************")
                                    

                        else:

                            onTimeLoop = True
                            print("\n************************************")
                            print("*Incorrect Data. Enter y or n only.*")
                            print("************************************")

                    
                        
                elif returnMore == "y":
                    
                    print("\n*********************************************************************")
                    print("\n               Select which costume you want to return.\n")
                    print("*********************************************************************")
                
                    printReturnCostumes()
                    rSNO = getRetSNO(mainData)

                    if rSNO == "cancel":

                        continueLoop = False
                        
                        name = input("\nYour name?: ")
                        contact = input("\nYour contact number?: ")

                        onTimeLoop = True

                        while onTimeLoop == True:
                            
                            onTime = (input("\nIs the costume returned in time?(y/n): ")).lower()
                            #checking if costume was returned on time
                            if onTime == "y":

                                onTimeLoop = False
                                
                                printBillOnTime(mainData,contentOfFile,cart2,date,time,date_time,name,contact)
                                
                            elif onTime == "n":

                                onTimeLoop = False

                                daysLoop = True

                                while daysLoop == True:
                                    try:
                                        days = int(input("\nHow many days late?(5 fine per day):"))

                                        if days >= 0:
                                            daysLoop = False

                                            printBillNotOnTime(mainData,contentOfFile,cart2,date,time,date_time,name,contact,days)
                                            
                                        else:
                                            print("\n****************************************")
                                            print("*Value cannot be in negative or decimal*")
                                            print("****************************************")
                                        
                                    except:

                                        print(cart2)
                                        input()
                                        print("\n**********************")
                                        print("*No Strings Allowed!.*")
                                        print("**********************")
                                
                            else:
                                continueLoop = True
                                print("\n************************************")
                                print("*Incorrect Data. Enter y or n only.*")
                                print("************************************")
                            

                    elif rSNO != "cancel":
                        
                        QTYreturn = getRetQty(mainData, rSNO)
                

                        if QTYreturn == "none":

                            continueLoop = True
                            

                        elif QTYreturn != "none":

                            cart2.append([rSNO, QTYreturn])

                            writeReturnFunction(mainData, rSNO, QTYreturn)

                else:
                    print("\n************************************")
                    print("*Incorrect Data. Enter y or n only.*")
                    print("************************************")

#main return function
def ret():
    cart2 = []
    date,time = getDateTime()
    contentOfFile = getcontentOfFile()
    mainData = getDictionary(contentOfFile)
    date_time = getDateTimeBill()

    returnMore(mainData,contentOfFile,cart2,date,time,date_time)


