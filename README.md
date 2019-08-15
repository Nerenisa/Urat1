# Urat1
The first U.S. Naval Observatory Astrometric Robotic Telescope Catalog (URAT1)


The urat1all.py program is written in the Python programming language for decoding binary catalogs URAT1 (z326 ..... z900)
Decoded information is converted to a table and written to the postgresql database


     
i | int           | integer | 4 | ra, spd, id2
h | short         | integer | 2 | sigs, sigm, epoc, mmag, sigp, nit, niu, pmr, pmd, pme, jmag, 
                                  hmag, kmag, ejmag, ehmag, ekmag, abm, avm, agm, arm, aim
B | unsigned char | integer | 1 | nst, nsm, ref, ngt, ngu, mf2, mfa, iccj, icch, icck, phqj,
                                  phqh, phqk, ann, ano, ebm, evm, egm, erm, eim
b | signed char   | integer | 1 | nsu


                                  
  

