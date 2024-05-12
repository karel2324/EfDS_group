import sys
import pandas as pd
import datetime as dt
import glob
import home_messages_db as hm
import sqlalchemy as sa
import os

def smart(file):
    data = pd.read_csv (str(file), sep = '\t')   #read in the files
    data = data.drop('attribute', axis=1) #Selecting columns
    data = data.drop_duplicates() #removing duplicates
    data.rename(columns={"epoch":"time"},inplace=True)
    data["time"] = pd.to_datetime(data.time).dt.tz_localize(None) # Remove time zones
    data["time"] = (data['time'] - dt.datetime(1970,1,1)).dt.total_seconds()  #Change to epoch time
    data = data.reset_index(drop=True)  #Remove index from dataframe
    return data

used = False #whether or not the function table is used
while used == False:
    userinput = input("What would you like to do with this tool? Use -h or --help for a description of the tool. \n") #get user input
    if userinput == "-h" or userinput == "--help":
        print("Usage:\n smartthings.py [OPTIONS] smartthings-2022-01-01-2022-09-22.tsv [...]\n")
        print("Output options: \n -d DBURL insert into the project database (DBURL is a SQLALchemy database URL) \n")
    elif "smartthings.py -d " in userinput: # else if input is of type: tool -d DBURL filename
        li = list(userinput.split(" "))
        path = "efds/smartthings/"+li[3]
        name = li[0].replace('.py', '')
        for filepath in glob.glob(path):
            df = smart(filepath)
            db = hm.HomeMessagesDB(li[2]) #create instance
            db.connect() #connecting
            db.add(df, name) #adding dataframe
        used = True
    else:
        print("We do not understand what you are asking \n")
        

db.dup(name) #Remove duplicates from the table
    
