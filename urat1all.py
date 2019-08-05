#!/usr/bin/env python3
# coding: utf-8

import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import struct
import os


z_catalog = "/home/source_cat/URAT1/v12"         #r"C:\Users\User\Documents\urat1test"   # folder with directories "/home/source_cat/URAT1/v12"    
binary_unpack = 'iihhBbhhhBBhhBBhhhBBihhhhhhBBBBBBhhhhhhhhhhBB'   # format characters module struct (80 bytes)
col = ['RA', 'spd', 'sigs', 'sigm', 'nst', 'nsu', 'epoc', 'mmag', 'sigp', 'nsm', 'ref', 'nit', 'niu', 'ngt', 'ngu', 'pmr', 'pmd', 'pme', 'mf2', 'mfa', 'id2', 'jmag', 'hmag', 'kmag', 'ejmag', 'ehmag', 'ekmag', 'iccj', 'icch', 'icck', 'phqj', 'phqh', 'phqk', 'abm', 'avm', 'agm', 'arm', 'aim', 'ebm', 'evm', 'egm', 'erm', 'eim', 'ann', 'ano']
pg_engine = create_engine('postgresql+psycopg2://user@localhost:5433/test2')
psql = 'select * from "urat1.2" limit 300;'


counter_w=0

# walk through files in a directory z_catalog
zfiles = [f for f in os.listdir(z_catalog) if f.startswith("z")]
for z_files in zfiles:
    full_name_path = os.path.join(z_catalog, z_files)
    with open(full_name_path, 'rb') as fin:
        din = True
        n = 0
        all_catalog = []   # creating a temporary list of decoded binary directory strings z326....z900
        s = []    # creation of a temporary list from binary directory line numbering z326....z900
        while din:
            din = fin.read(80)
            if len(din) == 80:
                list_row = list(struct.unpack(binary_unpack, din)) 
                list_row[0] = round(list_row[0] / 3600000, 7)
                list_row[1] = round(list_row[1] / 3600000-90, 7)
                list_row[7] = list_row[7] / 1000
                list_row[21] = list_row[21] / 1000
                list_row[22] = list_row[22] / 1000
                list_row[23] = list_row[23] / 1000
                list_row[33] = list_row[33] / 1000
                list_row[34] = list_row[34] / 1000
                list_row[35] = list_row[35] / 1000
                list_row[36] = list_row[36] / 1000
                list_row[37] = list_row[37] / 1000
                #print(list_row)
                all_catalog.append(list_row)
                n = n + 1
                s.append(str(n).zfill(6))
        zn = ''.join((z_files.lstrip('z'), '-')).split() * all_catalog.__len__() 
        idn = [ zn[i] + s[i] for i in range(len(s))]  
        df = pd.DataFrame(all_catalog, index = idn, columns = col)
        #print(df)
        if counter_w == 0:
            df.to_sql('urat1.2', con=pg_engine)
            counter_w = 1
        else:
            df.to_sql('urat1.2', con=pg_engine, if_exists='append')

pg_df = pd.read_sql_query(psql, con=pg_engine)
print(pg_df)

