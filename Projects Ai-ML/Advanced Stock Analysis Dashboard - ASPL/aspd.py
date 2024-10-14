import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import ta

# App config
st.set_page_config(layout="wide", page_title="Advanced Stock Analysis Dashboard")

# Sidebar
st.sidebar.title("Stock Analysis Dashboard")
ticker = st.sidebar.text_input("Enter Stock Ticker", value="AAPL")
start_date = st.sidebar.date_input("Start Date", datetime.now() - timedelta(days=365))
end_date = st.sidebar.date_input("End Date", datetime.now())

# Fetch data
@st.cache_data
def fetch_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

data = fetch_stock_data(ticker, start_date, end_date)

# Main layout
st.title(f"Advanced Stock Analysis Dashboard - {ticker}")

# Price chart
def plot_price_chart(data):
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=data.index,
                                 open=data['Open'],
                                 high=data['High'],
                                 low=data['Low'],
                                 close=data['Close'],
                                 name='Price'))
    fig.update_layout(title="Stock Price Chart", xaxis_title="Date", yaxis_title="Price")
    return fig

st.plotly_chart(plot_price_chart(data), use_container_width=True)

# Technical Indicators
def add_technical_indicators(data):
    data['SMA20'] = ta.trend.sma_indicator(data['Close'], window=20)
    data['SMA50'] = ta.trend.sma_indicator(data['Close'], window=50)
    data['RSI'] = ta.momentum.rsi(data['Close'], window=14)
    data['MACD'] = ta.trend.macd_diff(data['Close'])
    return data

data_with_indicators = add_technical_indicators(data)

# Technical Analysis Chart
def plot_technical_analysis(data):
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.05,
                        row_heights=[0.5, 0.3, 0.2])
    
    fig.add_trace(go.Candlestick(x=data.index, open=data['Open'], high=data['High'],
                                 low=data['Low'], close=data['Close'], name='Price'),
                  row=1, col=1)
    fig.add_trace(go.Scatter(x=data.index, y=data['SMA20'], name='SMA 20'), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.index, y=data['SMA50'], name='SMA 50'), row=1, col=1)
    
    fig.add_trace(go.Bar(x=data.index, y=data['Volume'], name='Volume'), row=2, col=1)
    
    fig.add_trace(go.Scatter(x=data.index, y=data['RSI'], name='RSI'), row=3, col=1)
    fig.add_hline(y=70, line_dash="dash", line_color="red", row=3, col=1)
    fig.add_hline(y=30, line_dash="dash", line_color="green", row=3, col=1)
    
    fig.update_layout(title="Technical Analysis Chart", height=800)
    fig.update_xaxes(title_text="Date", row=3, col=1)
    fig.update_yaxes(title_text="Price", row=1, col=1)
    fig.update_yaxes(title_text="Volume", row=2, col=1)
    fig.update_yaxes(title_text="RSI", row=3, col=1)
    
    return fig

st.plotly_chart(plot_technical_analysis(data_with_indicators), use_container_width=True)

# Predictive Modeling
def train_model(data):
    features = ['Open', 'High', 'Low', 'Close', 'Volume', 'SMA20', 'SMA50', 'RSI', 'MACD']
    X = data[features]
    y = data['Close'].shift(-1)  # Predict next day's closing price
    X = X[:-1]  # Remove last row
    y = y[:-1]  # Remove last row
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    return model, mse, r2

model, mse, r2 = train_model(data_with_indicators)

st.subheader("Predictive Model Performance")
col1, col2 = st.columns(2)
col1.metric("Mean Squared Error", f"{mse:.4f}")
col2.metric("R-squared Score", f"{r2:.4f}")

# Future Price Prediction
future_days = st.slider("Predict future prices (days)", 1, 30, 7)

last_data = data_with_indicators.iloc[-1]
future_predictions = []

for _ in range(future_days):
    prediction = model.predict([last_data[['Open', 'High', 'Low', 'Close', 'Volume', 'SMA20', 'SMA50', 'RSI', 'MACD']]])[0]
    future_predictions.append(prediction)
    last_data['Open'] = last_data['Close']
    last_data['Close'] = prediction
    last_data['High'] = max(last_data['Open'], prediction)
    last_data['Low'] = min(last_data['Open'], prediction)
    # Update indicators (simplified)
    last_data['SMA20'] = prediction
    last_data['SMA50'] = prediction
    last_data['RSI'] = 50
    last_data['MACD'] = 0

future_dates = pd.date_range(start=data.index[-1] + timedelta(days=1), periods=future_days)
future_df = pd.DataFrame({'Date': future_dates, 'Predicted_Close': future_predictions})

st.subheader("Future Price Predictions")
st.dataframe(future_df)

# Visualize predictions
def plot_predictions(data, future_df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], name='Historical Close'))
    fig.add_trace(go.Scatter(x=future_df['Date'], y=future_df['Predicted_Close'], name='Predicted Close'))
    fig.update_layout(title="Historical and Predicted Stock Prices", xaxis_title="Date", yaxis_title="Price")
    return fig

st.plotly_chart(plot_predictions(data, future_df), use_container_width=True)

# Additional Analysis
st.subheader("Additional Analysis")

# Correlation Heatmap
correlation = data[['Open', 'High', 'Low', 'Close', 'Volume']].corr()
fig = go.Figure(data=go.Heatmap(z=correlation.values, x=correlation.index, y=correlation.columns, colorscale='Viridis'))
fig.update_layout(title="Correlation Heatmap", height=500)
st.plotly_chart(fig, use_container_width=True)

# Trading Volume Analysis
volume_ma = data['Volume'].rolling(window=20).mean()
fig = go.Figure()
fig.add_trace(go.Bar(x=data.index, y=data['Volume'], name='Volume'))
fig.add_trace(go.Scatter(x=data.index, y=volume_ma, name='20-day MA Volume'))
fig.update_layout(title="Trading Volume Analysis", xaxis_title="Date", yaxis_title="Volume")
st.plotly_chart(fig, use_container_width=True)

# Volatility Analysis
data['Returns'] = data['Close'].pct_change()
data['Volatility'] = data['Returns'].rolling(window=20).std() * np.sqrt(252)  # Annualized volatility

fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data['Volatility'], name='20-day Volatility'))
fig.update_layout(title="Volatility Analysis", xaxis_title="Date", yaxis_title="Annualized Volatility")
st.plotly_chart(fig, use_container_width=True)