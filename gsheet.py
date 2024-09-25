# import streamlit as st
# from streamlit_gsheets import GSheetsConnection

# url = "https://docs.google.com/spreadsheets/d/1uYljw94G3ztdqVg5CTz9hCHdj8EFcFQfVyn5SEVjP-A/edit?usp=sharing"

# conn = st.connection("gsheets", type=GSheetsConnection)

# data = conn.read(spreadsheet=url, usecols=[0, 1])
# st.dataframe(data)

import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1uYljw94G3ztdqVg5CTz9hCHdj8EFcFQfVyn5SEVjP-A/edit?usp=sharing"

# Initialize the connection
conn = st.connection("gsheets", type=GSheetsConnection)

# Sample data to write to Google Sheets
data_to_write = pd.DataFrame({
    'Column1': ['Data1', 'Data2', 'Data3'],
    'Column2': ['Value1', 'Value2', 'Value3']
})

# Specify the sheet name (Sheet2) to write data
conn.write(spreadsheet=url, data=data_to_write)

st.write("Data written successfully to Sheet2!")

