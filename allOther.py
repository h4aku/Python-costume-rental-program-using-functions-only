#Function for getting the contents from the txt file
def getcontentOfFile():
    file = open("costume.txt","r")
    data = file.readlines()
    file.close()

    return data

#Function for creating a dictionary and placing the values of txt file in it
def getDictionary(contentOfFile):
    dictionary = {}
    
    for index in range(len(contentOfFile)):
        
        dictionary[index+1] = contentOfFile[index].replace("\n","").split(",")
    
    return dictionary

