import pandas as pd

# Load your Excel file
file_path = "filtered_attendance.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1_Students")

# Merge name and roll no into a new column with a space
df["name_roll"] = df["name"].astype(str) + " " + df["roll no"].astype(str)

# (Optional) If you want only the merged column + department:
# df = df[["name_roll", "department"]]

# Save back to Excel
output_file = "filtered_attendance_with_name_roll.xlsx"
df.to_excel(output_file, index=False)

print("File saved as:", output_file)
