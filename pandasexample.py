print('PART 1\n')
print('Load Module\n')
import pandas as pd
print('Load External File\n')
raw_sales = pd.read_csv('sales_data.csv')
print('Preview Structure\n')
print(raw_sales.head(3),raw_sales.tail(2),'\n')
print('Check Dimensions')
print(raw_sales.shape,'\n')
print('Run Diagnostics')
print(raw_sales.info(),'\n')
print('Statistical Overview')
print(raw_sales.describe(),'\n')
print(raw_sales.describe(include='all'),'\n')
print('Identify Anomalies')
print(raw_sales.isnull().sum(),'\n')
print(raw_sales.duplicated().sum(),'\n')

print('PART 2\n')
print('Deduplication\n')
cleaned_sales = raw_sales.drop_duplicates(keep='first').copy()
print(cleaned_sales.shape,'\n')

print('Impute Categorical Data\n')
cleaned_sales['Category'] = cleaned_sales['Category'].fillna('Uncategorized')
print(cleaned_sales)

print('Impute Numeric Data\n')
mean_price = cleaned_sales['UnitPrice'].mean()
cleaned_sales['UnitPrice'] = cleaned_sales['UnitPrice'].fillna(mean_price)
print(cleaned_sales,'\n')

print('Handle Remaining Units\n')
cleaned_sales['Quantity'] = cleaned_sales['Quantity'].fillna(1)
print(cleaned_sales,'\n')


print('PART 3\n')
print('Vectorized Calculation')
cleaned_sales['TotalRevenue'] = cleaned_sales['UnitPrice'] * cleaned_sales['Quantity']
print(cleaned_sales,'\n')

print('Label-Based Access\n')
print(cleaned_sales.loc[2:5,['OrderID','Category','TotalRevenue']],'\n')

print('Position-Based Access\n')
print(cleaned_sales.iloc[:,0:3],'\n')

print('PART 4\n')
print('Conditional Filtering\n')
print(cleaned_sales.query("(Category != 'Electronics') & (TotalRevenue > 100)"),'\n')

print('Group Aggregation\n')
print(cleaned_sales.groupby('Region')['TotalRevenue'].sum(),'\n')

cleaned_sales['OrderID'] = cleaned_sales['OrderID'].astype(int)
cleaned_sales['Quantity'] = cleaned_sales['Quantity'].astype(int)

cleaned_sales['UnitPrice'] = cleaned_sales['UnitPrice'].round(2)
cleaned_sales['TotalRevenue'] = cleaned_sales['TotalRevenue'].round(2)

cleaned_sales.to_csv(
    'cleanedSales.csv',
    index=False,
    encoding='utf-8',
    lineterminator='\n',
    float_format='%.2f'
)

print('Mean Unit Price:', mean_price)

print('\nCleaned Data:')
print(cleaned_sales.to_string(index=False))

print('\nRevenue by Region:')
print(cleaned_sales.groupby('Region')['TotalRevenue'].sum())
