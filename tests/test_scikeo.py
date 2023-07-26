#!/usr/bin/env python
# -*- coding: utf-8 -*-
# +
""" Tests for the scikit-eo package. """

import numpy as np
import pytest
import rasterio
import pandas as pd
from scikeo.process import confintervalML
from scikeo.sma import sma
from scikeo.pca import PCA
from scikeo.tassCap import tassCap
from scikeo.fusionrs import fusionrs
from scikeo.process import crop


def test_confintervalML():
    
    """Confusion Matrix by Estimated Proportions of area an uncertainty is tested. 
    
    To carry out it, this function was tested using ground-truth values obtained by 
    Olofsson et al. (2014).
    """
    conf_error = pd.read_csv("tests/data/confusion_matrix.csv", index_col= 0, sep = ';')
    # only confusion matrix values
    values = conf_error.iloc[0:4,0:4].to_numpy()
    # number of pixels for each class
    img = np.array([200000, 150000, 3200000, 6450000])
    res = confintervalML(matrix = values, image_pred = img, pixel_size = 30, nodata = -9999)
    assert round(res.get('Overall_accuracy'),3) == 0.947
    
def test_sma():
    """Confusion Matrix by Estimated Proportions of area an uncertainty is tested. 
    
    To carry out it, this function was tested using ground-truth values obtained by 
    Olofsson et al. (2014).
    """
    # image to be processed
    img = rasterio.open('tests/data/LC08_232066_20190727.tif')
    # endmembers
    endm =[[8980,8508,8704,13636,16579,11420], # soil
            [8207,7545,6548,16463,9725,6673], # forest
            [9276,9570,10089,6743,5220,5143], # water
           ]
    endm = np.array(endm)
    # applying the sma function
    frac = sma(image = img, endmembers = endm)
    assert frac.shape[2] == 3
    
def test_pca():
    """Confusion Matrix by Estimated Proportions of area an uncertainty is tested. 
    
    To carry out it, this function was tested using ground-truth values obtained by 
    Olofsson et al. (2014).
    """
    # image to be processed
    img = rasterio.open('tests/data/LC08_232066_20190727.tif')
    # Applying the PCA function:
    arr_pca = PCA(image = img, stand_varb = True)
    img_pca = arr_pca.get('PCA_image')
    assert img_pca.shape[2] == 6

def test_tassCap():
    """Confusion Matrix by Estimated Proportions of area an uncertainty is tested. 
    
    To carry out it, this function was tested using ground-truth values obtained by 
    Olofsson et al. (2014).
    """
    # image to be processed
    img = rasterio.open('tests/data/LC08_232066_20190727.tif')
    # Applying the tassCap function:
    arr_tct = tassCap(image = img, sat = 'Landsat8OLI')
    assert arr_tct.shape[2] == 3

def test_fusionrs():
    """Confusion Matrix by Estimated Proportions of area an uncertainty is tested. 
    
    To carry out it, this function was tested using ground-truth values obtained by 
    Olofsson et al. (2014).
    """
    # image to be processed
    # optical
    optical = rasterio.open('tests/data/LC08_003069_20180906_clip.tif')
    # radar
    radar = rasterio.open('tests/data/S1_2018_VV_VH_clip.tif')
    # Applying the fusionrs function:
    fusion = fusionrs(optical = optical, radar = radar)
    # Cumulative variance (%)
    cum_var = fusion.get('Cumulative_variance')*100
    assert round(cum_var[8],0) == 100

def test_fusionrs():
    """Confusion Matrix by Estimated Proportions of area an uncertainty is tested. 
    
    To carry out it, this function was tested using ground-truth values obtained by 
    Olofsson et al. (2014).
    """
    # image to be processed
    # optical
    optical = rasterio.open('tests/data/LC08_003069_20180906_clip.tif')
    # radar
    radar = rasterio.open('tests/data/S1_2018_VV_VH_clip.tif')
    # Applying the fusionrs function:
    fusion = fusionrs(optical = optical, radar = radar)
    # Cumulative variance (%)
    cum_var = fusion.get('Cumulative_variance')*100
    assert round(cum_var[8],0) == 100

def test_crop():
    """Test that crop all returns a list."""
    # raster to be clipped
    path_raster = "tests/data/LC08_232066_20190727.tif"
    # area of Interes -> shapefile
    path_shp = "tests/data/clip.shp"
    # Path where the image will be saved
    output_path_raster = "tests/data"
    # The raster name
    output_name = 'LC08_232066_20190727_clip'
    # Applying the crop() function:
    crop(image = path_raster, shp = path_shp, 
         filename = output_name, 
         filepath = output_path_raster)
    clip_image = rasterio.open(output_path_raster + '/' + output_name+ '.tif')
    assert type(clip_image) == rasterio.io.DatasetReader
