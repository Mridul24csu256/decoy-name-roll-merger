import streamlit as st
import pandas as pd

st.title("Merge Name and Roll Number from Excel")

# File uploader
uploaded_file = st.file_uploader("Upload your Excel file (.xlsx)", type=["xlsx"])

if uploaded_file:
    try:
        # Read only Sheet1
        df = pd.read_excel(uploaded_file, sheet_name="Sheet1")
        
        # Normalize column names to lowercase to avoid case issues
        df.columns = [col.lower() for col in df.columns]

        # Check if required columns exist
        if "name" in df.columns and "rollno" in df.columns:
            # Merge columns
            df["name_rollno"] = df["name"].astype(str) + " " + df["rollno"].astype(str)

            # Keep only the merged column
            result = df[["name_rollno"]]

            # Display result
            st.success("✅ Columns merged successfully!")
            st.dataframe(result)

            # Download button
            result_file = "merged_output.xlsx"
            result.to_excel(result_file, index=False)
            st.download_button(
                label="Download Merged Excel",
                data=open(result_file, "rb"),
                file_name="merged_output.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        else:
            st.error("⚠️ Columns 'name' and/or 'rollno' not found in Sheet1.")

    except Exception as e:
        st.error(f"Error reading Excel file: {e}")
