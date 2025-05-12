#!/usr/bin/env python3

import os
import numpy as np
import nibabel as nib
import warnings

class DelayBH:
  def __init__(self, delay, tstatpath):
      self.delayNum = delay
      self.path = tstatpath
      self.img=self.loadData()

  def loadData(self):
    # ARGUMENTS:
    # Load nifti file
    # Adds back to self
    imgFile=nib.load(self.path)
    img=imgFile.get_fdata()
    return img

def getBestFits(outdir,*tstatmap,maskpath=None):
  # ARGUMENTS:
  # outdir: 'path/to/output/directory'
  # *tstatmap: DelayBH objects (wording?)
  # (optional) maskpath='path/to/groupmask.nii.gz'
  
  # USAGE: 
  # getBestFits('path/to/output/directory',DelayBH1,DelayBH2,...,maskpath='group/mask/path')

  # Note: Right now any delay value that =0 is set to a really small number so that it 
  # is distinct from the background (for visualization purposes) 0.00000000000001
  
  # Load "template" image for nifti output & header info
  template=nib.load(tstatmap[0].path)
  template_shape=template.header.get_data_shape()
  # print("original hdr: ", template_header)

  # Get number of input tstat maps
  numData=len(tstatmap)
  
  # Create 4D array of zeros – size of nifti and 4th dimension: numData
  # allMaps=np.zeros(tstatmap[0].img.shape)
  allMaps=np.zeros((template_shape[0], template_shape[1], template_shape[2], numData))
  # Then fill this with the maps (or maybe just append them all to each other)
  mapNum=0
  for map in tstatmap:
    print("Delay:", map.delayNum,"TRs")
    # allMaps=np.append(allMaps,map)
    allMaps[:,:,:,mapNum]=map.img
    mapNum+=1  

  # Set new header dimensions (shape datatype is tuple)
  new_shape=(template_shape[0], template_shape[1], template_shape[2], numData)
  template.header.set_data_shape(new_shape)
  # print("new hdr: ", template.header)

  # Print nifti file of all tstat maps
  allMapsNii=nib.Nifti1Image(allMaps, template.affine, template.header)
  outpath=os.path.join(outdir,"tstatMapsAll.nii.gz")
  nib.save(allMapsNii, outpath)

  # DELAY MAP: Find across the 4th dimension (of non-zero voxels)
  delayMap=np.zeros((template_shape[0], template_shape[1], template_shape[2]))
  # Use indices of nonzero voxels (in mask or in tstat file):
  if maskpath: 
    # If maskpath was given, find nonzero in group mask
    mask=nib.load(maskpath)
    maskimg=mask.get_fdata()
    specified=maskimg.nonzero()
  else:
    # If maskpath was not given, find nonzero in first tstat map
    specified=allMaps[:,:,:,0].nonzero()

  for (x,y,z) in zip(*specified):    
    # print(allMaps[x,y,z,:]) # current voxel
    # print(np.amax(allMaps[x,y,z,:], axis=0)) # max t-stat
    # print(np.argmax(allMaps[x,y,z,:], axis=0)) # max t-stat idx
    maxTstatIdx_temp=np.argmax(allMaps[x,y,z,:], axis=0)
    delay_temp=tstatmap[maxTstatIdx_temp].delayNum
    if delay_temp==0:
      delay_temp=0.00000000000001
    delayMap[x,y,z]=delay_temp
  
  orig=nib.load(tstatmap[0].path)
  delayMapNii=nib.Nifti1Image(delayMap, orig.affine, orig.header)
  outpath_delay=os.path.join(outdir,"delayMap.nii.gz")
  nib.save(delayMapNii, outpath_delay)
  
  print("View delay map:")
  print("fsleyes ",outpath_delay,"&")



def delayCorrectedSCVR(outdir,*betamap,maskpath=None,delaymappath=None,
                     prefix=None):
  # Create delay corrected SCVR map with best fits 
  # Requires running getBestFits() first
  # Uses the delay map output and the parameter estimates 
  # in each randomise delay folder to construct a delay-corrected SCVR 
  # output file (for each fMRI run).
  # 
  # ARGUMENTS:
  # outdir: 'path/to/output/directory'
  # *betamaps: DelayBH objects
  # delaymappath='path/to/delayMap.nii.gz'
  # (optional) maskpath='path/to/groupmask.nii.gz'
  # (optional) prefix='sub-01_run-01'
  # 
  # USAGE: 
  # delayCorrectedSCVR('path/to/output/directory',DelayBH1,DelayBH2,...,
  # delaymappath='path/to/delayMap.nii.gz',maskpath='path/to/mask.nii.gz')

  # Load "template" image for nifti output & header info
  template=nib.load(betamap[0].path)
  template_shape=template.header.get_data_shape()

  # Get number of input beta maps
  numData=len(betamap)

  # Check that range of values in delay map does not exceed # beta maps
  delaymap=nib.load(delaymappath)
  delaymap_img=delaymap.get_fdata()
  delaymap_range=np.ptp(delaymap_img)
  if delaymap_range>numData:
    warnings.warn("Delay map range exceeds number of input beta maps")


  # Create 4D array of zeros – size of nifti and 4th dimension: numData
  allMaps=np.zeros((template_shape[0], template_shape[1], template_shape[2], numData))
  # Then fill this with the maps (or maybe just append them all to each other)
  mapNum=0
  indexRef={}
  for map in betamap:
    print("Delay:", map.delayNum, "TRs")
    # Compile all beta maps into allMaps
    allMaps[:,:,:,mapNum]=map.img
    
    # Create dictionary to index this
    # map.delayNum ––– 0, 1, etc.
    indexRef[map.delayNum] = mapNum
    mapNum+=1
  print("INDEX REFS:")
  print(indexRef)

  # Print nifti file of all pe/beta maps
  allMapsNii=nib.Nifti1Image(allMaps, template.affine, template.header)
  if prefix==None:
    outpath=os.path.join(outdir,"peMapsAll.nii.gz")
  else:
    outpath=os.path.join(outdir,prefix+"_peMapsAll.nii.gz")
  nib.save(allMapsNii, outpath)

  # DELAY CORR MAP: Find across the 4th dimension (of non-zero voxels)
  corrSCVR=np.zeros((template_shape[0], template_shape[1], template_shape[2]))

  # Use indices of nonzero voxels (in mask or in beta file):
  if maskpath: 
    # If maskpath was given, find nonzero in group mask
    mask=nib.load(maskpath)
    maskimg=mask.get_fdata()
    specified=maskimg.nonzero()
  else:
    # If maskpath was not given, find nonzero in first beta map
    specified=allMaps[:,:,:,0].nonzero()

  for (x,y,z) in zip(*specified):
    # Get delay at each voxel location
    voxelDelay=int(delaymap_img[x,y,z])

    # Fill corrected SCVR map with the appropriate beta parameter
    # (using indexRef dictionary)
    corrSCVR[x,y,z]=allMaps[x,y,z,indexRef[voxelDelay]]

  # Save nifti
  orig=nib.load(betamap[0].path)
  corrSCVRNii=nib.Nifti1Image(corrSCVR, orig.affine, orig.header)
  if prefix==None:
    outpath_SCVR=os.path.join(outdir,"delayCorrSCVR.nii.gz")
  else:
    outpath_SCVR=os.path.join(outdir,prefix+"_delayCorrSCVR.nii.gz")
  nib.save(corrSCVRNii, outpath_SCVR)
  
  print("View delay map:")
  print("fsleyes ",outpath_SCVR,"&")

"""
Written by Kimberly J. Hemmerling 2023
"""
