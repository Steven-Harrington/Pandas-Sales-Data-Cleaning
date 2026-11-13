# Sales Data Cleaning and Analysis Using Pandas

## Project Overview

This project demonstrates an introductory Extract, Transform, Load (ETL) workflow using Python and the Pandas library. The program imports a sales dataset, identifies data quality issues, cleans missing and duplicate records, performs basic sales analysis, and exports the cleaned data to a CSV file.

The project was developed as part of COS 380: Database Application Design at the University of Maine.

## Technologies Used

- Python
- Pandas
- CSV Files

## Project Features

### 1. Data Import and Inspection
- Imports sales data from a CSV file using Pandas.
- Previews the first and last records.
- Examines dataset dimensions, data types, and non-null values.
- Generates descriptive statistics for numerical and categorical data.
- Identifies missing values and exact duplicate records.

### 2. Data Cleaning
- Removes exact duplicate rows while keeping the first occurrence.
- Replaces missing category values with "Uncategorized".
- Replaces missing unit prices with the mean unit price.
- Replaces missing quantities with a default value of 1.

### 3. Feature Engineering
- Creates a `TotalRevenue` column by multiplying `UnitPrice` and `Quantity`.
- Demonstrates label-based and position-based data selection using `.loc[]` and `.iloc[]`.

### 4. Data Filtering and Aggregation
- Filters orders based on product category and total revenue.
- Groups sales by region to calculate total revenue for each region.

### 5. Data Export
- Converts order IDs and quantities to integers.
- Rounds numerical values to two decimal places.
- Exports the cleaned dataset to `cleanedSales.csv`.

## How to Run

1. Download or clone this repository.
2. Ensure Python is installed.
3. Install Pandas using:

   `pip install -r requirements.txt`

4. Keep `sales_data.csv` in the same directory as the Python script.
5. Run the program using:

   `python pandasexample.py`

The program displays the results of each processing stage and generates `cleanedSales.csv`.

## Data Cleaning Considerations

The program removes only exact duplicate rows, including comparisons of `OrderID`. Orders with different IDs are preserved even when their other sales attributes match.

Missing numerical values are replaced using mean imputation or a default quantity, following the original assignment requirements. In a real business environment, these assumptions would need to be evaluated before being applied to financial data.

## Learning Outcomes

Through this project, I gained experience with:

- Importing and inspecting structured datasets.
- Identifying and correcting data quality issues.
- Using Pandas for data transformation.
- Performing descriptive statistics and sales aggregation.
- Exporting processed data for further use.

## Author

Steven Harrington

Computer Science Student — University of Maine
