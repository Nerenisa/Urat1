# Urat1
The first U.S. Naval Observatory Astrometric Robotic Telescope Catalog (URAT1)


The urat1all.py program is written in the Python programming language for decoding binary catalogs URAT1 (z326 ..... z900)
Decoded information is converted to a table and written to the postgresql database

items to read from input files:
     
i | int           | integer | 4 | ra, spd, id2

h | short         | integer | 2 | sigs, sigm, epoc, mmag, sigp, nit, niu, pmr, pmd, pme, jmag, 
                                  hmag, kmag, ejmag, ehmag, ekmag, abm, avm, agm, arm, aim
                                  
B | unsigned char | integer | 1 | nst, nsm, ref, ngt, ngu, mf2, mfa, iccj, icch, icck, phqj,
                                  phqh, phqk, ann, ano, ebm, evm, egm, erm, eim
                                  
b | signed char   | integer | 1 | nsu


column	 item	type	unit	description and notes
1	     ra	    i*4  	mas	    mean RA on ICRF at URAT mean obs.epoch   (1)
2	     spd	i*4  	mas	    mean South Pole Distance = Dec + 90 deg  (2)
3	     sigs	h*2  	mas	    position error per coord. from scatter   
4	     sigm	h*2	    mas	    position error per coord. from model     
5	     nst	B*1  	--	    tot. number of sets the star is in      
6	     nsu	b*1  	--	    n. of sets used for mean position + flag 
7	     epoc	h*2  	myr	    mean URAT obs. epoch - 2000.0            (3)
8	     mmag	h*2  	mmag	mean URAT model fit magnitude            (4)
9	     sigp	h*2  	mmag	URAT photometry error                    
10	     nsm	B*1  	--	    number of sets used for URAT magnitude   
11	     ref	B*1	    --	    largest reference star flag              
12	     nit	h*2  	--	    total number of images (observations)
13	     niu	h*2	    --	    number of images used for mean position
14	     ngt	B*1	    --	    total number of 1st order grating obs.
15	     ngu	B*1  	--	    number of 1st order grating positions used
16	     pmr	h*2	 0.1mas/yr	proper motion RA*cosDec (from 2MASS)     
17	     pmd	h*2	 0.1mas/yr	proper motion Dec                        
18	     pme	h*2	 0.1mas/yr	proper motion error per coordinate       
19	     mf2	B*1  	--	    match flag URAT with 2MASS               
20	     mfa	B*1  	--	    match flag URAT with APASS               
21	     id2	i*4  	--	    unique 2MASS star identification number
22	     jmag	h*2  	mmag	2MASS J mag                              (5)
23	     hmag	h*2  	mmag  	2MASS H mag                              (6)
24	     kmag	h*2  	mmag	2MASS K mag                              (7)
25	     ejmag	h*2  	mmag	error 2MASS J mag
26	     ehmag	h*2  	mmag	error 2MASS H mag
27	     ekmag	h*2  	mmag	error 2MASS K mag
28	     iccj	B*1  	--	    CC flag 2MASS 
29	     icch	B*1	    --	    CC flag 2MASS H
30    	 icck	B*1  	--	    CC flag 2MASS K
31	     phqj	B*1  	--	    photometry quality flag 2MASS J          
32	     phqh	B*1  	--	    photometry quality flag 2MASS H
33	     phqk	B*1  	--	    photometry quality flag 2MASS K
34	     abm    h*2  	mmag	APASS B mag                             (8)
35	     avm	h*2  	mmag	APASS V mag                             (9)
36	     agm	h*2  	mmag	APASS g mag                            (10)
37	     arm	h*2  	mmag	APASS r mag                            (11)
38	     aim	h*2	    mmag	APASS i mag                            (12)
39	     ebm	h*2  	mmag	error APASS B mag
40	     evm	h*2  	mmag	error APASS V mag
41	     egm	h*2  	mmag	error APASS g mag
42	     erm	h*2  	mmag	error APASS r mag
43	     eim	h*2  	mmag	error APASS i mag
44	     ann	B*1  	--	    APASS numb. of nights                    
45	     ano	B*1  	--	    APASS numb. of observ.                   


80 = total number of bytes per star record



(1)
(2)                                  
(3) 
(4)
(5)
(6)
(7)
(8)
(9)
(10)
(11)
(12)
