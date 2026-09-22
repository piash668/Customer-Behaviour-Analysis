import pandas as pd
from sqlalchemy import create_engine

# ==============================================================================
# Project: Customer Shopping Behavior Analysis
# Script: Data Cleaning, Feature Engineering, and SQL Database Ingestion
# Author: Piash Barua
# ==============================================================================

# Connect python with the transactional CSV dataset
df = pd.read_csv('customer_shopping_behavior.csv')

# ------------------------------------------------------------------------------
# Step 1: Missing Data Imputation
# ------------------------------------------------------------------------------
# Impute missing values in the 'Review Rating' column using the 
# median rating of each respective product category to maintain data integrity.
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(
    lambda x: x.fillna(x.median())
)

# ------------------------------------------------------------------------------
# Step 2: Column Standardization
# ------------------------------------------------------------------------------
# Convert all column headers to lowercase and replace spaces with underscores 
# to comply with SQL database naming standards.
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')
df = df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'})

# ------------------------------------------------------------------------------
# Step 3: Feature Engineering - Age Groups & Purchase Frequency
# ------------------------------------------------------------------------------
# Categorize customers into quartiles based on age
labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels=labels)

# Map text purchase frequency descriptions to numerical days for deeper time-series analysis
frequency_mapping = {
    'fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)

# ------------------------------------------------------------------------------
# Step 4: Redundancy Check & Cleanup
# ------------------------------------------------------------------------------
# Drop the redundant 'promo_code_used' column as it duplicates 'discount_applied' logic
df = df.drop(columns=['promo_code_used'])

# ------------------------------------------------------------------------------
# Step 5: Database Connection & Ingestion
# ------------------------------------------------------------------------------
# Define SQL Server connection parameters using Windows Authentication
server = r'DESKTOP-8LOAKQG\SQLEXPRESS'
database = 'customer_behaviour'
driver = 'ODBC Driver 17 for SQL Server'

# Create the SQLAlchemy connection engine
engine = create_engine(
    f'mssql+pyodbc://@{server}/{database}?driver={driver}&trusted_connection=yes'
)

# Upload the cleaned DataFrame into the SQL Server table named 'customer_data'
df.to_sql('customer_data', con=engine, if_exists='replace', index=False)

print('Data successfully cleaned, formatted, and uploaded to the SQL Server database!')