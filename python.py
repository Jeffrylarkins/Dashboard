# import streamlit as st
# import pandas as pd

# # Title
# st.title("Excel Column Operations App")

# # Upload Excel file
# uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

# if uploaded_file is not None:
#     # Read Excel file
#     excel_data = pd.read_excel(uploaded_file)

#     # Display uploaded data
#     st.subheader("Uploaded Data")
#     st.dataframe(excel_data)

#     # Select operation
#     operation = st.selectbox("Select an operation", ["Addition", "Subtraction"])

#     # Select columns
#     selected_columns = st.multiselect("Select columns to operate on", excel_data.columns)

#     if len(selected_columns) < 2:
#         st.warning("Please select at least 2 columns for the operation.")
#     else:
#         # Perform operation
#         if operation == "Addition":
#             result = excel_data[selected_columns].sum(axis=1)
#         else:
#             result = excel_data[selected_columns[0]] - excel_data[selected_columns[1]]

#         # Display result
#         st.subheader("Result")
#         st.dataframe(result)

# import streamlit as st
# import pandas as pd
# from fpdf import FPDF

# def save_as_pdf(data_series, filename):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)

#     for index, value in data_series.iteritems():
#         pdf.cell(0, 10, txt=f"Row {index}: {value}", ln=True)

#     pdf.output(filename)

#     st.write('Done!! Saveds as pdf')

# # Title
# st.title("Excel Column Operations App")


# # Upload Excel file
# uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls","csv])

# if uploaded_file is not None:
#     # Read Excel file
#     excel_data = pd.read_excel(uploaded_file)

#     # Display uploaded data
#     st.subheader("Uploaded Data")
#     st.dataframe(excel_data)

#     # Select operation
#     operation = st.selectbox("Select an operation", ["Addition", "Subtraction"])

#     # Select columns
#     selected_columns = st.multiselect("Select columns to operate on", excel_data.columns)

#     if len(selected_columns) < 2:
#         st.warning("Please select at least 2 columns for the operation.")
#     else:
#         # Perform operation
#         if operation == "Addition":
#             result = excel_data[selected_columns].sum(axis=1)
#         else:
#             result = excel_data[selected_columns[0]] - excel_data[selected_columns[1]]

#         # Display result
#         st.subheader("Result")
#         st.dataframe(result)

#         # Option to save result as PDF
#         if st.button("Save Result as PDF"):
#             save_as_pdf(result, "result.pdf")

# # Function to save a Series as a PDF using FPDF

import streamlit as st
import pandas as pd
from fpdf import FPDF

# Function to save a Series as a PDF using FPDF
def save_as_pdf(data_series, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for index, value in data_series.iteritems():
        pdf.cell(0, 10, txt=f"Row {index}: {value}", ln=True)

    pdf.output(filename)

    st.write('Done!! Download success')

# Title
st.title("Excel/CSV Column Operations App")

# Upload Excel or CSV file
uploaded_file = st.file_uploader("Upload an Excel or CSV file", type=["xlsx", "xls", "csv"])

if uploaded_file is not None:
    # Read Excel or CSV file
    if uploaded_file.name.endswith('.csv'):
        excel_data = pd.read_csv(uploaded_file)
    else:
        excel_data = pd.read_excel(uploaded_file)

    # Display uploaded data
    st.subheader("Uploaded Data")
    st.dataframe(excel_data)

    # Select operation
    operation = st.selectbox("Select an operation", ["Addition", "Subtraction"])

    # Select columns
    selected_columns = st.multiselect("Select columns to operate on", excel_data.columns)

    if len(selected_columns) < 2:
        st.warning("Please select at least 2 columns for the operation.")
    else:
        # Perform operation
        if operation == "Addition":
            result = excel_data[selected_columns].sum(axis=1)
        else:
            result = excel_data[selected_columns[0]] - excel_data[selected_columns[1]]

        # Display result
        st.subheader("Result")
        st.dataframe(result)

        # Option to save result as PDF
        if st.button("Save Result as PDF"):
            save_as_pdf(result, "result.pdf")





