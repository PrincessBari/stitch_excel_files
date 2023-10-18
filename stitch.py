import pandas as pd
import glob

# List all excel files in directory
file_list = glob.glob(r"filepath")

# Create an empty dataframe to store the merged data
merged_data = pd.DataFrame()

for i, file in enumerate(file_list):
    # Read data from sheet "X", skipping the first 4 rows for files other than the 1st one
    skip_rows = 4 if i > 0 else 0
    df = pd.read_excel(file, sheet_name="X", header=None, skiprows=skip_rows)

    # Append the data to the merged dataframe
    merged_data = merged_data.append(df, ignore_index=True) 

# Write the merged data to a new excel file
merged_data.to_excel("merged.xlsx", index=False)
