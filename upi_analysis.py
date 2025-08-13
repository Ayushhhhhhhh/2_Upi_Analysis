# ==============================================================================
# Project: UPI Transaction Analysis and Forecasting (Advanced)
# Author: [Ayush Singhal]
# Date: August 13, 2025
# Description: This script performs an advanced analysis of UPI transaction data,
#              including cleaning, detailed EDA with seasonality analysis,
#              time-series forecasting, and model performance evaluation.
# ==============================================================================

# --- 1. Import Necessary Libraries ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error
from statsmodels.tsa.seasonal import seasonal_decompose
import warnings

warnings.filterwarnings('ignore')

# --- 2. Data Loading and Initial Cleaning ---

def load_and_clean_data(filepath):
    """
    Loads the raw UPI data, cleans column names, handles data types,
    and creates a proper Datetime index.
    """
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found. Please ensure it is in the correct directory.")
        return None

    df.columns = ['Year', 'Month', 'TransactionVolume_Cr', 'TransactionValue_RsCr']
    df['Date'] = pd.to_datetime(df['Year'].astype(str) + '-' + df['Month'].astype(str) + '-01')
    df.set_index('Date', inplace=True)
    df['TransactionVolume_Cr'] = pd.to_numeric(df['TransactionVolume_Cr'], errors='coerce')
    df['TransactionValue_RsCr'] = pd.to_numeric(df['TransactionValue_RsCr'], errors='coerce')
    df.dropna(inplace=True)
    print("--- Data Loaded and Cleaned Successfully ---")
    return df

# --- 3. Feature Engineering ---

def create_features(df):
    """
    Engineers new features from the existing data to aid analysis.
    """
    df['AvgTransactionValue_Rs'] = round((df['TransactionValue_RsCr']) / (df['TransactionVolume_Cr']), 2)
    df['YoY_Volume_Growth_%'] = round(df['TransactionVolume_Cr'].pct_change(12) * 100, 2)
    print("\n--- Feature Engineering Complete ---")
    return df

# --- 4. Exploratory Data Analysis (EDA) ---

def perform_eda(df):
    """
    Generates and saves key visualizations for the EDA report.
    """
    print("\n--- Starting Exploratory Data Analysis (EDA) ---")
    plt.style.use('seaborn-v0_8-whitegrid')

    # a. Plot Transaction Volume and Value Over Time (Dual Axis)
    # [This plot remains the same as it's fundamental]
    fig, ax1 = plt.subplots(figsize=(14, 7))
    ax1.plot(df.index, df['TransactionVolume_Cr'], color='tab:blue', marker='o', label='Transaction Volume (Cr)')
    ax1.set_xlabel('Date', fontsize=12)
    ax1.set_ylabel('Transaction Volume (in Crores)', color='tab:blue', fontsize=12)
    fig.tight_layout()
    plt.title('UPI Transaction Volume Growth', fontsize=16, fontweight='bold')
    plt.savefig('upi_volume_growth.png', dpi=300)
    plt.show()

    # b. NEW: Seasonal Heatmap of Transaction Volume
    # This helps visualize if certain months consistently have higher/lower volume.
    pivot_table = df.pivot_table(values='TransactionVolume_Cr', index=df.index.month, columns=df.index.year)
    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot_table, cmap='YlGnBu', annot=True, fmt=".0f", linewidths=.5)
    plt.title('Monthly UPI Transaction Volume (in Crores) - Heatmap', fontsize=16, fontweight='bold')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Month', fontsize=12)
    plt.savefig('upi_seasonal_heatmap.png', dpi=300)
    plt.show()
    print("Saved 'upi_seasonal_heatmap.png'")

    # c. NEW: Time-Series Decomposition
    # This statistically breaks down the data into its components.
    decomposition = seasonal_decompose(df['TransactionVolume_Cr'], model='multiplicative', period=12)
    fig = decomposition.plot()
    fig.set_size_inches(14, 10)
    fig.suptitle('Time-Series Decomposition of UPI Volume', fontsize=16, fontweight='bold', y=1.02)
    plt.savefig('upi_decomposition_plot.png', dpi=300)
    plt.show()
    print("Saved 'upi_decomposition_plot.png'")

# --- 5. Time-Series Forecasting with Prophet & Model Evaluation ---

def forecast_transactions(df):
    """
    Uses Facebook Prophet to forecast future transaction volumes and evaluates model performance.
    """
    print("\n--- Starting Time-Series Forecasting & Evaluation ---")
    
    prophet_df = df.reset_index()[['Date', 'TransactionVolume_Cr']].rename(columns={'Date': 'ds', 'TransactionVolume_Cr': 'y'})

    # Split data for evaluation: Train on data up to the last 12 months, test on the last 12.
    train = prophet_df.iloc[:-12]
    test = prophet_df.iloc[-12:]

    # Initialize and fit the model on the training data
    model = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False, seasonality_mode='multiplicative')
    model.fit(train)

    # Predict on the test set for evaluation
    test_forecast = model.predict(test[['ds']])

    # --- NEW: Evaluate the Model ---
    mae = mean_absolute_error(test['y'], test_forecast['yhat'])
    rmse = np.sqrt(mean_squared_error(test['y'], test_forecast['yhat']))
    print("\n--- Model Performance Evaluation (on last 12 months) ---")
    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f}\n")

    # Now, retrain the model on the FULL dataset for the final forecast
    full_model = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False, seasonality_mode='multiplicative')
    full_model.fit(prophet_df)
    
    future = full_model.make_future_dataframe(periods=24, freq='MS')
    final_forecast = full_model.predict(future)

    # Plot the final forecast
    fig = full_model.plot(final_forecast, figsize=(14, 8))
    plt.title('UPI Transaction Volume Forecast (Next 24 Months)', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Transaction Volume (in Crores)', fontsize=12)
    plt.savefig('upi_forecast_plot_final.png', dpi=300)
    plt.show()
    
    return final_forecast

# --- Main Execution Block ---
if __name__ == "__main__":
    raw_data_filepath = 'upi_raw_data.csv'
    df_cleaned = load_and_clean_data(raw_data_filepath)
    
    if df_cleaned is not None:
        df_featured = create_features(df_cleaned.copy())
        processed_filepath = 'upi_processed_data.csv'
        df_featured.reset_index().to_csv(processed_filepath, index=False)
        print(f"\nProcessed data saved to '{processed_filepath}'")
        
        perform_eda(df_featured)
        transaction_forecast = forecast_transactions(df_featured)
        
        forecast_filepath = 'upi_forecast_data.csv'
        transaction_forecast.to_csv(forecast_filepath, index=False)
        print(f"\nForecast data saved to '{forecast_filepath}'")
        
        print("\n--- Project Pipeline Complete! ---")

