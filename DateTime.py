import datetime

#Function for date and time
def getDateTime():   
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)

    date = str(year+"/"+month+"/"+day)
    time = str(hour+":"+minute+":"+second)

    return date,time

#Function for data and time for Bill only
def getDateTimeBill():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)

    date_time = str(year+month+day+hour+minute+second)

    return date_time

