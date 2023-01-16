
# ! to be used by user: utilizes libraries made by "create_stat_libraries.py"
import numpy as np
import statistics 
from statistics import mode
import scipy.stats as st

def search_probability():
    pattern_matches = []

    # ! this list is NOT automaticcaly updated by "create_stat_libraries"
        # # this is to avoid compiling "create_stat_libraries" every time this code is run
    tickers = ['AAPL', 'GOOGL', 'BAC', 'INTC', 'AMZN', 
                'TSLA', 'MSFT', 'NIO', 'KO', 'VALE', 'SBUX',
                'LEGN', 'CVX', 'AVPT', 'XOM', 'HD', 'UNH',
                'ABT', 'LLY', 'VOD', 'JPM', 'NVS', 'WB', 
                'DCM', 'EON', 'GE', 'BP', 'C', 'PG', 'WMT',
                'PFE', 'HBC', 'TM', 'JNJ', 'MO', 'KO', 'SI',
                'ORCL', 'AXA', 'BTI', 'DIS', 'MCD', 'DEO', 
                'LOW', 'BNS', 'RIO', 'VLO']

    # get pattern from user
    pattern = input("Data pattern (int) (ex. -1 2 4 3): ")

    # compare users pattern with pettern banks and collect matches
    for i in range(len(tickers)):
        data = np.loadtxt(tickers[i] + '_pattern_bank', delimiter = '\n', dtype = str)
        for i in range(len(data)-2):
            if (pattern == data[i]):
                pattern_matches.append(int(data[i+1]))
    num_matches = len(pattern_matches)
    print("Number of pattern matches: " + str(num_matches))

    # calculate most frequent outcome of given pattern
    if num_matches > 0:
        most_freq_next_change = mode(pattern_matches)
        print("Most likely change: " + str(most_freq_next_change))
        # limit amount of info printed on screen to keep it neat
        if num_matches <= 10:
            print(pattern_matches)

        # calculate occurance percentage of most frequent outcome
        most_likely_tally = 0
        for i in range(len(pattern_matches)):
            if (most_freq_next_change == pattern_matches[i]):
                    most_likely_tally += 1
        most_likely_percentage = (most_likely_tally / len(pattern_matches)) * 100
        print("\tLikelihood of " + str(most_freq_next_change) + ": % " + str(most_likely_percentage))

        # Calculate percentages for going up, same, and going down
        up,same,down = 0,0,0
        for i in range(len(pattern_matches)):
            pm = pattern_matches[i]
            if pm > 0:
                up += 1
            elif pm < 0:
                down += 1
            else:
                same += 1
        up_percentage   = (up / len(pattern_matches))   * 100
        same_percentage = (same / len(pattern_matches)) * 100
        down_percentage = (down / len(pattern_matches)) * 100
        print("Percentage up: % " + str(up_percentage))
        print("Percentage same: % " + str(same_percentage))
        print("Percentage down: % " + str(down_percentage))

        #calculate %90 percent confidence level
        if num_matches < 30 and num_matches > 0:
            confidence_interval = st.t.interval(alpha = .90, df = num_matches - 1, loc = np.mean(pattern_matches), scale = st.sem(pattern_matches))
        elif num_matches >= 30:
            confidence_interval = st.norm.interval(alpha = .90, loc = np.mean(pattern_matches), scale = st.sem(pattern_matches))
        print("%90 confidence interval: " + str(confidence_interval))
    else:
        print("\t-No matches for this pattern")

search_probability()