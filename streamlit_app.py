import yfinance as yf
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def get_stock_returns(tickers, start_date, end_date, interval):
    data = yf.download(tickers, start=start_date, end=end_date, interval=interval)['Adj Close']
    returns = data.pct_change().dropna()
    return returns

def plot_returns(returns, title):
    # Normalize and separate the returns to avoid overlap
    normalized_returns = (returns - returns.min()) / (returns.max() - returns.min())
    offset = np.arange(len(returns.columns)) * 1.2
    separated_returns = normalized_returns + offset

    fig, ax = plt.subplots(figsize=(24, 12))

    for i, ticker in enumerate(returns.columns):
        sns.lineplot(x=separated_returns.index, y=separated_returns[ticker], label=ticker, ax=ax)

    ax.set_yticks(offset)
    ax.set_yticklabels(returns.columns)
    ax.set_title(title)
    ax.set_xlabel('Date')
    ax.set_ylabel('Returns (separated)')
    ax.legend()
    plt.show()

tickers = [ 'BAC-PB', 'BAC-PE', 'BAC-PM', 'BAC-PN', 'BAC-PO', 'BAC-PP', 'BAC-PQ', 'BAC-PS', 'BANFP', 'BEP-PA', 'BEPH', 'BEPI', 'BFS-PD', 'BFS-PE', 'BHFAL', 'BHFAM', 'BHFAN', 'BHFAO', 'BHFAP', 'BHR-PD', 'BIP-PA', 'BIP-PB', 'BIPH', 'BIPI', 'BML-PG', 'BML-PH', 'BML-PJ', 'BML-PL']

start_date = '2022-10-21'
end_date = '2023-04-21'
interval = '1d'  # Use '1d' for daily or '1wk' for weekly

returns = get_stock_returns(tickers, start_date, end_date, interval)
plot_returns(returns, f'Stock Returns ({start_date} to {end_date})')
