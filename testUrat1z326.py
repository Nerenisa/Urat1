#!/usr/bin/env python3
# coding: utf-8

import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import struct
import os


z_catalog = r"C:\Users\User\Documents\urat1test"   # folder with directories "/home/source_cat/URAT1/v12"    
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
engine = create_engine('postgresql+://user:147456@158.250.29.198:5433/test2')



# walk through files in a directory z_catalog

#for root, dirs, files in os.walk(z_catalog):
zfiles = [f for f in os.listdir(z_catalog) if f.startswith("z")]
#print("Find {} z files in {} ".format(len(zfiles), z_catalog)) 
for z_files in zfiles:
    full_name_path = os.path.join(z_catalog, z_files)
    with open(full_name_path, 'rb') as fin:
        all_catalog = []
        din = True
        while din:
            din = fin.read(80)
            if len(din) == 80:
                list_row = struct.unpack(binary_unpack, din)
                all_catalog.append(list_row)
                    #to_print = ("".join("{:" + "{}".format(list_str[i]) + "} " for i in range(len(list_row)))).format(*( _ for _ in list_row))
df = pd.DataFrame(all_catalog, columns = col)
print(df)

df.to_sql('table_Urat1_test', engine)
                    #print(to_print)
                    #with open(dump_file, 'a') as fout:
                        #fout.write(to_print +'\n')

# print number of bytes
#s = os.path.getsize(dump_file)
#print (s)
