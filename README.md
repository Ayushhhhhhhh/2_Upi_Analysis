# UPI Transaction Growth Analysis for India

## Project Overview

This project presents a comprehensive analysis of the exponential growth of the Unified Payments Interface (UPI) in India, using monthly transaction data from January 2018 to December 2023. The analysis covers the complete data lifecycle:

- **Data Cleaning:** Preparation and cleansing of the raw dataset for analysis.
- **Exploratory Data Analysis (EDA):** Identification of major trends and patterns.
- **Feature Engineering:** Creation of additional features to enhance forecasting accuracy.
- **Time-Series Forecasting:** Prediction of future growth using statistical and machine learning methods.
- **Visualization:** Interactive dashboard built in Power BI to showcase insights.

---

## Dashboard Showcase

An interactive dashboard was developed in Power BI to visualize key trends, KPIs, and forecasts.

> **Note:** Due to Power BI licensing restrictions for personal accounts, a public live link cannot be generated. The dashboard design and functionality are demonstrated in the provided `.pbix` file.

**Final Dashboard Preview:**

![UPI India - Digital Payments Growth Analysis](Dashboard.jpg)

*(Above: The Power BI dashboard visualizes total transaction volume, total value, average transaction value, year-wise growth, forecasts, and key insights.)*

---

## Key Insights

- **Explosive Growth:** Transaction volumes increased by over **7,860%** from the start of 2018 to the end of 2023, signifying mass-market adoption.
- **Shift in Payment Behavior:** The average transaction value halved since 2018, indicating a move towards smaller, everyday payments.
- **Pandemic Acceleration:** The highest rate of adoption occurred during the pandemic (2020–2021), cementing UPI as essential digital infrastructure.
- **Continued Expansion:** The most recent year-over-year growth rate remains strong at **53.5%**, showing ongoing robust expansion.
- **Seasonal Patterns:** Q4 (Oct–Dec) consistently shows the highest transaction volumes, aligning with festive season spending.

---

## Running The Project

1. **Install Dependencies:**

   After downloading the project files, navigate to the main project folder in your terminal. Ensure you have Python 3 installed, then run:

   ```
   pip install -r requirements.txt
   ```

2. **Run the Analysis Script:**

   Execute the analysis script to perform data cleaning and generate processed data in the `data/` folder:

   ```
   python upi_analysis.py
   ```

3. **Explore the Dashboard:**

   Open the `UPI_Analysis_Dashboard.pbix` file in the `dashboard/` folder using [Power BI Desktop](https://powerbi.microsoft.com/en-us/desktop/) to interactively explore the visualizations.

---

## Project Structure

```
UPI_Analysis_Project/
│
├── data/              # Raw and processed data files
├── dashboard/         # Power BI .pbix file and visuals
├── sql/               # SQL script for database setup
├── upi_analysis.py    # Main Python script for analysis & forecasting
├── requirements.txt   # Python dependencies
└── README.md          # Project overview and documentation
```

---

## License

This project is provided for educational and analytical purposes. Please check individual file headers for any additional licensing notes.

---

## Contact

For questions or feedback, please open an issue or contact the project maintainer.
