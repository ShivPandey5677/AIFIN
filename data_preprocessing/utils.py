import pandas as pd
import ta

def add_technical_indicators(df):
    df = ta.add_all_ta_features(df, open="Open", high="High", low="Low", close="Close", volume="Volume", fillna=True)
    return df

def calculate_return(start_price, end_price):
    return (end_price - start_price) / start_price
