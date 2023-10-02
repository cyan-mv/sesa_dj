# make_excel.py

import pandas as pd

def generate_excel():
    # Sample data for the first table
    data1 = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']
    }

    # Sample data for the second table
    data2 = {
        'Product': ['Laptop', 'Phone', 'Tablet'],
        'Price': [1200, 800, 500],
        'Stock': [20, 15, 30]
    }

    # Create DataFrames
    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)

    # Specify the Excel file name
    excel_file = 'myapp/output_tables.xlsx'

    # Create a Pandas Excel writer object
    with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
        # Write the first DataFrame to the Excel file
        df1.to_excel(writer, sheet_name='Sheet1', index=False)

        # Write the second DataFrame to the Excel file, starting from column D
        df2.to_excel(writer, sheet_name='Sheet1', index=False, startcol=len(df1.columns) + 2)

    # Notify the user
    print(f"Excel file '{excel_file}' generated successfully.")

# If you want to run this script independently, you can call the function like this:
if __name__ == "__main__":
    generate_excel()
