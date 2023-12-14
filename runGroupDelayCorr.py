import os
from groupdelay import groupdelay

basedir="/Users/kjh6624/Documents/ANVIL/SPINAL_CORD/Neilsen/BreathHoldAnalysis/"
subjects=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,21,22,23,24,25,26,27,29,30]
# Excluded: 19,20,28
for id in subjects:
    for run in range(1,3):
        if id<=9:
            prefix="C0"+str(id)+"_S"+str(run)+"_SC_BH"
        else:
            prefix="C"+str(id)+"_S"+str(run)+"_SC_BH"
        print(prefix)
        stat_file="_cope1.nii.gz"
        plus1path=os.path.join(basedir,
                            "grpLevel-neilsen/RANDOMISE_blur_plus1/copes_indiv/", prefix+stat_file)
        plus2path=os.path.join(basedir,
                            "grpLevel-neilsen/RANDOMISE_blur_plus2/copes_indiv/", prefix+stat_file)
        plus3path=os.path.join(basedir,
                            "grpLevel-neilsen/RANDOMISE_blur_plus3/copes_indiv/", prefix+stat_file)
        plus4path=os.path.join(basedir,
                            "grpLevel-neilsen/RANDOMISE_blur_plus4/copes_indiv/", prefix+stat_file)
        plus5path=os.path.join(basedir,
                            "grpLevel-neilsen/RANDOMISE_blur_plus5/copes_indiv/", prefix+stat_file)
        noDelaypath=os.path.join(basedir,
                                "grpLevel-neilsen/RANDOMISE_blur_noDelay/copes_indiv/", prefix+stat_file)
        minus1path=os.path.join(basedir,
                                "grpLevel-neilsen/RANDOMISE_blur_minus1/copes_indiv/", prefix+stat_file)
        minus2path=os.path.join(basedir,
                                "grpLevel-neilsen/RANDOMISE_blur_minus2/copes_indiv/", prefix+stat_file)
        minus3path=os.path.join(basedir,
                                "grpLevel-neilsen/RANDOMISE_blur_minus3/copes_indiv/", prefix+stat_file)
        minus4path=os.path.join(basedir,
                                "grpLevel-neilsen/RANDOMISE_blur_minus4/copes_indiv/", prefix+stat_file)
        minus5path=os.path.join(basedir,
                                "grpLevel-neilsen/RANDOMISE_blur_minus5/copes_indiv/", prefix+stat_file)
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
        groupmask=os.path.join(basedir, "grpLevel-neilsen/RANDOMISE_blur_noDelay/group_mask.nii.gz")
        delaymap=os.path.join(basedir,"grpLevel-neilsen/delay/delayMap.nii.gz")
        out=os.path.join(basedir, "grpLevel-neilsen/delay", "copes_indiv")

        groupdelay.delayCorrectedSCVR(out,minus5,minus4,minus3,minus2,minus1,noDelay,
                            plus1,plus2,plus3,plus4,plus5,maskpath=groupmask,
                            delaymappath=delaymap,prefix=prefix)