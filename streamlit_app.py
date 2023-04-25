#This heatmap displays the Pearson correlation coefficients between the daily returns of different stocks.
#Daily returns are calculated as the percentage change in stock prices from one day to the next. 
#A stock returns correlation heatmap shows how the daily returns of different stocks are related, revealing which stocks tend to move together or in opposite directions.
#stock returns correlation heatmap is based on the daily returns of the stocks
import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def get_stock_returns(tickers, start_date, end_date, interval):
    data = yf.download(tickers, start=start_date, end=end_date, interval=interval)['Adj Close']
    returns = data.pct_change().dropna()
    return returns

def plot_returns(returns, title):
    corr_matrix = returns.corr()
    
    plt.figure(figsize=(24, 12))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1, linewidths=0.5)
    plt.title(title)
    plt.xlabel('Tickers')
    plt.ylabel('Tickers')
    plt.show()

tickers = [ 'BAC-PB', 'BAC-PE', 'BAC-PM', 'BAC-PN', 'BAC-PO', 'BAC-PP', 'BAC-PQ', 'BAC-PS', 'BANFP', 'BEP-PA', 'BEPH', 'BEPI', 'BFS-PD', 'BFS-PE', 'BHFAL', 'BHFAM', 'BHFAN', 'BHFAO', 'BHFAP', 'BHR-PD', 'BIP-PA', 'BIP-PB', 'BIPH', 'BIPI', 'BML-PG', 'BML-PH', 'BML-PJ', 'BML-PL']

start_date = '2022-10-21'
end_date = '2023-04-21'
interval = '1d'  # Use '1d' for daily or '1wk' for weekly

returns = get_stock_returns(tickers, start_date, end_date, interval)
plot_returns(returns, f'Stock Returns Correlation ({start_date} to {end_date})')
