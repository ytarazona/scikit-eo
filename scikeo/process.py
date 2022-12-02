# -*- coding: utf-8 -*-
# +
import os
import fiona
import rasterio
import rasterio.mask
import numpy as np
import geopandas as gpd

def crop(image, shp, filename = None, filepath = None):
    
    '''
    This algorithm allows to clip a raster (.tif) including a satellite image using a shapefile.
    
    Parameters:
        
        image: This parameter can be a string with the raster path (e.g., r'/home/image/b3.tif') or
        it can be a rasterio.io.DatasetReader type.
        
        shp: Vector file, tipically shapefile.
        
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
        raise TypeError(f'"image" must be a string like r"/home/image/b5.tif" or must be rasterio.io.DatasetReader. image = {type(image)}')

        
def extract(image, shp):
    
    '''
    This algorithm allows to extract raster values using a shapefile.
    
    Parameters:
        
        image: Optical images. It must be rasterio.io.DatasetReader with 3d or 2d.
        
        shp: Vector file, tipically shapefile.
        
    Return:
    
        A dataframe with raster values obtained.
        
    Note:
        This function is usually used to extract raster values to be used on machine 
        learning algorithms.
    '''
    
    if not isinstance(image, (rasterio.io.DatasetReader)):
        raise TypeError('"image" must be raster read by rasterio.open().')
    
    if not isinstance(shp, (gpd.geodataframe.GeoDataFrame)):
        raise TypeError('"shp" must be Shapefile (.shp)')
    
    gdf = gpd.GeoDataFrame(geometry = shp['geometry'])
    
    coords = [(x,y) for x, y in zip(gdf['geometry'].x, gdf['geometry'].y)]
    
    gdf['values'] = [x for x in img.sample(coords)]
    
    bands_total = gdf['values'][0].shape[0]
    
    col_names = [f'band{i}' for i in range(1, bands_total + 1)]
    
    df = pd.DataFrame(gdf["values"].to_list(), columns = col_names)
    
    join_df = pd.concat([shp.iloc[:,0], df], axis = 1, join = 'inner')

    if join_df.isnull().values.any():
        raise TypeError('DataFrame contains nan values. Check it out')
        
    return join_df
