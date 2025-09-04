import openpyxl

# 1. Load your Excel file
file_name = 'your_file.xlsx'  # <-- Replace with your file name
wb = openpyxl.load_workbook(file_name)
sheet = wb.active  # Or wb['SheetName'] if you know the sheet

# 2. Find the first empty column to put merged data
max_col = sheet.max_column
new_col = max_col + 1  # next empty column
sheet.cell(row=1, column=new_col).value = "Name_Roll"  # header

# 3. Merge Name (A) and Roll (B) into the new column
for row in range(2, sheet.max_row + 1):  # assuming row 1 is headers
    name = sheet[f"A{row}"].value
    roll = sheet[f"B{row}"].value
    if name is not None and roll is not None:
        sheet.cell(row=row, column=new_col).value = f"{name} {roll}"

# 4. Save the updated Excel file
wb.save('your_file_merged.xlsx')
print(f"Done! Merged column added as column {new_col} in 'your_file_merged.xlsx'.")
