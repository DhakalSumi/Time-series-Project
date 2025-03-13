# app/config.py

# Directory paths for data and model files
DATA_PATH = "/Users/sums/Documents/Masterschool/Time Series/retail_demand_forecast/data/"  # Path to the directory containing the raw data files
MODEL_PATH = '/Users/sums/Documents/Masterschool/Time Series/retail_demand_forecast/model/'  # Path to the directory containing the model files

# Google Drive file IDs for each dataset
# Replace these with actual file IDs from Google Drive where the datasets are stored
your_file_id_for_stores_csv = '1TxV_9g9G4pRMEAkrLZQPcM_uYkds_qp3'  # ID for stores data CSV
your_file_id_for_items_csv = '1QexzIcT6V1fCTbhnZpIbLJcKxhqIwfos'  # ID for items data CSV
your_file_id_for_transactions_csv = '1Raewkx6GtFp4QJ1IqZKQhAvufvmYAO6n'  # ID for transactions data CSV
your_file_id_for_oil_csv = '1DVzoJMfpiDyyTwRH-SapGJEptKl4ldWL'  # ID for oil prices data CSV
your_file_id_for_holidays_csv = '1TSC7zJx6iVweL1ssCzTtAUgSjqN2eCF-'  # ID for holidays data CSV
your_file_id_for_train_csv = '1zaQFSLhPLOEFn6uRXY4KyKQOv7WOiHrE'  # ID for training data CSV

# Google Drive links for each dataset
# These links are dynamically constructed using the file IDs, making it easy to download the data
GOOGLE_DRIVE_LINKS = {
    "stores": f"https://drive.google.com/uc?id={your_file_id_for_stores_csv}",  # Link for stores data
    "items": f"https://drive.google.com/uc?id={your_file_id_for_items_csv}",  # Link for items data
    "transactions": f"https://drive.google.com/uc?id={your_file_id_for_transactions_csv}",  # Link for transactions data
    "oil": f"https://drive.google.com/uc?id={your_file_id_for_oil_csv}",  # Link for oil prices data
    "holidays_events": f"https://drive.google.com/uc?id={your_file_id_for_holidays_csv}",  # Link for holidays data
    "train": f"https://drive.google.com/uc?id={your_file_id_for_train_csv}"  # Link for training data
}

# Google Drive link for the model
# Replace the file ID below with the actual file ID for the XGBoost model saved in Google Drive
your_file_id_for_xgboost_model_xgb = "1-4tS6mHbkuPiYctX7Mh6Y9rJk9hiPHy-"  # ID for the XGBoost model file

# Google Drive link for the model file
GOOGLE_DRIVE_LINKS_MODELS = {
    "xgboost_model": f"https://drive.google.com/uc?id={your_file_id_for_xgboost_model_xgb}"  # Link for the XGBoost model
}
