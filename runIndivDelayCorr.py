import os
from groupdelay import groupdelay

# Run file for within subject delay correction (e.g., highly sampled subjects with multiple runs)

basedir="/path/to/base/directory/"
# Subject ID
subj="sub-01"
print("subject: "+subj)
for run in range(1,19):
    if run<=9:
        prefix=subj+ "_run-0"+str(run)
    else:
        prefix=subj+ "_run-"+str(run)
    print(prefix)
    # Define paths to parameter estimate files for all shifts
    stat_file="_cope1.nii.gz"
    minus5path=os.path.join(basedir,
                            "path/to/", prefix+stat_file)
    minus4path=os.path.join(basedir,
                            "path/to/", prefix+stat_file)
    minus3path=os.path.join(basedir,
                            "path/to/", prefix+stat_file)
    minus2path=os.path.join(basedir,
                            "path/to/", prefix+stat_file)
    minus1path=os.path.join(basedir,
                            "path/to/", prefix+stat_file)
    noDelaypath=os.path.join(basedir,
                            "path/to/", prefix+stat_file)
    plus1path=os.path.join(basedir,
                        "path/to/", prefix+stat_file)
    plus2path=os.path.join(basedir,
                        "path/to/", prefix+stat_file)
    plus3path=os.path.join(basedir,
                        "path/to/", prefix+stat_file)
    plus4path=os.path.join(basedir,
                        "path/to/", prefix+stat_file)
    plus5path=os.path.join(basedir,
                        "path/to/", prefix+stat_file)
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
    # Define path to consensus mask
    groupmask=os.path.join(basedir, "path/to/group_mask.nii.gz")
    # Define path to delay map (requres running getBestFits first)
    delaymap=os.path.join(basedir, "path/to/delayMap.nii.gz")
    # Define path to output directory
    out=os.path.join(basedir, "path/to", "folder")
    # Run delay correction
    groupdelay.delayCorrectedSCVR(out,minus5,minus4,minus3,minus2,minus1,noDelay,
                        plus1,plus2,plus3,plus4,plus5,maskpath=groupmask,
                        delaymappath=delaymap,prefix=prefix)
