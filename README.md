# SCVR

Scripts **Spinal Cord Vascular Reactivity** (SCVR) delay mapping. The main functions are contained in `groupdelay.py`. 

---
[![Twitter URL](https://img.shields.io/twitter/follow/KJHemm?style=social)](https://twitter.com/KJHemm)
[![MIT License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/BrightLab-ANVIL/SCVR/blob/main/LICENSE)
<br>

----
### How to Use:
These scripts were designed to take outputs from higher-level/group-level modeling including:
- T-statistic map (other statistical maps would also probably work)
- Group mask (this is the mask in which the group analyses were run in)

Requires the _nibabel_ python package.

### Code files:

**groupdelay.py**: a generic code file that defines functions used in the run files, and does not need specific editing.

**runGroupDelay.py**: takes the t-statistic maps for each time shift and calculates a group delay map.
- delayMap.nii.gz: group average voxel-wise delay map.
- tstatMapsAll.nii.gz: group average statistical map with all time shifts concatenated in the 4th dimension.

**runGroupDelayCorr.py**: takes in the cope files from each scan at each time shift and calculates a delay-corrected group average SCVR map with delay-corrected individual cope files.
- _delayCorrSCVR.nii.gz: group delay-corrected SCVR map.
- _peMapsAll.nii.gz: group average CVR map with all time shifts concatenated in the 4th dimension.

---
### Notes:
- [Randomise](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Randomise) was used for higher-level modeling in the development of these methods

----
### Citation: 
[tbd]
