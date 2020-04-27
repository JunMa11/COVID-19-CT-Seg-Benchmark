# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 19:43:47 2020

@author: JUN MA
"""

import numpy as np
import nibabel as nb
import os
from collections import OrderedDict
import pandas as pd
from SurfaceDice import compute_surface_distances, compute_surface_dice_at_tolerance, compute_dice_coefficient
join = os.path.join


seg_path = 'path to segmentation'
gt_path = 'path to ground truth'
save_path = 'path to save segmentation metrics'
save_name = 'Task_num_SegMetric.csv'

filenames = os.listdir(seg_path)
filenames.sort()
num_labels = np.max(nb.load(join(gt_path, filenames[0])).get_fdata())

seg_metrics = OrderedDict()
seg_metrics['Name'] = list()

if num_labels==1:
    seg_metrics['LesionDSC'] = list()
    seg_metrics['LesionNSD-3mm'] = list()

elif num_labels==2:
    seg_metrics['L-lungDSC'] = list()
    seg_metrics['L-lung-1mm'] = list()
    
    seg_metrics['R-lungDSC'] = list()
    seg_metrics['R-lung-1mm'] = list()
else:
    seg_metrics['L-lungDSC'] = list()
    seg_metrics['L-lung-1mm'] = list()
    
    seg_metrics['R-lungDSC'] = list()
    seg_metrics['R-lung-1mm'] = list()
    
    seg_metrics['LesionDSC'] = list()
    seg_metrics['LesionNSD-3mm'] = list()


for name in filenames:
    seg_metrics['Name'].append(name)
    # load grond truth and segmentation
    gt_nii = nb.load(join(gt_path, name))
    case_spacing = gt_nii.header.get_zooms()
    gt_data = np.uint8(gt_nii.get_fdata())
    seg_data = nb.load(join(seg_path, name)).get_fdata()
    
    labels = np.unique(gt_data)[1:]
    labels = labels.tolist()
    
    if num_labels==1: # Lesion
        surface_distances = compute_surface_distances(gt_data==1, seg_data==1, case_spacing)
        seg_metrics['LesionDSC'].append( compute_dice_coefficient(gt_data==1, seg_data==1))
        seg_metrics['LesionNSD-3mm'].append(compute_surface_dice_at_tolerance(surface_distances, 3))

    elif num_labels==2: # left and right lung
        surface_distances = compute_surface_distances(gt_data==1, seg_data==1, case_spacing)
        seg_metrics['L-lungDSC'].append(compute_dice_coefficient(gt_data==1, seg_data==1))
        seg_metrics['L-lung-1mm'].append(compute_surface_dice_at_tolerance(surface_distances, 1))  
        
        surface_distances = compute_surface_distances(gt_data==2, seg_data==2, case_spacing)
        seg_metrics['R-lungDSC'].append(compute_dice_coefficient(gt_data==2, seg_data==2))
        seg_metrics['R-lung-1mm'].append(compute_surface_dice_at_tolerance(surface_distances, 1))    

    else:      # left lung, right lung and infections
        surface_distances = compute_surface_distances(gt_data==1, seg_data==1, case_spacing)
        seg_metrics['L-lungDSC'].append( compute_dice_coefficient(gt_data==1, seg_data==1))
        seg_metrics['L-lung-1mm'].append( compute_surface_dice_at_tolerance(surface_distances, 1) )
        
        surface_distances = compute_surface_distances(gt_data==2, seg_data==2, case_spacing)
        seg_metrics['R-lungDSC'].append( compute_dice_coefficient(gt_data==2, seg_data==2))
        seg_metrics['R-lung-1mm'].append( compute_surface_dice_at_tolerance(surface_distances, 1))    
        
        surface_distances = compute_surface_distances(gt_data==3, seg_data==3, case_spacing)
        seg_metrics['LesionDSC'].append(compute_dice_coefficient(gt_data==3, seg_data==3))
        seg_metrics['LesionNSD-3mm'].append( compute_surface_dice_at_tolerance(surface_distances, 3))

dataframe = pd.DataFrame(seg_metrics)
dataframe.to_csv(join(save_path, save_name), index=False) 


 