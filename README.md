# SCVR

Scripts for **Spinal Cord Vascular Reactivity** (SCVR) delay mapping. The main functions are contained in `groupdelay.py`. Example run files are provided for group delay and individual subject delay (with multiple runs).

---
[![Twitter URL](https://img.shields.io/twitter/follow/KJHemm?style=social)](https://twitter.com/KJHemm)
[![MIT License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/BrightLab-ANVIL/SCVR/blob/main/LICENSE)
<br>

----
### Info:
These scripts were designed to take outputs from higher-level/group-level modeling including:
- t-statistic maps (other statistical maps would likely work but were not tested)
- parameter estimate maps (i.e., SCVR)
- group mask (this is the consensus mask in which the group analyses were run in)

This assumes that first-level and higher-level modeling were already performed at each desired temporal shift (delay). 

----
### Main Files and Usage:

**groupdelay.py**: Main code file that defines functions used in the run files. Should not need to be edited.

#### Group SCVR

1. **runGroupDelay.py**: Run file for calculation of group delay map.
- Takes the group-level statistic maps (e.g., t-stat maps from _randomise_) for all temporal shifts and calculates a delay map across the group.
- Outputs:
    - delayMap.nii.gz: 3D voxel-wise delay map
    - tstatMapsAll.nii.gz: 4D collated t-stat map for each time shift, used to calculate voxelwise max

2. **runGroupDelayCorr.py**: Run file for group delay correction.
- Takes parameter estimate files (e.g., cope files from FEAT, warped to template space) at each temporal shift and delay map to calculate delay-corrected SCVR maps. 
- Outputs: 
    - \<prefix>_delayCorrSCVR.nii.gz: delay-corrected SCVR map for each subject/run (3D)
    - \<prefix>_peMapsAll.nii.gz: 4D collated parameter estimate (SCVR) maps for each subject/run

3. Collect all delay-corrected SCVR files across subjects/runs and run higher-level stats (e.g., _randomise_).

#### Individual SCVR

1. **runIndivDelay.py**: Run file for individual delay map (e.g., for highly-sampled subjects).
- Takes the higher-level statistic maps (e.g., t-stat maps from _randomise_) for all temporal shifts and calculates a delay map across the runs.
- Outputs:
    - delayMap.nii.gz: 3D voxel-wise delay map
    - tstatMapsAll.nii.gz: 4D collated t-stat map for each time shift, used to calculate voxel-wise max

2. **runIndivDelayCorr.py**: Run file for individual delay correction.
- Takes parameter estimate files (e.g., cope files from FEAT, warped to template space) at each temporal shift and delay map to calculate delay-corrected SCVR maps. 
- Outputs:
    - \<prefix>_delayCorrSCVR.nii.gz: delay-corrected SCVR map for each fMRI run (3D)
    - \<prefix>_peMapsAll.nii.gz: 4D collated parameter estimate (SCVR) maps for each run

3. Collect all delay-corrected SCVR files across runs and run higher-level stats (e.g., _randomise_).

---
### Notes:
- [Randomise](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Randomise) was used for higher-level modeling in the development of these methods
- _This repository contains code to accompany the manuscript cited below, and has not been prepared as a general package for SCVR modeling and hemodynamic delay analysis._

----
### Citation: 
Hemmerling KJ, Hoggarth MA, Sandhu MS, Parrish TB, Bright MG. MRI mapping of hemodynamics in the human spinal cord. _Sci Rep_ 15, 34880 (2025). https://doi.org/10.1038/s41598-025-17048-4
