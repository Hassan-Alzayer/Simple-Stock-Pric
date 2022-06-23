import yfinance as yf
import streamlit as st

st.write(" - Welcome to my app - ")

ticker = 'BTC-USD'
data = yf.Ticker(ticker)
ticker_data = data.history(period = '1d', start='2010-1-1',end = '2020-1-1')
st.write(" - Closing price - ")


st.line_chart(ticker_data.Close)
st.write(" - Volume - ")
st.line_chart(ticker_data.Volume)

