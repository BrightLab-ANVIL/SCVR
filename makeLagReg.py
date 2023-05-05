#!/usr/bin/env python3

import os
import numpy as np
import csv
from phys2cvr.phys2cvr import phys2cvr


def lagRegressor(
        TR,
        fname,
        increment=0.3,
        maxShift=5
        ):
    """
    Create .txt files of lagged regressors with .txt file regressor input.
    ARGUMENTS:
    TR : TR (in seconds)
    fname : file name, including full path to file (.txt)
    increment : lag regressor shifts (in seconds) [default: 0.3]
    maxShift : maximum positive and negative shift of input regressor (in seconds) [default: 5]
    """
    # Load input regressor
    inputReg=[]
    with open(fname) as fd:
        reader=csv.reader(fd)
        for row in reader:
            # print(row[0], type(row[0]))
            inputReg.append(float(row[0]))
    inputReg=np.array(inputReg)

    # Split fname into base fname and extension
    fname_split=os.path.basename(fname).split(".")
    pathToFile=os.path.dirname(fname)
    
    numRegs=np.floor(maxShift/increment)*2
    print(numRegs)

def extractCO2(fname):
    """
    Extract just CO2 regressor from text file (hires file from LabChart_Phys_Regressors)
    fname : Full path to text file
    """
    # Set column to extract (idx start at 0)
    col=1
    reg=[]
    with open(fname) as fd:
        reader=csv.reader(fd, delimiter='\t')
        for row in reader:
            reg.append(float(row[col]))
    reg=np.array(reg)
    # Split fname into base fname and extension
    fname_split=os.path.basename(fname).split(".")
    pathToFile=os.path.dirname(fname)
    
    fname_new=pathToFile+"/"+fname_split[0]+"_regOnly.txt"
    print("Saving regressor ONLY to new text file: ",fname_new)
    np.savetxt(fname_new,reg,fmt='%f')

# Testing my code (taking a break on this...)
co2path='/Users/kjh6624/Desktop/C03/C03_S1_SC_BH/regressors/C03_S1_SC_BH_CO2_HRFconv.txt'
# lagRegressor(2,co2path,increment=0.3,maxShift=1)

co2hires_orig="/Users/kjh6624/Desktop/C03/C03_S1_SC_BH/regressors/C03_S1_SC_BH_CO2_hires.txt"
extractCO2(co2hires_orig)
co2hires="/Users/kjh6624/Desktop/C03/C03_S1_SC_BH/regressors/C03_S1_SC_BH_CO2_hires_regOnly.txt"

# # Testing phys2cvr
# # Test 1: use input raw CO2 (hires), and file with peak indices
# phys2cvr("/Users/kjh6624/Desktop/C03/C03_S1_SC_BH/C03_S1_SC_BH.nii.gz",
#          fname_co2="/Users/kjh6624/Desktop/C03/C03_S1_SC_BH/regressors/test_co2_raw.txt",
#          fname_pidx="/Users/kjh6624/Desktop/C03/C03_S1_SC_BH/regressors/test_co2_peaksIDX.txt",
#          fname_mask="/Users/kjh6624/Desktop/C03/C03_S1_SC_BH/C03_S1_SC_BH_mask1slice.nii.gz",
#          outdir="/Users/kjh6624/Desktop/C03/C03_S1_SC_BH/phys2cvr_rawCO2",
#          freq=float(100),
#          lag_max=5,
#          lag_step=0.3,
#          run_regression=False,
#          skip_xcorr=True
#          )
# Test 2: use input of already HRF-convolved CO2 trace
phys2cvr("/Users/kjh6624/Desktop/C03/C03_S1_SC_BH/C03_S1_SC_BH.nii.gz",
         fname_co2=co2hires,
         fname_mask="/Users/kjh6624/Desktop/C03/C03_S1_SC_BH/C03_S1_SC_BH_mask1slice.nii.gz",
         outdir="/Users/kjh6624/Desktop/C03/C03_S1_SC_BH/phys2cvr_CO2convReg",
         run_conv=False,
         freq=float(100),
         lag_max=5,
         lag_step=0.25,
         run_regression=False,
         skip_xcorr=True
         )
# Test 1 vs. test 2: regressors look basically exactly the same... test 2: easier to format text
# file correctly for phys2cvr -> USE TEST 2

# I could use the xcorr to get the opt lag for that dataset in 
# the ROI I chose using createLagROI.sh
