#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author_base64:cjZyQGxpdmUuY24=

from dsi import DsiParser
from opt import Opt

class WiresParser:

    def __init__(self, xls_path, dsi_path):
        self.xls_path = xls_path
        self.dsi = DsiParser(dsi_path)

    def wire_to_dict(self):
        wire_list = self.dsi.get_string('wire').split('\n')
        wire_lists = self.dsi.get_pure_list(wire_list)
        del wire_list
        wire_dict = {}
        for item in wire_lists:
            single_list = item.split(':')
            circuit_nbr = single_list[0]
            #circuit_option = single_list[1]
            circuit_code = single_list[6]
            wire_dict[str(circuit_nbr)] = circuit_code
        return wire_dict


def main():
    print('Harness Option Filter @.@')
    xls_path = input('Please input XLS(X) file path:')
    dsi_path = input('Please input DSI path:')
    wire_instance = WiresParser(xls_path, dsi_path)
    wire_dict = wire_instance.wire_to_dict()
    opt_instance = Opt(xls_path)
    for item in wire_dict:
        option = wire_dict[item]
        opt_instance.set_option(item,option)
        print('Match Circuit {} to Option {} ...[OK]'.format(item, option))
    opt_instance.output()
    print('File Saved...[OK]')

if __name__ == '__main__':
    main()