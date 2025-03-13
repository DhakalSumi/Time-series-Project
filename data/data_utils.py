# data/data_utils.py

import pandas as pd  # Import pandas for data manipulation and analysis
import os  # Import os to interact with the file system
import gdown  # Import gdown to download files from Google Drive
from app.config import DATA_PATH, GOOGLE_DRIVE_LINKS  # Import paths and links for data files
from sklearn.preprocessing import LabelEncoder  # Import LabelEncoder to encode categorical features

def download_file(file_path, url):
    """Downloads a file from Google Drive if it doesn't exist locally."""
    # Check if the file already exists locally
    if not os.path.exists(file_path):
        # If it doesn't exist, download the file from Google Drive using gdown
        gdown.download(url, file_path, quiet=False)
    else:
        # If the file already exists, print a message
        print(f"{file_path} already exists.")

def load_data(data_path=DATA_PATH):
    """Downloads necessary data from Google Drive and loads CSV files into DataFrames."""
    
    # Define the paths for all the required data files
    files = {
        "stores": f"{data_path}stores.csv",  # Path for stores data
        "items": f"{data_path}items.csv",  # Path for items data
        "transactions": f"{data_path}transactions.csv",  # Path for transactions data
        "oil": f"{data_path}oil.csv",  # Path for oil prices data
        "holidays_events": f"{data_path}holidays_events.csv",  # Path for holidays and events data
        "train": f"{data_path}train.csv"  # Path for training data
    }

    # Download the files if they don't already exist locally
    for key, file_path in files.items():
        download_file(file_path, GOOGLE_DRIVE_LINKS[key])

    # Load each downloaded CSV file into a pandas DataFrame
    df_stores = pd.read_csv(files["stores"])  # Stores data
    df_items = pd.read_csv(files["items"])  # Items data
    df_transactions = pd.read_csv(files["transactions"])  # Transactions data
    df_oil = pd.read_csv(files["oil"])  # Oil prices data
    df_holidays = pd.read_csv(files["holidays_events"])  # Holidays and events data
    
    # Load data only for stores in 'Pichincha' region
    # Get the list of store IDs for the state 'Pichincha'
    store_ids = df_stores[df_stores['state'] == 'Pichincha']['store_nbr'].unique()
    # Select the same items as for "Classical methods":
    item_ids = [564533, 838216, 582865, 364606]
    # Select data before April 2014
    max_date = '2014-04-01'

    # Initialize an empty list to hold filtered chunks
    filtered_chunks = []

    # Define the chunk size (number of rows per chunk)
    chunk_size = 10 ** 6  # Adjust based on your system's memory capacity

    # Read the CSV file in chunks
    for chunk in pd.read_csv(files["train"], chunksize=chunk_size):
        # Filter the chunk for the desired store IDs
        chunk_filtered = chunk[
            (chunk['store_nbr'].isin(store_ids)) & 
            (chunk['item_nbr'].isin(item_ids)) & 
            (chunk['date'] < max_date)
        ]
        # Append the filtered chunk to the list
        filtered_chunks.append(chunk_filtered)
        # Optional: Delete the chunk to free up memory
        del chunk

    # Concatenate all filtered chunks into a single DataFrame
    df_filtered = pd.concat(filtered_chunks, ignore_index=True)

    # Clean up to free memory
    del filtered_chunks

    # Group by date and aggregate sales
    df_filtered = df_filtered.groupby(['store_nbr', 'item_nbr', 'date']).sum()['unit_sales'].reset_index()

    # Return all the loaded DataFrames
    return df_stores, df_items, df_transactions, df_oil, df_holidays, df_filtered

import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)
