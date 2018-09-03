#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author_base64:cjZyQGxpdmUuY24=

import pandas as pd

class Opt:
    
    def __init__(self, xls_path):
        self.xls_path = xls_path
        self.data = pd.read_excel(self.xls_path, sheet_name='Wires')

    def set_option(self, circuit, option):
        data = self.data
        try:
            key = 'Circuit Nbr'
            data.loc[data[key]==str(circuit),'Option'] = option
        except:
            key = 'CIRCUIT NBR'
            data.loc[data[key]==str(circuit),'Option'] = option
        return data

    def output(self):
        new_file_path = self.xls_path.replace('.xls','_CHECK.xls')
        sorted_data = self.data.sort_values(by='Option')
        sorted_data.to_excel(new_file_path,sheet_name='Checked',index=False,header=True)
        return sorted_data


if __name__ == '__main__':
    opt_instance = Opt('Aptiv/1.xlsx')
    opt_instance.set_option('9039B','ALL00')
    opt_instance.set_option('265C','ALL00')
    opt_instance.output()