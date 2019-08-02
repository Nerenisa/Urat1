#!/usr/bin/env python3
# coding: utf-8

import pandas as pd
import os
import re
import numpy as np
import struct
import os

z_catalog = r"C:\Users\User\Documents\urat1test"
binary_unpack = 'iihhBbhhhBBhhBBhhhBBihhhhhhBBBBBBhhhhhhhhhhBB'
col = ['RA', 'spd', 'sigs', 'sigm', 'nst', 'nsu', 'epoc', 'mmag', 'sigp', 'nsm', 'ref', 'nit', 'niu', 'ngt', 'ngu', 'pmr', 'pmd', 'pme', 'mf2', 'mfa', 'id2', 'jmag', 'hmag', 'kmag', 'ejmag', 'ehmag', 'ekmag', 'iccj', 'icch', 'icck', 'phqj', 'phqh', 'phqk', 'abm', 'avm', 'agm', 'arm', 'aim', 'ebm', 'evm', 'egm', 'erm', 'eim', 'ann', 'ano']


zfiles = [f for f in os.listdir(z_catalog) if f.startswith("z")]
for z_files in zfiles:
    full_name_path = os.path.join(z_catalog, z_files)
    with open(full_name_path, 'rb') as fin:
        din = True
        n = 0
        all_catalog = []   
        idn = []      # new 
        s = []     # new
        while din:
            din = fin.read(80)
            if len(din) == 80:
                list_row = list(struct.unpack(binary_unpack, din))
                all_catalog.append(list_row)
                n = n + 1
                s.append(str(n).zfill(6))       
            #print(f)
        zn = ''.join((z_files.lstrip('z'), '-')).split() * all_catalog.__len__()  # new
        for zin in zn:
            for f in s:
                idn.append(''.join((zin, str(f))))
                
               
                    
            #print(idn)
            #print(e)


        df = pd.DataFrame(all_catalog, index = idn, columns = col)
        print(df)












