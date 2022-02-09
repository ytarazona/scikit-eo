# -*- coding: utf-8 -*-
# +
import numpy as np
import pandas as pd
import rasterio
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def PCA(image, stand_varb = True, nodata = -99999, **kwargs):
    
    '''
    Runing Principal Component Analysis (PCA) with satellite images.
    
    This algorithm allows to obtain Principal Components from images either radar or optical
    coming from different spectral sensors. It is also possible to obtain the contribution (%) 
    of each variable.
    
    Parameters:
    
        images: Optical or radar image, it must be rasterio.io.DatasetReader with 3d.
        
        stand_varb: Logical. If ``stand.varb = True``, the PCA is calculated using the correlation 
                    matrix (standardized variables) instead of the covariance matrix 
                    (non-standardized variables).
                    
        nodata: The NoData value to replace with -99999.
        
        **kwargs: These will be passed to scikit-learn PCA, please see full lists at:
                  https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
    
    Return:
        numpy.ndarray with 3d.
    
    
    '''
    
    if not isinstance(image, (rasterio.io.DatasetReader)): 
            raise TypeError('The "image" must be rasterio.io.DatasetReader.')
        
    bands = image.count
        
    rows = image.height
        
    cols = image.width
        
    st = image.read()
    
    st_reorder = np.moveaxis(opt, 0, -1)
    
    # data in [rows*cols, bands]
    arr = st_reorder.reshape((rows*cols, bands))
    
    # nodata
    if np.isnan(np.sum(arr)):
        arr[np.isnan(arr)] = self.nodata
    
    # standardized variables
    if stand_varb:
        arr = StandardScaler().fit_transform(arr)
    
    inst_pca = PCA(**kwargs)
    
    fit_pca = inst_pca.fit(arr)
    
    pC = fit_pca.transform(arr)
    
    # fused images
    pc = pC.reshape((rows, cols, bands))
    
    # variance
    var = fit_pca.explained_variance_
    
    # Proportion variance
    pro_var = fit_pca.explained_variance_ratio_
    
    # Cumulative variance
    cum_var = np.array([np.sum(fit_pca.explained_variance_ratio_[:i]) for i in range(1, bands + 1)])
    
    # Correlation between original variables and pc
    df_ori = pd.DataFrame(arr, 
                          columns = [f'var{i}' for i in range(1, bands + 1)])
    df_pca = pd.DataFrame(pC, 
                          columns = [f'pc{j}' for j in range(1, bands + 1)])
    
    def corr(data_frame_1, data_frame_2):
        
        '''This function allows to obtain correlation between two dataFrames'''
        
        v1, v2 = data_frame_1.values, data_frame_2.values
        
        sums = np.multiply.outer(v2.sum(0), v1.sum(0))
        
        stds = np.multiply.outer(v2.std(0), v1.std(0))
        
        return pd.DataFrame((v2.T.dot(v1) - sums/len(data_frame_1))/stds/len(data_frame_1), 
                            data_frame_2.columns, 
                            data_frame_1.columns)

    corr_mat = corr(df_ori, df_pca).T
    
    results = {'Fused_images':pc,
              'Variance':var,
              'Proportion_of_variance':pro_var,
              'Cumulative_variance':cum_var,
              'Correlation':corr_mat
              #'Contribution_in_%':
             }

    return results
