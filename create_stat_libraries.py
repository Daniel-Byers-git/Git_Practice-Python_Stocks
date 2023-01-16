import get_stock_data as gsd
import comb_data as cd
import populate_pattern_bank as ppb
#import numpy as np

# ! single use code just to make libraries

# {
    # class dictionary(dict):
    #     def __init__(self):
    #         self = dict()
    #     def append(self, key, value):
    #         self[key] = value
    #     def stat_collect(self, ticker):
    #         # ? chng_dat = np.loadtxt('percent_changes_daily.txt', dtype = str)
    #         chng_dat = np.loadtxt(ticker + '_percent_changes_daily.txt', dtype = str)
    #         chng_dat_sz = chng_dat.size
    #         for i in range(chng_dat_sz-4):
    #             pattern_key = chng_dat[i] + chng_dat[i+1] + chng_dat[i+2] + chng_dat[i+3]
    #             end_value = chng_dat[i+4]
    #             self.append(pattern_key, end_value)
    #         # puts 4 day pattern as key with 5th day as value
    #         # appends it to one large dictionary
# }

ticker_list = ['AAPL', 'GOOGL', 'BAC', 'INTC', 'AMZN', 
               'TSLA', 'MSFT', 'NIO', 'KO', 'VALE', 'SBUX',
               'LEGN', 'CVX', 'AVPT', 'XOM', 'HD', 'UNH',
               'ABT', 'LLY', 'VOD', 'JPM', 'NVS', 'WB', 
               'DCM', 'EON', 'GE', 'BP', 'C', 'PG', 'WMT',
               'PFE', 'HBC', 'TM', 'JNJ', 'MO', 'KO', 'SI',
               'ORCL', 'AXA', 'BTI', 'DIS', 'MCD', 'DEO', 
               'LOW', 'BNS', 'RIO', 'VLO']

# full_library = dictionary()
# full_library = []

for i in range(len(ticker_list)):
    gsd.get_stock_data(ticker_list[i], '2015-01-01', '2021-01-01')
    cd.comb_data(ticker_list[i])
    ppb.populate_pattern_bank(ticker_list[i])
    # full_library.stat_collect(ticker_list[i])
    # uses two custom made scripts to gather data then appends it to large library using class functions defined above
    # ! make a list:
    # ! put the four pattern in one slot
    # ! and it matching fifth in the next slot
    # ! then when you search for a four pattern just take the next index as its fifth value

# print(full_library)