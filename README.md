# Urat1
The first U.S. Naval Observatory Astrometric Robotic Telescope Catalog (URAT1)


The **urat1all.py** program is written in the Python programming language for decoding binary catalogs URAT1 (z326 ..... z900)
Decoded information is converted to a table and written to the postgresql database

items to read from input files:
     
i | int           | integer | 4 | ra, spd, id2

h | short         | integer | 2 | sigs, sigm, epoc, mmag, sigp, nit, niu, pmr, pmd, pme, jmag, 
                                  hmag, kmag, ejmag, ehmag, ekmag, abm, avm, agm, arm, aim
                                  
B | unsigned char | integer | 1 | nst, nsm, ref, ngt, ngu, mf2, mfa, iccj, icch, icck, phqj,
                                  phqh, phqk, ann, ano, ebm, evm, egm, erm, eim
                                  
b | signed char   | integer | 1 | nsu

			
<table>
<tr>
  <th>column</th>
  <th>item</th>
  <th>type</th>
  <th>unit</th>
  <th>description</th>
  <th>notes<th>
  </tr>
 <tr>
  <td>1</td>
  <td>ra</td>
  <td>i*4</td>
  <td>mas</td>
  <td>mean RA on ICRF at URAT mean obs.epoch</td>
  <th>(1)<th>
 </tr>
<tr>
  <td>2</td>
  <td>spd</td>
  <td>i*4</td>
  <td>mas</td>
  <td>mean South Pole Distance = Dec + 90 deg</td>
  <th>(2)<th>
</tr>
<tr>
  <td>3</td>
  <td>sigs</td>
  <td>h*2</td>
  <td>mas</td>
  <td>position error per coord. from scatter</td>
  <th><th>
</tr>
<tr>
  <td>4</td>
  <td>sigm</td>
  <td>h*2</td>
  <td>mas</td>
  <td>position error per coord. from model</td>
  <th><th>
</tr>
<tr>
  <td>5</td>
  <td>nst</td>
  <td>B*1</td>
  <td>--</td>
  <td>tot. number of sets the star is in </td>
  <th><th>
</tr>
<tr>
  <td>6</td>
  <td>nsu</td>
  <td>b*1</td>
  <td>--</td>
  <td>n. of sets used for mean position + flag </td>
  <th><th>
</tr>
<tr>
  <td>7</td>
  <td>epoc</td>
  <td>h*2</td>
  <td>myr</td>
  <td>mean URAT obs. epoch - 2000.0</td>
  <th>(3)<th>
</tr>
<tr>
  <td>8</td>
  <td>mmag</td>
  <td>h*2</td>
  <td>mmag</td>
  <td>mean URAT model fit magnitude</td>
  <th>(4)<th>
</tr>
<tr>
  <td>9</td>
  <td>sigp</td>
  <td>h*2</td>
  <td>mmag</td>
  <td>URAT photometry error</td>
  <th><th>
</tr>
<tr>
  <td>10</td>
  <td>nsm</td>
  <td>B*1</td>
  <td>--</td>
  <td>number of sets used for URAT magnitude</td>
  <th><th>
</tr>
<tr>
  <td>11</td>
  <td>ref</td>
  <td>B*1</td>
  <td>--</td>
  <td>largest reference star flag</td>
  <th><th>
</tr>
<tr>
  <td>12</td>
  <td>nit</td>
  <td>h*2</td>
  <td>--</td>
  <td>total number of images (observations)</td>
  <th><th>
</tr>
<tr>
  <td>13</td>
  <td>niu</td>
  <td>h*2</td>
  <td>--</td>
  <td>number of images used for mean position</td>
  <th><th>
</tr>
<tr>
  <td>14</td>
  <td>ngt</td>
  <td>B*1</td>
  <td>--</td>
  <td>total number of 1st order grating obs.</td>
  <th><th>
</tr>
<tr>
  <td>15</td>
  <td>ngu</td>
  <td>B*1</td>
  <td>--</td>
  <td>number of 1st order grating positions used</td>
  <th><th>
</tr>
<tr>
  <td>16</td>
  <td>pmr</td>
  <td>h*2</td>
  <td>0.1mas/yr</td>
  <td>proper motion RA*cosDec (from 2MASS)</td>
  <th><th>
</tr>
<tr>
  <td>17</td>
  <td>pmd</td>
  <td>h*2</td>
  <td>0.1mas/yr</td>
  <td>proper motion Dec</td>
  <th><th>
</tr>
<tr>
  <td>18</td>
  <td>pme</td>
  <td>h*2</td>
  <td>0.1mas/yr</td>
  <td>proper motion error per coordinate</td>
  <th><th>
</tr>
<tr>
  <td>19</td>
  <td>mf2</td>
  <td>B*1</td>
  <td>--</td>
  <td>match flag URAT with 2MASS</td>
  <th><th>
</tr>
<tr>
  <td>20</td>
  <td>mfa</td>
  <td>B*1</td>
  <td>--</td>
  <td>match flag URAT with APASS</td>
  <th><th>
