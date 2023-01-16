
# ! code to be used by "create_stat_libraries.py"

import numpy as np

def populate_pattern_bank(ticker):
    file = open(ticker + '_pattern_bank', 'w')
    chng_dat = np.loadtxt(ticker + '_percent_changes_daily.txt', dtype = str)
    chng_dat_sz = chng_dat.size
    for i in range(chng_dat_sz-4):
        pattern_key = chng_dat[i] + ' ' + chng_dat[i+1] + ' ' + chng_dat[i+2] + ' ' + chng_dat[i+3]
        file.write(pattern_key + '\n')
        end_value = chng_dat[i+4]
        file.write(end_value + '\n')
    file.close()         