import os
from grouplag import grouplag


basedir="/Users/kjh6624/Documents/ANVIL/SPINAL_CORD/Neilsen/BreathHoldAnalysis/"
plus1path=os.path.join(basedir,
                       "grpLevel/RANDOMISE_plus1/onesamp_t/BH_plus1_cope1_S1S2_AVG/BH_plus1_cope1_tstat1.nii.gz")
plus2path=os.path.join(basedir,
                       "grpLevel/RANDOMISE_plus2/onesamp_t/BH_plus2_cope1_S1S2_AVG/BH_plus2_cope1_tstat1.nii.gz")
plus3path=os.path.join(basedir,
                       "grpLevel/RANDOMISE_plus3/onesamp_t/BH_plus3_cope1_S1S2_AVG/BH_plus3_cope1_tstat1.nii.gz")
plus4path=os.path.join(basedir,
                       "grpLevel/RANDOMISE_plus4/onesamp_t/BH_plus4_cope1_S1S2_AVG/BH_plus4_cope1_tstat1.nii.gz")
plus5path=os.path.join(basedir,
                       "grpLevel/RANDOMISE_plus5/onesamp_t/BH_plus5_cope1_S1S2_AVG/BH_plus5_cope1_tstat1.nii.gz")
noDelaypath=os.path.join(basedir,
                         "grpLevel/RANDOMISE_noDelay/onesamp_t/BH_noDelay_cope1_S1S2_AVG/BH_noDelay_cope1_tstat1.nii.gz")
minus1path=os.path.join(basedir,
                        "grpLevel/RANDOMISE_minus1/onesamp_t/BH_minus1_cope1_S1S2_AVG/BH_minus1_cope1_tstat1.nii.gz")
minus2path=os.path.join(basedir,
                        "grpLevel/RANDOMISE_minus2/onesamp_t/BH_minus2_cope1_S1S2_AVG/BH_minus2_cope1_tstat1.nii.gz")
minus2=grouplag.LagBH(-2,minus2path)
minus1=grouplag.LagBH(-1,minus1path)
noDelay=grouplag.LagBH(0,noDelaypath)
plus1=grouplag.LagBH(1,plus1path)
plus2=grouplag.LagBH(+2,plus2path)
plus3=grouplag.LagBH(3,plus3path)
plus4=grouplag.LagBH(4,plus4path)
plus5=grouplag.LagBH(5,plus5path)
groupmask=os.path.join(basedir, "grpLevel/RANDOMISE_noDelay/group_mask.nii.gz")

out=os.path.join(basedir, "grpLevel/")
# out=os.path.join(basedir, "grpLevel")
grouplag.getBestFits(out,minus2,minus1,noDelay,plus1,plus2,plus3,plus4,plus5,maskpath=groupmask)
# grouplag.getBestFits(out,minus2,minus1,noDelay,plus1,plus2,plus3,plus4,plus5) 
