import pandas as pd

# Load data
df = pd.read_csv("stock_data.csv")
print("Original shape:", df.shape)

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Drop rows with invalid or missing dates
df = df.dropna(subset=['Date'])

# Sort by date
df = df.sort_values(by='Date')

# Drop duplicates and NaNs
df = df.drop_duplicates()
df = df.dropna()

# Set 'Date' as index
df.set_index('Date', inplace=True)

# Save cleaned data
df.to_csv("cleaned_stock_data.csv")

print("Cleaned shape:", df.shape)
print("✅ Data cleaned and saved to 'cleaned_stock_data.csv'")
