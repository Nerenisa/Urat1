# Urat1
The first U.S. Naval Observatory Astrometric Robotic Telescope Catalog (URAT1)

There are 45 columns of URAT1 data.



column item type  unit     description                             
------------------------------------------------------------------------
  1  ra      I*4  mas      mean RA on ICRF at URAT mean obs.epoch   
  2  spd     I*4  mas      mean South Pole Distance = Dec + 90 deg  
  3  sigs    I*2  mas      position error per coord. from scatter   
  4  sigm    I*2  mas      position error per coord. from model     
  5  nst     I*1  --       tot. number of sets the star is in       
  6  nsu     I*1  --       n. of sets used for mean position + flag 
  7  epoc    I*2  myr      mean URAT obs. epoch - 2000.0            
  8  mmag    I*2  mmag     mean URAT model fit magnitude            
  9  sigp    I*2  mmag     URAT photometry error                    
 10  nsm     I*1  --       number of sets used for URAT magnitude   
 11  ref     I*1  --       largest reference star flag              
 12  nit     I*2  --       total number of images (observations)
 13  niu     I*2  --       number of images used for mean position
 14  ngt     I*1  --       total number of 1st order grating obs.
 15  ngu     I*1  --       number of 1st order grating positions used
 16  pmr     I*2 0.1mas/yr proper motion RA*cosDec (from 2MASS)     
 17  pmd     I*2 0.1mas/yr proper motion Dec                        
 18  pme     I*2 0.1mas/yr proper motion error per coordinate       
 19  mf2     I*1  --       match flag URAT with 2MASS               
 20  mfa     I*1  --       match flag URAT with APASS               
 21  id2     I*4  --       unique 2MASS star identification number
 22  jmag    I*2  mmag     2MASS J mag
 23  hmag    I*2  mmag     2MASS H mag
 24  kmag    I*2  mmag     2MASS K mag
 25  ejmag   I*2  mmag     error 2MASS J mag
 26  ehmag   I*2  mmag     error 2MASS H mag
 27  ekmag   I*2  mmag     error 2MASS K mag
 28  iccj    I*1  --       CC flag 2MASS J                          
 29  icch    I*1  --       CC flag 2MASS H
 30  icck    I*1  --       CC flag 2MASS K
 31  phqj    I*1  --       photometry quality flag 2MASS J          
 32  phqh    I*1  --       photometry quality flag 2MASS H
 33  phqk    I*1  --       photometry quality flag 2MASS K
 34  abm     I*2  mmag     APASS B mag                              
 35  avm     I*2  mmag     APASS V mag
 36  agm     I*2  mmag     APASS g mag
 37  arm     I*2  mmag     APASS r mag
 38  aim     I*2  mmag     APASS i mag
 39  ebm     I*2  mmag     error APASS B mag
 40  evm     I*2  mmag     error APASS V mag
 41  egm     I*2  mmag     error APASS g mag
 42  erm     I*2  mmag     error APASS r mag
 43  eim     I*2  mmag     error APASS i mag
 44  ann     I*1  --       APASS numb. of nights                    
 45  ano     I*1  --       APASS numb. of observ.                  
------------------------------------------------------------------------
             80 = total number of bytes per star record

