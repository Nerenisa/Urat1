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


zfiles = [f for f in os.listdir(z_catalog) if f.startswith("z900")]
for z_files in zfiles:
    full_name_path = os.path.join(z_catalog, z_files)
    with open(full_name_path, 'rb') as fin:
        din = True
        n = 0
        all_catalog = []   
        s = []     # new
        while din:
            din = fin.read(80)
            if len(din) == 80:
                list_row = list(struct.unpack(binary_unpack, din)) 
                list_row[0] = round(list_row[0] / 3600000, 7)
                list_row[1] = round(list_row[1] / 3600000-90, 7)
                list_row[6] = list_row[6] / 1000 + 2000
                list_row[7] = list_row[7] / 1000
                list_row[21] = list_row[21] / 1000
                list_row[22] = list_row[22] / 1000
                list_row[23] = list_row[23] / 1000
                list_row[33] = list_row[33] / 1000
                list_row[34] = list_row[34] / 1000
                list_row[35] = list_row[35] / 1000
                list_row[36] = list_row[36] / 1000
                list_row[37] = list_row[37] / 1000
                all_catalog.append(list_row)
                n = n + 1
                s.append(str(n).zfill(6))       
            #print(f)
        zn = ''.join((z_files.lstrip('z'), '-')).split() * all_catalog.__len__()  # new
        idn = [ zn[i] + s[i] for i in range(len(s))]
                
               
                    
            #print(idn)
            #print(e)


        df = pd.DataFrame(all_catalog, index = idn, columns = col)
        print(df)












