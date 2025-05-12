import os
from groupdelay import groupdelay

# Run file for group-level delay correction

basedir="/path/to/base/directory/"
# List of subjects
subjects=[1,2,3,4,5,6,7,8,9,10]
for id in subjects:
    for run in range(1,3):
        if id<=9:
            prefix="sub-0" + str(id) + "_run-0"+str(run)
        else:
            prefix="sub-" + str(id) + "_run-0"+str(run)
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
        # Define each delay with inputs: (delay, path/to/stat/file)
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
        # Define path to delay map (requres running getBestFits first)
        delaymap=os.path.join(basedir, "path/to/delayMap.nii.gz")
        # Define path to output directory
        out=os.path.join(basedir, "path/to", "folder")
        # Run delay correction
        groupdelay.delayCorrectedSCVR(out,minus5,minus4,minus3,minus2,minus1,noDelay,
                            plus1,plus2,plus3,plus4,plus5,maskpath=groupmask,
                            delaymappath=delaymap,prefix=prefix)