</tr>
<tr>
  <td>21</td>
  <td>id2</td>
  <td>i*4</td>
  <td>--</td>
  <td>unique 2MASS star identification number</td>
  <th><th>
</tr>
<tr>
  <td>22</td>
  <td>jmag</td>
  <td>h*2</td>
  <td>mmag</td>
  <td>2MASS J mag</td>
  <th>(5)<th>
</tr>
<tr>
  <td>23</td>
  <td>hmag</td>
  <td>h*2</td>
  <td>mmag</td>
  <td>2MASS H mag</td>
  <th>(6)<th>
</tr>
<tr>
  <td>24</td>
  <td>kmag</td>
  <td>h*2 </td>
  <td>mmag</td>
  <td>2MASS K mag</td>
  <th>(7)<th>
</tr>
<tr>
  <td>25</td>
  <td>ejmag</td>
  <td>h*2</td>
  <td>mmag</td>
  <td>error 2MASS J mag</td>
  <th><th>
</tr>
<tr>
  <td>26</td>
  <td>ehmag</td>
  <td>h*2</td>
  <td>mmag</td>
  <td>error 2MASS H mag</td>
  <th><th>
</tr>
<tr>
  <td>27</td>
  <td>ekmag</td>
  <td>h*2</td>
  <td>mmag</td>
  <td>error 2MASS K mag</td>
  <th><th>
</tr>
<tr>
  <td>28</td>
  <td>iccj</td>
  <td>B*1</td>
  <td>--</td>
  <td>CC flag 2MASS</td>
  <th><th>
</tr>
<tr>
  <td>29</td>
  <td>icch</td>
  <td>B*1</td>
  <td>--</td>
  <td>CC flag 2MASS H</td>
  <th><th>
</tr>
<tr>
  <td>30</td>
  <td>icck</td>
  <td>B*1</td>
  <td>--</td>
  <td>CC flag 2MASS K</td>
  <th><th>
</tr>
<tr>
  <td>31</td>
  <td>phqj</td>
  <td>B*1</td>
  <td>--</td>
  <td>photometry quality flag 2MASS J</td>
  <th><th>
</tr>
<tr>
  <td>32</td>
  <td>phqh</td>
  <td>B*1</td>
  <td>--</td>
  <td>photometry quality flag 2MASS H</td>
  <th><th>
</tr>
<tr>
  <td>33</td>
  <td>phqk</td>
  <td>B*1</td>
  <td>--</td>
  <td>photometry quality flag 2MASS K</td>
  <th><th>
</tr>
<tr>
  <td>34</td>
  <td>abm</td>
  <td>h*2</td>
  <td>mmag</td>
  <td>APASS B mag</td>
  <th>(8)<th>
</tr>
<tr>
  <td>35</td>
  <td>avm</td>
  <td>h*2</td>
  <td>mmag</td>
  <td>APASS V mag</td>
  <th>(9)<th>
</tr>
<tr>
  <td>36</td>
  <td>agm</td>
  <td>h*2</td>
  <td>mmag</td>
  <td>APASS g mag</td>
  <th>(10)<th>
</tr>
<tr>
  <td>37</td>
  <td>arm</td>
  <td>h*2</td>
  <td>mmag</td>
  <td>APASS r mag</td>
  <th>(11)<th>
</tr>
<tr>
  <td>38</td>
  <td>aim</td>
  <td>h*2</td>
  <td>mmag</td>
  <td>APASS i mag</td>
  <th>(12)<th>
</tr>
<tr>
  <td>39</td>
  <td>ebm</td>
  <td>h*2</td>
  <td>mmag</td>
  <td>error APASS B mag</td>
  <th><th>
</tr>
<tr>
  <td>40</td>
  <td>evm</td>
  <td>h*2</td>
  <td>mmag</td>
  <td>error APASS V mag</td>
  <th><th>
</tr>
<tr>
  <td>41</td>
  <td>egm</td>
  <td>h*2</td>
  <td>mmag</td>
  <td>error APASS g mag</td>
  <th><th>
</tr>
<tr>
  <td>42</td>
  <td>erm</td>
  <td>h*2 </td>
  <td>mma</td>
  <td>g	error APASS r mag</td>
  <th><th>
</tr>
<tr>
  <td>43</td>
  <td>eim</td>
  <td>h*2</td>
  <td>mmag</td>
  <td>error APASS i mag</td>
  <th><th>
</tr>
<tr>
  <td>44</td>
  <td>ann</td>
  <td>B*1</td>
  <td>--</td>
  <td>APASS numb. of nights</td>
  <th><th>
</tr>
<tr>
  <td>45</td>
  <td>ano</td>
  <td>B*1</td>
  <td>--</td>
  <td> APASS numb. of observ.</td>
  <th><th>
</tr>
</table>

<<<<<<< HEAD
caption {
caption-side: bottom;
text-align: right;
padding: 10px 0; 
font-size: 14px;
}
=======

>>>>>>> 0af4a25118ec83b5867dc75a4a89d701f7c78e44
    	  		                      
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
