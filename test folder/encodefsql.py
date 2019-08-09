#!/usr/bin/env python3
# coding: utf-8

import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import struct
import os
import sys

binary_pack = 'iihhBbhhhBBhhBBhhhBBihhhhhhBBBBBBhhhhhhhhhhBB'
pg_engine = create_engine('postgresql+psycopg2://user@localhost:5433/test2')
psql = 'select * from "urat1.3";'


pg_df = pd.read_sql_query(psql, con=pg_engine)
#print(pg_df)
for row in pg_df.itertuples(index=False, name=False):
    binary = struct.pack(binary_pack, *row)
    #print(binary)
    with open('binaryf', 'ab') as fout:
          fout.write(binary)