
import pandas 
import glob
#from home_messages_db import HomeMessagesDB


def cleanuptsv(documents):
    combined_df = pandas.DataFrame()  # Initialize an empty DataFrame to store combined data
    tsv_files = glob.glob(documents)  ## The directory should probably be specified in the function below. Because sometimes you want one file, other times a group of files (see "### Smartthings tool" in group assignment)
    for file in tsv_files:
        df = pandas.read_csv(file, sep='\t')  # Read the file as a DataFrame with tab separator
        combined_df = pandas.concat([combined_df, df], ignore_index=True)  # Concatenate the DataFrame
    combined_df = combined_df.drop_duplicates # Remove duplicates (in function)
    #combined_df.rename(columns={'epoch':'time'}) # Rename column (in function), really needed??
    return combined_df


import pandas 
import glob
#from home_messages_db import HomeMessagesDB

while True:
    input_user = input("This tool is meant to insert TSV files in the HomeMessages dataset. Press '--help' or '-h' for the options and arguments of this tool.")
    
    if input_user == "smartthings.py -d*" and input_user == "*data/smartthings*":
        input_split = input_user.split()
        database = input_split[2]
        tsv_files = input_split[3]
        for documents in tsv_files:
            data_output = cleanuptsv(documents)
            ## Question marks
        #database = tuple(input.split())[2] #Find database where the data_output should be loaded into
        #data_output = cleanuptsv(tuple(input.split())[3]) # Find the tsv-documents in 'input', and clean the data (cleanuptsv function)
        
        break # Exit the loop
        ## Still missing: How to add the data-output to the home_messages_db and creating the instance
    elif input_user == "--help" or input_user == "-h":
        print("Usage: smartthings.py [OPTIONS] smartthingsLog.1.tsv [smartthingsLog.2.tsv...]. Output options: -d DBURL insert into the project database (DBURL is a SQLAlchemy database URL)")
        continue # Start loop over
    else:
        print("Your input is not clear for this tool to use. You are redirected to the start of this tool.") 
        continue # Start loop over

## HOW 'input=input("This...)' SHOULD WORK, STATED BY THE GROUP ASSIGNMENT
#For example, to load the data from the file `smartthings/smartthings.202301.tsv` into the database `myhome.db` use the command:

#```bash
#smartthings.py -d sqlite:///myhome.db smartthings/smartthings.202301.tsv
#```

#And to load the data from all the files starting with `smartthings/smartthings.` into the database `myhome.db` use the command:

#```bash
#smartthings.py -d sqlite:///myhome.db smartthings/smartthings.*
