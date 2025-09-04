import pandas as pd
import streamlit as st
from io import BytesIO

st.title("Name + RollNo Merger")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file is not None:
    # Read uploaded Excel
    df = pd.read_excel(uploaded_file, sheet_name="Sheet1_Students")

    # Merge name and roll no into one column
    df["name_roll"] = df["name"].astype(str) + " " + df["roll no"].astype(str)

    # Keep only merged column + department (optional)
    # df = df[["name_roll", "department"]]

    # Save to memory
    output = BytesIO()
    df.to_excel(output, index=False)
    output.seek(0)

    st.download_button(
        label="Download Updated Excel",
        data=output,
        file_name="merged_name_roll.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    st.success("File processed successfully ✅")
