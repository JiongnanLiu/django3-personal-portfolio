from pandas_datareader import get_data_yahoo
import bs4 as bs
import pickle
import requests
import pandas as pd
from datetime import datetime, timedelta
import tdameritrade as td
#from stockscreener.config import cliend_id
from stockscreener import config
#cliend_id = 'QEXW048XXG6CP86J51LNWTM2QSLVZJKZ'

cliend_id = config.get_id()


class Stock:

    def __init__(self):
        self.sp500 = self.save_sp500_tickers()
        self.ndx = self.save_nasdaq_tickers()
        self.epoch = datetime.utcfromtimestamp(0)
        self.sp500_comp_last_price = []

    def get_data(self, request):
        df = get_data_yahoo('AAPL', '2018-05-01')
        df = df.reset_index()
        df = df.iloc[:, :-1]

        for col in df.columns[1:]:
            df[col] = df[col].astype('int')

        for col in df.columns:
            df[col] = df[col].astype('str')
        df_list = df.values.tolist()

        data = {'titleSet': 'AAPL',
                'dataSet': df_list}
        # return JsonResponse(data, safe=False)
        return data

    def save_sp500_tickers(self):
        resp = requests.get(
            'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
        soup = bs.BeautifulSoup(resp.text, 'lxml')
        table = soup.find('table', {'class': 'wikitable sortable'})
        tickers = []
        for row in table.findAll('tr')[1:]:
            ticker = row.findAll('td')[0].text
            tickers.append(ticker)

        with open("sp500tickers.pickle", "wb") as f:
            pickle.dump(tickers, f)

        tickers = [s.replace('\n', '') for s in tickers]
        return tickers

    def save_nasdaq_tickers(self):
        resp = requests.get(
            'http://en.wikipedia.org/wiki/NASDAQ-100#External_links')
        soup = bs.BeautifulSoup(resp.text, 'lxml')
        table = soup.find(
            'table', {'id': 'constituents'})
        tickers = []
        for row in table.findAll('tr')[1:]:
            ticker = row.findAll('td')[1].text
            tickers.append(ticker)

        with open("nasdaq100tickers.pickle", "wb") as f:
            pickle.dump(tickers, f)

        tickers = [s.replace('\n', '') for s in tickers]
        return tickers

    def unix_time_millis(self, dt):
        return int((dt - self.epoch).total_seconds() * 1000)

    def api_url(self, tick):
        endpoint = r"https://api.tdameritrade.com/v1/marketdata/{}/pricehistory".format(
            tick)
        return endpoint

    def get_sp500_comp_last_price(self):
        table = []
        last = datetime.now() - timedelta(3)
        epochtime = str(self.unix_time_millis(last))
        print(epochtime)
        payload = {'apikey': cliend_id,
                   'periodType': 'year',
                   'frequencyType': 'daily',
                   'frequency': '1',
                   'period': '1',
                   'startDate': epochtime,
                   'needExtendedHoursData': 'False'}
        counter = 0
        for tick in self.sp500:
            if (counter == 20):
                break
            content = requests.get(url=self.api_url(tick), params=payload)
            data = content.json()
            # print(data)
            table.append(
                {'symbol': data['symbol'], 'close': data['candles'][0]['close'], 'volume': data['candles'][0]['volume']})
            counter += 1
        #df = pd.DataFrame(table)
        # print(table)
        self.sp500_comp_last_price = table
        return table


#mystock = Stock()
# mystock.get_sp500_comp_last_price()
