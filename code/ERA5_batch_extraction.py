# -*- coding: utf-8 -*-
"""

Work out the extraction of the fields Ray Graham needs for his MS thesis.
Goal: time series of column-integrated moisture convergence at site
Requires: either div(q*U) or q*div(U)+grad(q)-dot-U
Time: 09/01/2016 - 10/31/17
Lat: 8.5 - 11.5 N.
Lon: 126.5 - 123.5 W

Modified from:
C:/Users/jtomf/Documents/Python/WHOTS_WG_proposal/ERA5_batch_extraction.py
C:/Users/jtomf/Documents/Python/WHOTS_WG_proposal/ERA5_extraction_tool.py
C:/Users/jtomf/Documents/Python/ERA5_plots/read_ERA5_SPURS2_Copernicus_CDS_API.py


Created on Thu Jun  3 21:14:11 2021

@author: jtomf
"""

import ERA5_extraction_tool
import numpy as np
import time
################
# This allows us to import Tom_tools_v1
import sys
sys.path.append('C:/Users/jtomf/Documents/Python/Tom_tools/')
################
import Tom_tools_v1 as tt


var=['specific_humidity', 'u_component_of_wind', 'v_component_of_wind']
#yrs=['2016', '2017']
#mons= ['01', '02', '03','04', '05', '06','07', '08', '09','10', '11', '12']
yrs=['2016']
mons= ['09', '10', '11', '12']

# 'specific_cloud_liquid_water_content', 'u_component_of_wind', 'v_component_of_wind', 'vertical_velocity'

for varname in var:
    for yr in yrs:
        for mon in mons:
            tt.tic()
            ERA5_extraction_tool.get_vars_for_Ray(varname,yr,mon)
            tt.toc()
            time.sleep(25) # I am not sure this helps, but it seems like 
                          # rapid repeated requests may cause it to bog down
                          # For some reason, the first 2 requests are quickly processed
                          # and the third one takes very long

