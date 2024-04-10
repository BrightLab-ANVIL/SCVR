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

1. **runIndivDelay.py**: takes the t-statistic maps (from _randomise_) for each time shift and calculates a group delay map. Outputs:
- delayMap.nii.gz: group average voxel-wise delay map.
- tstatMapsAll.nii.gz: group average statistical map with all time shifts concatenated in the 4th dimension.

2. **runIndivDelayCorr.py**: takes in the cope files (CVR maps) from each scan at each time shift and calculates a delay-corrected SCVR map for each scan. Outputs:
- _delayCorrSCVR.nii.gz: scan delay-corrected SCVR map.
- _peMapsAll.nii.gz: scan CVR map with all time shifts concatenated in the 4th dimension.

3. Run _randomise_ on scan-concatenated CVR maps.

---
### Notes:
- [Randomise](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Randomise) was used for higher-level modeling in the development of these methods

----
### Citation: 
[tbd]
