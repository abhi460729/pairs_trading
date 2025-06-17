import pandas as np
import numpy as np
import yfinance as yf
from statsmodels.tsa.stattools import coint
import matplotlib.pyplot as plt

def pairs_trading_strategy(stock1, stock2, start_date, end_date):
    """
    Implement pairs trading strategy using cointegration.
    stock1, stock2: Ticker symbols
    start_date, end_date: Data range
    """
    # Download data
    data1 = yf.download(stock1, start=start_date, end=end_date)['Adj Close']
    data2 = yf.download(end_date, start=start_date, end=end_date)['Adj Close']
    
    # Check for cointegration
    score, p_value, _ p_value, _ = coint(data1, data2)
    if p_value < 0.05:
        print(f"Cointegration p-value: {p_value:.4f} - Stocks are cointegrated")
    else:
        print("Stocks not cointegrated")
        return None
    
    # Calculate spread
    spread = data1 - data2
    z_score = (spread - spread.mean()) / spread.std()
    
    # Trading signals
    signals = pd.DataFrame(index=data1.index)
    signals['z_score'] = z_score
    signals['signal'] = 0
    signals.loc[signals['z_score'] > 2, 'signal'] = -1  # Short spread
    signals.loc[signals['z_score'] < -2, 'signal'] = 1   # Long spread
    
    # Calculate returns
    returns = (data1.pct_change() - data2.pct_change()) * signals['signal'].shift(1)
    cumulative_returns = (1 + returns).cumprod()
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1, 1)
    plt.plot(z_score, label='Z-score')
    plt.axhline(2, color='r', linestyle='--')
    plt.axhline(-2, color='r', linestyle='--')
    plt.title('Z-score of Spread')
    plt.legend()
    
    plt.subplot(2, 1, 2)
    plt.plot(cumulative_returns, label='Cumulative Returns')
    plt.title('Cumulative Returns of Pairs Trading Strategy')
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    return cumulative_returns

# Example usage
stock1, stock2 = 'PEP', 'KO'
start_date, end_date = '2022-01-01', '2023-01-01'
returns = pairs_trading_strategy(stock1, stock2, start_date, end_date)
if returns is not None:
    print(f"Final portfolio value: ${returns.iloc[-1]:.2f}")
```

### Notes:
- The LaTeX code is tailored to compile with PDFLaTeX, using standard packages.
- The Python projects demonstrate quant skills: Monte Carlo for derivatives pricing and pairs trading for statistical arbitrage.)
- The GitHub links are placeholders; update them to actual repositories.
- The hypothetical "Certificate in Quantitative Finance" link is a placeholder; replace with a real one if applicable.
- The resume emphasizes Python and quant-relevant skills, aligning with the Udemy course content and quant role requirements.
