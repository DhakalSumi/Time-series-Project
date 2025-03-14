# app/main.py
import streamlit as st  # Streamlit is used for creating the web interface
from app.config import DATA_PATH, MODEL_PATH  # Import paths for data and model
from data.data_utils import load_data, preprocess_input_data  # Import functions to load and preprocess data
from model.model_utils import load_model, predict  # Import functions to load the model and make predictions
import datetime  # Used for handling date inputs

def main():
    # Title of the Streamlit app
    st.title("Corporación Favorita Sales Forecasting")

    # Load data and model from the provided paths
    # This function loads datasets related to stores, items, transactions, oil prices, holidays, and training data
    df_stores, df_items, df_transactions, df_oil, df_holidays, df_train = load_data(DATA_PATH)
    # Load the pre-trained model from the specified path
    model = load_model(MODEL_PATH)

    # UI components for input selection
    # Store selection - for testing, limited to one store (store number 1)
    store_id = st.selectbox("Store", [1])  # For testing limit to one store
    # Item selection - for testing, limited to a few item numbers
    item_id = st.selectbox("Item", [564533, 838216, 582865, 364606])  # For testing limit to a few items

    # Set default and allowed date range for forecasting
    default_date = datetime.date(2014, 3, 1)  # Default date is March 1, 2014
    min_date = datetime.date(2013, 1, 1)  # Minimum date allowed is January 1, 2013
    max_date = datetime.date(2014, 6, 7)  # Maximum date allowed is June 7, 2014
    # Date input for selecting forecast date, within the range [min_date, max_date]
    date = st.date_input("Forecast Date", value=default_date, min_value=min_date, max_value=max_date)

    # When the user clicks the "Get Forecast" button
    if st.button("Get Forecast"):
        # Preprocess the input data to create a suitable format for the model
        input_data = preprocess_input_data(store_id, item_id, date, df_stores, df_items, df_train)
        # Use the model to predict sales based on the input data
        prediction = predict(model, input_data)
        # Display the predicted sales for the selected date
        st.write(f"Predicted Sales for {date}: {prediction[0]}")

# Ensure the script runs the main function if executed directly
if __name__ == "__main__":
    main()
