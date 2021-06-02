# Data Source
import yfinance as yf
#Data viz
import plotly.graph_objs as go
import imgkit

class moving_average():
    def __init__(self, ticker):
        self.ticker = ticker
    def get_trend(self, instant, graph):
        # Download yahoo finance btc-usd data
        data = yf.download(self.ticker,period = '24h', interval = '15m')

        # Adding Moving average calculated field
        data['MA5'] = data['Close'].rolling(5).mean()
        data['MA20'] = data['Close'].rolling(20).mean()

        # Remove first 20 points of data without the averages
        data = data.iloc[20:]

        if graph:
            # Declare figure
            fig = go.Figure()

            #Candlestick
            fig.add_trace(go.Candlestick(x=data.index.tz_convert("US/Pacific"),
                        open=data['Open'],
                        high=data['High'],
                        low=data['Low'],
                        close=data['Close'], name = 'market data'))

            # Add moving averages lines
            fig.add_trace(go.Scatter(x=data.index.tz_convert("US/Pacific"), y= data['MA20'],line=dict(color='blue', width=1.5), name = 'Long Term MA'))
            fig.add_trace(go.Scatter(x=data.index.tz_convert("US/Pacific"), y= data['MA5'],line=dict(color='orange', width=1.5), name = 'Short Term MA'))
            
            # Save image
            fig.write_html(self.ticker + ".html")
            imgkit.from_file(self.ticker + ".html", self.ticker + ".jpg")
        if instant:
            if data['MA5'][-1] > data['MA20'][-1]:
                tmp = "buy"
            else:
                tmp = "sell"
            time = data.index[-1].tz_convert("US/Pacific").strftime("%d/%m/%Y %H:%M:%S")
            return time, data['Close'][-1], tmp
        # Store new data in seperate location
        df = data.loc[:, ['Close', 'MA5', 'MA20']]
        if data['MA5'][-2] > data['MA20'][-2]:
            tmp = "buy"
        else:
            tmp = "sell"
        time = data.index[-2].tz_convert("US/Pacific").strftime("%d/%m/%Y %H:%M:%S")
        return time, df['Close'][-2], tmp

if __name__ == '__main__':
    btc_time, btc_close, btc_status = moving_average('BTC-USD').get_trend(True)
    eth_time, eth_close, eth_status = moving_average('ETH-USD').get_trend(True)
    doge_time, doge_close, doge_status = moving_average('DOGE-USD').get_trend(True)
    print('{} Price of BTC-USD is at {}, you should {}'.format(btc_time, btc_close, btc_status))
    print('{} Price of ETH-USD is at {}, you should {}'.format(eth_time, eth_close, eth_status))
    print('{} Price of DOGE-USD is at {}, you should {}'.format(doge_time, doge_close, doge_status))