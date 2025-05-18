# Stock Price Cleaning Project

This project provides a robust pipeline for loading and cleaning Yahoo stock price data, preparing it for time series forecasting and further financial analysis.

## Project Structure

- **`stock_data.csv`**: Raw input stock price data (downloaded from Yahoo Finance).
- **`clean_stock_data.py`**: Python script to process and clean the dataset.
- **`cleaned_stock_data.csv`**: Cleaned and processed output, ready for analysis.

## Cleaning Workflow

The cleaning script performs the following steps:
1. **Date Parsing**: Converts date columns to datetime objects for consistency.
2. **Handle Missing/Invalid Data**: Removes rows with missing values or invalid entries (e.g., negative prices, non-numeric values).
3. **Sort Chronologically**: Ensures data is sorted in ascending order by date.
4. **Remove Duplicates**: Drops any duplicate records based on date or other identifiers.
5. **Save Cleaned Data**: Outputs a new CSV file (`cleaned_stock_data.csv`) containing only valid, chronologically sorted records.

## Requirements

- Python 3.8+
- pandas

Install requirements:
```bash
pip install pandas
```

## How to Use

1. Place your raw Yahoo Finance CSV file as `stock_data.csv` in the project folder.
2. Run the cleaning script:
   ```bash
   python clean_stock_data.py
   ```
3. The cleaned data will be saved as `cleaned_stock_data.csv`.

## Customization

- You can update `clean_stock_data.py` to add or change cleaning rules (e.g., handle outliers, adjust column selection).
- To process different raw file names, modify the script’s input path accordingly.

## License

MIT License

---

**Ready to analyze your stock data? Start by running the cleaning script and build your models on a solid foundation!**
