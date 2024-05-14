## Differences:
#1. Name of function = 'cleanuptsv'
#2. Directory should (maybe) be in 2nd function
#3. Deduplication within function cleanuptsv
#4. Renaming 'epoch' to 'time'.
#5. Using 'pandas' instead of 'pd'

## Questions:
##1. What is concatenate?
##2. Is renaming column 'epoch' to 'time' really needed? Maybe rename it to 'Unix'?
##3. Could you try if the cleanuptsv-function works for you?

import pandas 
import glob
import click
from home_messages_db import HomeMessagesDB


def cleanuptsv(documents):
    combined_df = pandas.DataFrame()  # Initialize an empty DataFrame to store combined data
    tsv_files = glob.glob(documents)  ## The directory should probably be specified in the function below. Because sometimes you want one file, other times a group of files (see "### Smartthings tool" in group assignment)
    for file in tsv_files:
        df = pandas.read_csv(file, sep='\t')  # Read the file as a DataFrame with tab separator
        combined_df = pandas.concat([combined_df, df], ignore_index=True)  # Concatenate the DataFrame
    combined_df = combined_df.drop_duplicates # Remove duplicates (in function)
    combined_df.rename(columns={'epoch':'time'}) # Rename column (in function), really needed??
    return combined_df

## Still work to do...
input = input("This tool is meant to insert TSV files in the HomeMessages dataset. Press '--help' or '-h' for the options and arguments of this tool.")
    if input == "smartthings.py -d*" and input == "*data/smartthings*":
        database = tuple(input.split())[2] #Find database where the data_output should be loaded into
        data_output = cleanuptsv(tuple(input.split())[3]) # Find the tsv-documents in 'input', and clean the data (cleanuptsv function)
        ## Still missing: How to add the data-output to the home_messages_db and creating the instance
    elif input == "--help" or input == "-h":
       print("Usage: smartthings.py [OPTIONS] smartthingsLog.1.tsv [smartthingsLog.2.tsv...]. Output options: -d DBURL insert into the project database (DBURL is a SQLAlchemy database URL)")
    else:
        print("Your input is not clear for this tool to use. It is politely suggested to reread options and arguments of this tool.") 


## HOW 'input=input("This...)' SHOULD WORK, STATED BY THE GROUP ASSIGNMENT
#For example, to load the data from the file `smartthings/smartthings.202301.tsv` into the database `myhome.db` use the command:

#```bash
#smartthings.py -d sqlite:///myhome.db smartthings/smartthings.202301.tsv
#```

#And to load the data from all the files starting with `smartthings/smartthings.` into the database `myhome.db` use the command:

#```bash
#smartthings.py -d sqlite:///myhome.db smartthings/smartthings.*