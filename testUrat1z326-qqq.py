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
#binary_file = 'z326'     # read file from the folder with directories 
#dump_file = 'testW.asc'   # folder dumpfile 
#list_row = 'RA, spd, sigs, sigm, nst, nsu, \
                #epoc, mmag, sigp, nsm, ref, \
                #nit, niu, ngt, ngu, pmr, pmd, \
                #pme, mf2, mfa, id2, jmag, hmag, \
                #kmag, ejmag, ehmag, ekmag, iccj, \
                #icch, icck, phqj, phqh, phqk, abm, \
                #avm, agm, arm, aim, ebm, evm, egm, '
                #erm, eim, ann, ano'      # tuple of table columns
col = ['RA', 'spd', 'sigs', 'sigm', 'nst', 'nsu', 'epoc', 'mmag', 'sigp', 'nsm', 'ref', 'nit', 'niu', 'ngt', 'ngu', 'pmr', 'pmd', 'pme', 'mf2', 'mfa', 'id2', 'jmag', 'hmag', 'kmag', 'ejmag', 'ehmag', 'ekmag', 'iccj', 'icch', 'icck', 'phqj', 'phqh', 'phqk', 'abm', 'avm', 'agm', 'arm', 'aim', 'ebm', 'evm', 'egm', 'erm', 'eim', 'ann', 'ano']
#list_str = [10, 9, 3, 3, 2, 3, 5, 5, 3, 2, 1, 3, 3, 3, 3, 5, 5, 3, 2, 2, 10, 5, 5, 5, 4, 4, 4, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3]
pg_engine = create_engine('postgresql+psycopg2://user@localhost:5433/test2')
psql = 'select * from "urat1" limit 5;'

counter_w=0

# walk through files in a directory z_catalog
#for root, dirs, files in os.walk(z_catalog):
zfiles = [f for f in os.listdir(z_catalog) if f.startswith("z8")]
for z_files in zfiles:
    full_name_path = os.path.join(z_catalog, z_files)
    with open(full_name_path, 'rb') as fin:
        din = True
        all_catalog = []
        while din:
            din = fin.read(80)
            if len(din) == 80:
                list_row = struct.unpack(binary_unpack, din) 
                qq=list(list_row)
                qq[1] = round(qq[1] / 3600000-90, 7)
                qq[0] = round(qq[0] / 3600000, 7)
                qq[7] = qq[7] / 1000
                qq[21] = qq[21] / 1000
                qq[22] = qq[22] / 1000
                qq[23] = qq[23] / 1000
                qq[33] = qq[33] / 1000
                qq[34] = qq[34] / 1000
                qq[35] = qq[35] / 1000
                qq[36] = qq[36] / 1000
                qq[37] = qq[37] / 1000
                #print(qq)  #=list_row[1]/3600000
                all_catalog.append(qq)
                    #to_print = ("".join("{:" + "{}".format(list_str[i]) + "} " for i in range(len(list_row)))).format(*( _ for _ in list_row))
        df = pd.DataFrame(all_catalog, columns = col)
        #print(df)
        if counter_w == 0:
            df.to_sql('urat1', con=pg_engine)
            counter_w = 1
        else:
            df.to_sql('urat1', con=pg_engine, if_exists='append')
pg_df = pd.read_sql_query(psql, con=pg_engine)
print(pg_df)

                    #print(to_print)
                    #with open(dump_file, 'a') as fout:
                        #fout.write(to_print +'\n')

# print number of bytes
#s = os.path.getsize(dump_file)
#print (s)
