import pandas as pd
import datetime as dt
import glob
import click
from home_messages_db import HomeMessagesDB


def read_tsv_files(directory):
    tsv_files = glob.glob(directory + "/*.tsv")  # Get a list of all .tsv files in the directory
    combined_df = pd.DataFrame()  # Initialize an empty DataFrame to store combined data
    for file in tsv_files:
        df = pd.read_csv(file, sep='\t')  # Read the file as a DataFrame with tab separator
        combined_df = pd.concat([combined_df, df], ignore_index=True)  # Concatenate the DataFrame
    return combined_df


directory_path = "C:\\Users\\HP\\Desktop\\Python\\Group_assignment\\data\\smartthings\\smarthings.tsv"

combined_dataframe = read_tsv_files(directory_path)

# Now you have a single DataFrame containing data from all TSV files in the directory
combined_dataframe


def remove_duplicates(dataframe):
    # Remove duplicates based on all columns
    deduplicated_df = dataframe.drop_duplicates()
    return deduplicated_df


deduplicated_dataframe = remove_duplicates(combined_dataframe)
deduplicated_dataframe

deduplicated_dataframe=deduplicated_dataframe.rename(columns={'epoch':'time'})
deduplicated_dataframe

@click.command()
@click.option('-d', '--dburl', required=True, help='Insert into the project database (DBURL is a SQLAlchemy database URL)')
@click.argument('files', nargs=-1, type=click.Path(exists=True))
def insert_data(dburl, files):
    """Insert data from SmartThings files into the database."""
    db = HomeMessagesDB(dburl)
    for file in files:
        try:
            # Read data from file
            combined_dataframe = read_tsv_files(file)

            # Remove duplicates
            deduplicated_dataframe = remove_duplicates(combined_dataframe)

            # Rename columns
            deduplicated_dataframe = deduplicated_dataframe.rename(columns={'epoch': 'time'})

            # Insert data into the database
            db.insert_data(deduplicated_dataframe)
            click.echo(f"Data from {file} inserted into the database.")
        except Exception as e:
            click.echo(f"Error inserting data from {file}: {str(e)}", err=True)

if __name__ == '__main__':
    insert_data()
