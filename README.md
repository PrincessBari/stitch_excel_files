# stitch_excel_files

In October 2023, I had to stitch together around 20 excel files into one file. In each original file, the first
2 rows contained the file name and metadata, the 3rd row was blank, and the 4th row had the column headers. So I 
wrote code that said to take everything from the 1st file but only the data starting from row 5 in each subsequent file. 
