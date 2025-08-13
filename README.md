UPI Transaction Growth Analysis for India
Project Overview
This project provides a comprehensive analysis of the exponential growth of the Unified Payments Interface (UPI) in India, utilizing monthly data from January 2018 to December 2023. The analysis covers the entire data lifecycle: data cleaning, exploratory data analysis (EDA), feature engineering, time-series forecasting, and visualization in an interactive Power BI dashboard.

Dashboard Showcase
An interactive dashboard was built in Power BI to visualize key trends, KPIs, and forecasts.

Note: Due to Power BI licensing for personal accounts, a public live link cannot be generated. The showcase below demonstrates the dashboard's design and functionality.

Final Dashboard
<img width="1121" height="632" alt="image" src="https://github.com/user-attachments/assets/0eb9e9f8-0e9d-4127-8f38-3e984dc97fc2" />








Key Insights
Transaction volumes have exploded by over 7,860% from the start of 2018 to the end of 2023, signifying mass-market adoption.

The average transaction value has been cut in half since 2018, indicating a fundamental shift towards smaller, everyday payments.

The highest acceleration in adoption occurred during the pandemic (2020-2021), establishing UPI as essential digital infrastructure.

The most recent year-over-year growth rate remains strong at 53.5%, showing continued, powerful expansion.

Data consistently shows the highest transaction volumes in the fourth quarter (Oct-Dec), aligning with festive season spending.

Running The Project
1. Install Dependencies:
After downloading the project files, navigate to the main project folder in your terminal. Ensure you have Python 3 installed. Then, run the following command to install the required libraries:

pip install -r requirements.txt

2. Run the Analysis Script:
Execute the Python script to perform the data cleaning and analysis. This will generate the processed data file in the data/ folder.

python upi_analysis.py

3. Explore the Dashboard:
Open the UPI_Analysis_Dashboard.pbix file located in the dashboard/ folder using Power BI Desktop to explore the interactive dashboard.

Project Structure
UPI_Analysis_Project/
│
├── data/              # Contains raw and processed data files
├── dashboard/         # Contains Power BI file and visuals
├── sql/               # Contains the SQL script for database setup
├── upi_analysis.py    # Main Python script for analysis and forecasting
├── requirements.txt   # List of Python dependencies
└── README.md          # Project overview and documentation


