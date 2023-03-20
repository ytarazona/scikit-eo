# -*- coding: utf-8 -*-
# +
import os
import copy
import fiona
import rasterio
import rasterio.mask
import numpy as np
import pandas as pd
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
    
    gdf['values'] = [x for x in image.sample(coords)]
    
    bands_total = gdf['values'][0].shape[0]
    
    col_names = [f'band{i}' for i in range(1, bands_total + 1)]
    
    df = pd.DataFrame(gdf["values"].to_list(), columns = col_names)
    
    join_df = pd.concat([shp.iloc[:,0], df], axis = 1, join = 'inner')

    if join_df.isnull().values.any():
        raise TypeError('DataFrame contains nan values. Check it out')
        
    return join_df


def confintervalML(matrix, image_predicted, pixel_size = 10, conf = 1.96):
    
    '''The error matrix is a simple cross-tabulation of the class labels allocated by the classification of the remotely 
    sensed data against the reference data for the sample sites. The error matrix organizes the acquired sample data 
    in a way that summarizes key results and aids the quantification of accuracy and area. The main diagonal of the error 
    matrix highlights correct classifications while the off-diagonal elements show omission and commission errors. 
    The cell entries and marginal values of the error matrix are fundamental to both accuracy assessment and area 
    estimation. The cell entries of the population error matrix and the parameters derived from it must be estimated 
    from a sample. This function shows how to obtain a confusion matrix by estimated proportions of area with a confidence
    interval at 95% (1.96).
        
    This function supports DataFrame (as a confusion matrix) and an image classified in array as input.
     
        
        Parameters:
    
            matrix: confusion matrix or error matrix in DataFrame
            
            image_predicted: Array with 2d. This array should be the image classified with classes.
            
            pixel_size: Pixel size of the image classified. By default is 10m of Sentinel-2.
            
            conf: Confidence interval. By default is 95%.
    
        Return:
        
            Information of confusion matrix by proportions of area, user's accuracy with confidence interval and 
            estimated area with confidence interval as well.
    '''
    
    matConf = matrix.drop(['Total','Producer_Accuracy','Omission'], axis = 0)
    
    # classes
    iclass = matConf.index.to_numpy().astype(int)
    
    # ni
    ni = matConf['Total'].to_numpy()
    
    matConf = matConf.drop(['Total','Users_Accuracy','Commission'], axis = 1).to_numpy()
    
    # number of classes
    n = matConf.shape[0]
    
    pixels = []
    
    for i in iclass:
        pixels.append((image_predicted == i).sum()) #((30**2)/10000) # ha    
    
    wi = (np.array([pixels])/np.array([pixels]).sum()).flatten()
    
    pixels = np.array(pixels)
    
    for i in range(n):
        matConf[i,:] = (matConf[i,:]/ni[i])*wi[i]
    
    # user's accuracy
    ua = np.diag(matConf)/np.sum(matConf, axis = 1)
    
    # total Wi
    total_wi = np.sum(matConf, axis = 1)
    
    # copy the matrix of proportions
    mat_conf = matConf.copy()
    # building the matrix of proportion area
    mat_conf = np.concatenate([mat_conf, total_wi.reshape(n, 1)], axis = 1)
    mat_conf = np.concatenate([mat_conf, pixels.reshape(n, 1)], axis = 1)
    # total Wi in rows
    total = np.sum(mat_conf, axis = 0)
    # final matrix
    mat_conf = np.concatenate([mat_conf, total.reshape(1, n+2)], axis = 0)
    
    namesCol = []
    for i in np.arange(1, n + 1): namesCol.append(str(i))
    namesCol.extend(['Total[Wi]', 'Area[pixels]'])

    namesRow = []
    for i in np.arange(1, n + 1): namesRow.append(str(i))
    namesRow.extend(['Total'])

    # error matrix (DataFrame) in proportions of area
    cm_prop_area = pd.DataFrame(np.round(mat_conf, 4), columns = namesCol, index = namesRow)
    
    # confidence interval for Overall accuracy at 95% 1.96
    conf_int_oa = list(map(lambda Wi, UA, Ni: (Wi)**2*UA*(1-UA)/(Ni-1), wi, ua, ni))
    conf_int_oa = conf*(np.array(conf_int_oa).sum())
        
    # confidence interval for user's accuracy at 95% 1.96
    conf_int_ua = conf*np.array(list(map(lambda UA, Ni: UA*(1-UA)/(Ni-1), ua, ni)))
    
    # confidence interval for the area at 95%
    sp = []
    for i in np.arange(n):
        s_pi = list(map(lambda Wi, Pik, Ni: (Wi*Pik - Pik**2)/(Ni-1), wi, matConf[:,i], ni))
        s_pi = np.sqrt(np.array(s_pi).sum())
        sp.append(s_pi)
    
    # S(A)=1.96*s(p)*A(total) in ha
    SA = conf*np.array(sp)*(np.array(pixels).sum())*(pixel_size**2/10000)
    
    # Area total estimated
    A = total[0:n]*(np.array(pixels).sum())*(pixel_size**2/10000)
    
    # print info
    def print_info(matrixCEA, a, b, c, d):
        print('***** Confusion Matrix by Estimated Proportions of area *****')
        print('')
        print('Overall accuracy')
        print(conf_int_oa)
        print('')
        print('Confusion matrix')
        print(matrixCEA)
        print('')
        print('User´s accuracy at 95%')
        for i in range(b.shape[0]):
            print(f'{iclass[i]}: {a[i]:.4f} ± {b[i]:.4f}')
        print('')
        print('Estimating area (Ha) and uncertainty at 95%')
        for i in range(b.shape[0]):
            print(f'{iclass[i]}: {c[i]:.4f} ± {d[i]:.4f}')
            
        
    return print_info(cm_prop_area, 
                      ua, 
                      conf_int_ua, 
                      A, 
                      SA)
