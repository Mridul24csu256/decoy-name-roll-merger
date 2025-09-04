import streamlit as st
import pandas as pd

st.title("Merge Name and Roll Number")

# File uploader
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file:
    try:
        # Read only Sheet1
        df = pd.read_excel(uploaded_file, sheet_name="Sheet1")
        
        # Check if required columns exist
        if "name" in df.columns and "rollno" in df.columns:
            df["name_rollno"] = df["name"].astype(str) + " " + df["rollno"].astype(str)
            result = df[["name_rollno"]]

            # Display result
            st.write("✅ Merged Column:")
            st.dataframe(result)

            # Allow download
            result_file = "merged_output.xlsx"
            result.to_excel(result_file, index=False)
            st.download_button(
                label="Download Merged Excel",
                data=open(result_file, "rb"),
                file_name="merged_output.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        else:
            st.error("⚠️ 'name' and/or 'rollno' column not found in Sheet1")

    except Exception as e:
        st.error(f"Error reading Excel file: {e}")
