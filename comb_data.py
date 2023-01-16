
# ! to be used by "create_stat_libraries.py"

import csv
# import numpy as np

def comb_data(ticker):
    # ? file = open('stock_prices.csv') 
    file = open(ticker)
        # open data from yahoo finance in csv form
    csv_read = csv.reader(file)
        # creates a csv reader to go through by row
    headers = []
    headers = next(csv_read)
        # collect the first row of labels in csv into list 'headers'
    data_list = []
    for row in csv_read:
        data_list.append(row)
        # makes a list of only open and close prices from the csv file
    file.close()
        # close the csv file with yahoo finance data

    [j.pop(0) for j in data_list]
        # gets rid of date in first column that contains the date

    data_arr = []
    for row in range(len(data_list)):
        data_list[row][0], data_list[row][1] = float(data_list[row][0]), float(data_list[row][1])
            # conerts the open and close from strings to floats
        daily_percent_change = ( (data_list[row][1] - data_list[row][0]) / data_list[row][0] ) * 100.0
            # calculates the percent change of stock price through each day
        daily_percent_change = round(daily_percent_change)
            # rounds to nearest integer
        daily_percent_change = str(daily_percent_change)
            # turn ints to string to concatenate into a list later. 
            # makes easier to search through i think.
        data_arr.append(daily_percent_change)
            # adds days percent change to a numpy array to store
    # ? out_perc = open('percent_changes_daily.txt', 'w')
    out_perc = open(ticker + '_percent_changes_daily.txt', 'w')
    for row in range(len(data_arr)):
        out_perc.write(f'{data_arr[row]}\n')
        # opens a txt file to store daily percent change values
    out_perc.close()
# test = comb_data('AAPL')