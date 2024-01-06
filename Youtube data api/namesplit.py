import pandas as pd

# Replace 'your_file.xlsx' with the actual path to your Excel file
excel_file_path = 'Tools Version 3.xlsx'

# Replace 'Sheet1' with the actual sheet name containing your data
sheet_name = 'Sheet1'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

# Replace 'Tool Name' with the actual column name containing the tool names
tool_name_column = 'Tool Name'

# Split the 'Tool Name' column based on the first space, hyphen, or colon
df['Tool Name'] = df[tool_name_column].str.split(' ', n=1).str[0]  # Split at the first space
# Or use the following lines for splitting at the first hyphen or colon
# df['Tool Name'] = df[tool_name_column].str.split('-', n=1).str[0]  # Split at the first hyphen
# df['Tool Name'] = df[tool_name_column].str.split(':', n=1).str[0]  # Split at the first colon

# Save the updated DataFrame to a new Excel file
# Replace 'output_file.xlsx' with the desired output file name
output_file_path = 'output_file.xlsx'
df.to_excel(output_file_path, index=False)

# Display the updated DataFrame
print(df)
