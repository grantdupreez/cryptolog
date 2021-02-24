import pandas as pd
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import warnings
from datetime import datetime
from datetime import timedelta
import yfinance as yf
import lxml as xml
from money import Money
from pandas_datareader import data as pdr

st.title("Cryptocurrency Valuation Repoting Tool")

def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]

crypt_total = 0

uploaded_file = st.sidebar.file_uploader("Upload your portfolio file",type=['CSV'])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, header=[0])
    df.head()

    warnings.filterwarnings('ignore')
    
    for i in df.index:
        df.at[i, "Price"] = get_current_price(df.at[i, 'Symbol'])
        df.at[i, "Value"] = df.at[i, 'Price'] * df.at[i, 'Holding']
        crypt_total = crypt_total + df.at[i, 'Value']
        
    st.write(df)
    
    st.write('Holding value: ' + str(("%.2f" % crypt_total)))

    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    st.write("Date and time:",date_time)
