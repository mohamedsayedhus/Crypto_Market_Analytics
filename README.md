## Crypto Market Analytics Pipeline

This project is an end-to-end data analytics pipeline that extracts cryptocurrency market data, transforms it, and loads it into Google Sheets / Excel for analysis and dashboarding.

The project follows a real-world ETL architecture with support for incremental loading, KPIs, and Pivot Table–ready outputs.

## Crypto_Market_Analytics/
│
├── extract.py              # Fetch crypto data from API
├── transform.py            # Data cleaning & KPI calculations
├── upload_to_gsheets.py    # Load data to Google Sheets (incremental)
├── main.py                 # Orchestrates the full pipeline
│
├── service_account.json    # Google Service Account credentials
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation


## Project Overview

The pipeline performs the following steps:

# Extract

Fetches crypto market data from a public API

Retrieves metrics such as price, market cap, volume, and percentage change

# Transform

Cleans and standardizes data

Calculates business KPIs

Adds a load_date column for incremental loading

# Load

Uploads data to Google Sheets

Supports first load and incremental load

Preserves column headers and schema

# Analyze

Data is ready for Excel / Google Sheets

Used for Pivot Tables, dashboards, and timelines
