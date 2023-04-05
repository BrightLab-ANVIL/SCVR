#!/usr/bin/env python3

import os
import numpy as np
import nibabel as nib

class LagBH:
  def __init__(self, lag, tstatpath):
      self.lagNum = lag
      self.path = tstatpath
      self.img=self.loadData()

  def loadData(self):
    # ARGUMENTS:    
    # Load tstat nifti file
    # Adds back to self
    imgFile=nib.load(self.path)
    img=imgFile.get_fdata()
    return img

def getBestFits(outdir,*tstatmap,**maskpath):
  # ARGUMENTS:
  # outdir: 'path/to/output/directory'
  # *tstatmap: LagBH objects (wording?)
  # (optional) maskpath='path/to/groupmask.nii.gz'
  
  # USAGE: 
  # getBestFits('path/to/output/directory',LagBH1,LagBH2,...,maskpath='group/mask/path')
  
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
    print("Lag:", map.lagNum,"TRs")
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

  # LAG MAP: Find across the 4th dimension (of non-zero voxels)
  lagMap=np.zeros((template_shape[0], template_shape[1], template_shape[2]))
  # indices of nonzero voxels (in mask or in tstat file):
  if maskpath: 
    # If maskpath was given, find nonzero in group mask
    mask=nib.load(maskpath["maskpath"])
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
    lag_temp=tstatmap[maxTstatIdx_temp].lagNum
    lagMap[x,y,z]=lag_temp
  
  orig=nib.load(tstatmap[0].path)
  lagMapNii=nib.Nifti1Image(lagMap, orig.affine, orig.header)
  outpath_lag=os.path.join(outdir,"lagMap.nii.gz")
  nib.save(lagMapNii, outpath_lag)
  
  print("View lag map:")
  print("fsleyes ",outpath_lag,"&")


"""
Written by Kimberly J. Hemmerling 2023
"""
