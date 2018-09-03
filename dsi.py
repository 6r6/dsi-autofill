#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author_base64:cjZyQGxpdmUuY24=

import re

class DsiParser:
    
    def __init__(self,file_path):
        self.file_path = file_path
        self.seg = {
            'circuit':'% Harness circuit information',
            'branch':'% Harness branch configuration',
            'wire':'% Harness wire specification',
            'mnode':'% Harness main node components',
            'tnode':'! Harness tapes at nodes',
            'enode':'! Harness extra node components',
            'terminals':'! Harness terminals',
            'seals':'! Harness cavity seals',
            'cavity':'! Harness extra cavity components',
            'wire-end-components':'! Harness wire end components',
            'multiple-location-components':'! Harness multiple location components',
            'assembly-items':'! Harness assembly items',
            'insulations':'% Harness branch insulations',
            'strips':'% Harness center strips',
            'multicores':'% Harness multicores',
            'child-details':'% Module child details',
            'compatibility-details':'% Module compatibility details',
            'bom-quantities':'% Manual BOM quantities',
            'options':'% Composite Option Codes',
            'wire-through-nodes':'% Harness wire through nodes',
            'branch-insulation':'% Harness branch insulation through nodes',
            'mid-wire-components':'% Harness mid wire components',
            'markers':'% Harness wire / multicore markers',
            'pin':'% Harness pin mappings',
            'scope':'% Harness scope',
            'name':'! Harness name information',
            'note':'% Harness note information'
        }

    @staticmethod
    def get_mid(text, w1, w2):
        pat = re.compile(w1 + '(.*?)' + w2, re.S)
        try:
            return pat.findall(text)[0]
        except:
            raise Exception
    
    @staticmethod
    def not_empty(s):
        return s and s.strip()

    @staticmethod
    def get_pure_list(list):
        return filter(DsiParser.not_empty, list)

    def get_file_str(self):
        with open(self.file_path,'r') as f:
            self.text = f.read()

    def get_string(self, func):
        self.get_file_str()
        try:
            return self.get_mid(self.text,w1=self.seg[func],w2='!\n')
        except:
            raise Exception
