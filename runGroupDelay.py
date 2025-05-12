import os
from groupdelay import groupdelay

# Run file to calculate group delay map

basedir="/path/to/base/directory/"
# Define paths to statistic (e.g., t-stat) files
stat_file="cope1_tstat1.nii.gz"
minus5path=os.path.join(basedir,
                        "path/to/minus5/", stat_file)
minus4path=os.path.join(basedir,
                        "path/to/minus4/", stat_file)
minus3path=os.path.join(basedir,
                        "path/to/minus3/", stat_file)
minus2path=os.path.join(basedir,
                        "path/to/minus2/", stat_file)
minus1path=os.path.join(basedir,
                        "path/to/minus1/", stat_file)
noDelaypath=os.path.join(basedir,
                         "path/to/noDelay/", stat_file)
plus1path=os.path.join(basedir,
                       "path/to/plus1/", stat_file)
plus2path=os.path.join(basedir,
                       "path/to/plus2/", stat_file)
plus3path=os.path.join(basedir,
                       "path/to/plus3/", stat_file)
plus4path=os.path.join(basedir,
                       "path/to/plus4/", stat_file)
plus5path=os.path.join(basedir,
                       "path/to/plus5/", stat_file)
minus5=groupdelay.DelayBH(-5,minus5path)
minus4=groupdelay.DelayBH(-4,minus4path)
minus3=groupdelay.DelayBH(-3,minus3path)
minus2=groupdelay.DelayBH(-2,minus2path)
minus1=groupdelay.DelayBH(-1,minus1path)
noDelay=groupdelay.DelayBH(0,noDelaypath)
plus1=groupdelay.DelayBH(1,plus1path)
plus2=groupdelay.DelayBH(+2,plus2path)
plus3=groupdelay.DelayBH(3,plus3path)
plus4=groupdelay.DelayBH(4,plus4path)
plus5=groupdelay.DelayBH(5,plus5path)
# Define path to group consensus mask
groupmask=os.path.join(basedir, "path/to/group_mask.nii.gz")
# Define path to output directory
out=os.path.join(basedir, "path/to", "folder")
# Calculate delay map
groupdelay.getBestFits(out,minus5,minus4,minus3,minus2,minus1,noDelay,
                       plus1,plus2,plus3,plus4,plus5,maskpath=groupmask)
