# -*- coding: utf-8 -*-
# +
import fiona
import rasterio
import rasterio.mask
import numpy as np
import os

def crop(image, shp, filename = None, filepath = None):
    
    '''
    This algorithm allows to clip a raster (.tif) including a satellite image using a shapefile.
    
    Parameters:
        
        image: This parameter can be a string with the raster path (e.g., '/home/image/b3.tif') or
        it can be a rasterio.io.DatasetReader type.
        
        shp: vector file, tipically shapefile.
        
        filename: The image name to be saved.
        
        filepath: The path which the image will be stored.
        
    Return:
    
        A raster in your filepath.
    '''
        
    if isinstance(image, (str)):
        
        image = image.replace(os.sep, '/')
    
        shp = shp.replace(os.sep, '/')
        
        if filename is None:
        
            filename = 'raster'
    
        if filepath is None:
        
            current_path = os.getcwd()
        
            path = current_path.replace(os.sep, '/') + '/' + filename + '.tif'
        
        else:
            path = filepath.replace(os.sep, '/') + '/' + filename + '.tif'
    
        path_name = path
    
        # read Shapefile
        with fiona.open(shp, "r") as shapefile:
            shapes = [feature["geometry"] for feature in shapefile]

        # read image
        with rasterio.open(image) as src:
            out_image, out_transform = rasterio.mask.mask(src, shapes, crop = True)
            out_meta = src.meta

        # save clipped image
        out_meta.update({"driver": "GTiff",
                         "height": out_image.shape[1],
                         "width": out_image.shape[2],
                         "transform": out_transform})

        with rasterio.open(path_name, "w", **out_meta) as dest:
            dest.write(out_image)
    
    elif isinstance(image, (rasterio.io.DatasetReader)):
    
        shp = shp.replace(os.sep, '/')
        
        if filename is None:
        
            filename = 'raster'
    
        if filepath is None:
        
            current_path = os.getcwd()
        
            path = current_path.replace(os.sep, '/') + '/' + filename + '.tif'
        
        else:
            path = filepath.replace(os.sep, '/') + '/' + filename + '.tif'
    
        path_name = path
    
        # read Shape file
        with fiona.open(shp, "r") as shapefile:
            shapes = [feature["geometry"] for feature in shapefile]

        # read image
        out_image, out_transform = rasterio.mask.mask(image, shapes, crop = True)
        out_meta = image.meta

        # save clipped image
        out_meta.update({"driver": "GTiff",
                         "height": out_image.shape[1],
                         "width": out_image.shape[2],
                         "transform": out_transform})

        with rasterio.open(path_name, "w", **out_meta) as dest:
            dest.write(out_image)
        
    else:
        raise TypeError(f'"image" must be a string like /home/image/b5.tif or must be rasterio.io.DatasetReader. image = {type(image)}')
