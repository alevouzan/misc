import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from scipy.stats import entropy

# Fetch data
stock_data = yf.download('AAPL', start='2020-01-01', end='2023-01-01')

# Calculate daily returns
stock_data['Daily_Return'] = stock_data['Close'].pct_change()
stock_data = stock_data.dropna()

# Calculate the probability distribution of returns
counts, bin_edges = np.histogram(stock_data['Daily_Return'], bins=50, density=True)

# Calculate the entropy
returns_entropy = entropy(counts)
print(f'Entropy of Daily Returns: {returns_entropy}')

# Plot daily returns
plt.figure(figsize=(14, 7))
plt.subplot(2, 1, 1)
plt.plot(stock_data.index, stock_data['Daily_Return'], label='Daily Returns')
plt.title('Daily Returns of AAPL')
plt.legend()

# Plot histogram of daily returns
plt.subplot(2, 1, 2)
plt.hist(stock_data['Daily_Return'], bins=50, edgecolor='k', alpha=0.7, density=True)
plt.title('Histogram of Daily Returns')
plt.xlabel('Daily Return')
plt.ylabel('Density')

plt.tight_layout()
plt.show()
