import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import yfinance as yf 
import datetime
from utils import * 

min_date = datetime.date(1990, 1, 2)
today = datetime.date.today()

start_date = st.date_input(
  label = "Start Date", 
  min_value = min_date, 
  max_value = today,
  value = today - datetime.timedelta(days = 18*31)
)

end_date = st.date_input(
  label = "End Date", 
  min_value = min_date, 
  max_value = today, 
  value = today - datetime.timedelta(days = 1)
)

def date_filter_format(date): 
    return "-".join([str(date.year), str(date.month), str(date.day)])

start_date_cleaned = date_filter_format(start_date) 
end_date_cleaned = date_filter_format(end_date) 

# Define the labels for your checkboxes
checkbox_labels = get_checkbox_column_labels()
tickers = get_sector_etf_tickers() 

########################## Plotting Sector ETFs ##########################



##################### Check Boxes to Include in Opt ######################

# Create a dictionary to hold the status of each checkbox
checkbox_status = {}

# Create a 4-column layout
col1, col2, col3, col4 = st.columns(4)

# Use a list to store your columns
columns = [col1, col2, col3, col4]

# Loop through each column and place three checkboxes in each,
# also storing their status in the checkbox_status dictionary
for i, col in enumerate(columns):
    with col:
        for label in checkbox_labels[i]:
            # Creating a checkbox and storing its return value
            if label == "": 
                continue
            else: 
                checkbox_status[label] = st.checkbox(label)

to_pull = [label.split(" ")[0] for label, status in checkbox_status.items() if status]
indices_to_pull = {label: i for i, label in enumerate(to_pull)}

historical_data = [] 

st.write(to_pull)

for ticker in to_pull: 
    df_ticker = yf.download(tickers=[ticker], start=start_date_cleaned, end=end_date_cleaned).reset_index()
    historical_data.append((ticker, df_ticker[["Date", "Close"]])) 

if to_pull is not None: 
    chart = alt.Chart(historical_data[indices_to_pull["XLU"]][1]).mark_line(color='red').encode(
        x='Date',
        y="Close",
        tooltip=['Date', 'Close']
    )
    st.altair_chart(chart, use_container_width=True)

