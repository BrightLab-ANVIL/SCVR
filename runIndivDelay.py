import os
from groupdelay import groupdelay

subj="BH-03"
print("subject: "+subj)
prefix=subj+ "_combo-18"
stat_file=subj + "_combo-18_tstat1.nii.gz"
basedir="/Users/kjh6624/Documents/ANVIL/SPINAL_CORD/Neilsen/BreathHoldAnalysis/"
plus1path=os.path.join(basedir,
                       "grpLevel-BH18/RANDOMISE_blur_plus1/onesamp_t/", prefix, stat_file)
plus2path=os.path.join(basedir,
                       "grpLevel-BH18/RANDOMISE_blur_plus2/onesamp_t/", prefix, stat_file)
plus3path=os.path.join(basedir,
                       "grpLevel-BH18/RANDOMISE_blur_plus3/onesamp_t/", prefix, stat_file)
plus4path=os.path.join(basedir,
                       "grpLevel-BH18/RANDOMISE_blur_plus4/onesamp_t/", prefix, stat_file)
plus5path=os.path.join(basedir,
                       "grpLevel-BH18/RANDOMISE_blur_plus5/onesamp_t/", prefix, stat_file)
noDelaypath=os.path.join(basedir,
                         "grpLevel-BH18/RANDOMISE_blur_noDelay/onesamp_t/", prefix, stat_file)
minus1path=os.path.join(basedir,
                        "grpLevel-BH18/RANDOMISE_blur_minus1/onesamp_t/", prefix, stat_file)
minus2path=os.path.join(basedir,
                        "grpLevel-BH18/RANDOMISE_blur_minus2/onesamp_t/", prefix, stat_file)
minus3path=os.path.join(basedir,
                        "grpLevel-BH18/RANDOMISE_blur_minus3/onesamp_t/", prefix, stat_file)
minus4path=os.path.join(basedir,
                        "grpLevel-BH18/RANDOMISE_blur_minus4/onesamp_t/", prefix, stat_file)
minus5path=os.path.join(basedir,
                        "grpLevel-BH18/RANDOMISE_blur_minus5/onesamp_t/", prefix, stat_file)
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
groupmask=os.path.join(basedir, "grpLevel-BH18/RANDOMISE_blur_noDelay/group_mask.nii.gz")

out=os.path.join(basedir, "grpLevel-BH18/", subj+"_delay",)
groupdelay.getBestFits(out,minus5,minus4,minus3,minus2,minus1,noDelay,
                     plus1,plus2,plus3,plus4,plus5,maskpath=groupmask)
