import os
from allOther import *
from DateTime import *

#Function for displaying all the available costumes
def printRentCostumes():
    contentOfFile = getcontentOfFile()
    mainData = getDictionary(contentOfFile)

    print("\n-------------------------------------------------------------------")
    print("|S.N","\t","Costume Name","\t","Brand","\t\t","Price(Rs)","\t","Quantity","|")
    print("-------------------------------------------------------------------")
    
    for key,value in mainData.items():
        
        print("|",key,"\t",value[0],"\t",value[1],"\t",value[2],"\t\t",value[3],"\t  |")
        
    print("-------------------------------------------------------------------")

#Function for validating the SNO
def getRentSNO(mainData):
    vData = False
    
    while vData == False:
        try:
            
            SNO = (input("\nEnter the costume you want to rent.\n(Type 'Cancel' to Exit to main menu): ")).lower()

            #checking if sno input is 'cancel'
            if SNO == "cancel":
                
                return "cancel"
                
            else: #can be written as elif SNO != "cancel"
                
                SNO = int(SNO) #converting input of sno to int datatype
                
                if SNO > 0 and SNO <= len(mainData):
                
                    vData = True
                
                    return SNO
            
                else:
                
                    print("\n=====================================================================")
                    print("                 Invalid Input!!! Chose a valid option!")
                    print("=====================================================================")

        except:

            print("\n************************************")
            print("*No Strings Allowed except 'cancel'*")
            print("************************************")

#Function for validating quantity
def getRentQty(mainData, SNO, cart1):
    vData = False
    while vData == False:

        try:
            costumeQty = (input("\nHow many do you want?\n(enter 'none' to cancel): ")).lower()

            #checking if input of quantity is none or not
            if costumeQty!="none":
                
                costumeQty = int(costumeQty)
            
            else:  
                    
                return "none"
            
            for key,value in mainData.items():

                #checking if sno exists in the main data
                if key == SNO:
                    
                    if costumeQty >=1 and costumeQty <= int(value[3]):
                        
                        vData = True
                        
                        print("\n=====================================================================")
                        print("                 Successfully rented ", costumeQty, value[0])
                        print("=====================================================================")
                        cart1.append([SNO,costumeQty]) #adding the items to list
                        
                        return costumeQty
                    
                    elif(costumeQty > int(value[3])):

                        print("\n=====================================================================")
                        print("                   Not enough costumes in stock")
                        print("=====================================================================")

                    else:

                        print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                        print("                   Cannot rent ", costumeQty, " costumes!!!!")
                        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        except:
            
            print("\n**********************************")
            print("*No Strings allowed except 'none'*")
            print("**********************************")

#Function for updating the quantity in txt file
def writeRentFunction(mainData, SNO, costumeQty):
    try:
        
        mainData[SNO][3] = str(int(mainData[SNO][3]) - costumeQty)
        
        file = open("costume.txt","w")
        
        for value in mainData.values():
            
            write_data = value[0]+","+value[1]+","+value[2]+","+value[3]+"\n"
            
            file.write(write_data)
            
        file.close()
        
    except:
        
        return

#Function for printing bill
def printBillRent(mainData,contentOfFile,cart1,date,time,date_time):
    xTotal = 0
    
    name = input("\nYour name?: ")
    contact = input("\nYour contact number?: ")
    
    filePath = os.path.abspath("Bill/"+name+date_time+"RENTED_BILL"+".txt")#declaring os path

    txtFile = open(filePath, "w")
                        
    txtFile.write("\n###################################################################\n")
    txtFile.write("\n                               BILLING\n")
    txtFile.write("\n...................................................................\n")
    txtFile.write("\nName: "+ name)
    txtFile.write("\nContact: "+ contact)
    txtFile.write("\nDate: "+ date)
    txtFile.write("\nTime: "+ time + "\n")


    txtFile.write("\n*******************************************************************\n")
    txtFile.write("              THE FOLLOWING COSTUMES HAVE BEEN RENTED!")
    txtFile.write("\n*******************************************************************\n")
        
    txtFile.write("\n-------------------------------------------------------------------\n")
    txtFile.write("|S.N"+"\t"+"Costume Name"+"\t"+"Brand"+"\t\t"+"Price(Rs)"+"\t"+"Quantity"+"  |")
    txtFile.write("\n-------------------------------------------------------------------\n")
        
    for index in range(len(cart1)):
                            
        xID = int(cart1[index][0])
        xName = mainData[xID][0]
        xBrand = mainData[xID][1]
        xQuantity = int(cart1[index][1])
        xPrice = float(mainData[xID][2])* xQuantity 
        xTotal = xTotal + xPrice
                            
        txtFile.write("\n|"+str(index+1)+"\t"+xName+"\t"+xBrand+"\t\t"+str(xPrice)+"\t\t"+str(xQuantity)+"\t  |")
        txtFile.write("\n\n-------------------------------------------------------------------")

    txtFile.write("\n\n#"+"\t\t" + "         Total is:      " + str(xTotal))
    txtFile.write("\n\n###################################################################")
    txtFile.close()

    file = open(filePath, "r")
    contentOfFileBill = file.read()
    print(contentOfFileBill)
    file.close()
        
#Function for renting more costumes
def rentMore(mainData,contentOfFile,cart1,date,time,date_time):
    
    print("\n*********************************************************************")
    print("\n               Select which costume you want to rent.\n")
    print("*********************************************************************")
        
    printRentCostumes()
        
    SNO = getRentSNO(mainData)

    #checking if input of sno is "cancel"
    if SNO == "cancel":
        
        return
    
    else:
        
        costumeQty = getRentQty(mainData, SNO, cart1)

        #checking if input of quantity is "none"
        if costumeQty == "none":
                
            return rent()
        
        else:

            #updating the quantity in txt file
            writeRentFunction(mainData, SNO, costumeQty)
            
            continueLoop = True
            while continueLoop == True:

                #renting more costumes
                rentMore = (input("\nDo you wish to rent more costumes?(y/n): ")).lower()
                
                if rentMore == "n":
                    
                    continueLoop = False
                    
                    printBillRent(mainData,contentOfFile,cart1,date,time,date_time)
                    
                    
                elif rentMore == "y":
                    print("\n*********************************************************************\n")
                    print("                Select which costume you want to rent.")
                    print("\n*********************************************************************\n")
                        
                    printRentCostumes()

                    SNO = getRentSNO(mainData)

                    if SNO == "cancel":

                        continueLoop = False
                        
                        printBillRent(mainData,contentOfFile,cart1,date,time,date_time)
                            
                             
                    else:
            
                        costumeQty = getRentQty(mainData, SNO, cart1)

                        if costumeQty == "none":
                            
                            continueLoop = True
                        
                        elif costumeQty != "none":
                            
                            writeRentFunction(mainData, SNO, costumeQty)
                        
            
                else:
                    
                    print("\n************************************")
                    print("*Incorrect Data. Enter y or n only.*")
                    print("************************************")
                    
#main rent function
def rent():
    cart1 = []
    date,time = getDateTime()
    contentOfFile = getcontentOfFile()
    mainData = getDictionary(contentOfFile)
    date_time = getDateTimeBill()

    rentMore(mainData,contentOfFile,cart1,date,time,date_time)

    
