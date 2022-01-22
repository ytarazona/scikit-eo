# -*- coding: utf-8 -*-
import numpy as np
import rasterio
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# +
import numpy as np
import pandas as pd
import rasterio
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def fusionrs(optical, radar, stand_varb = True, **kwargs):
    
    '''
    Fusion of images with different observation geometries through Principal Component Analysis (PCA).
    
    This algorithm allows to fusion images coming from different spectral sensors 
    (e.g., optical-optical, optical and SAR, or SAR-SAR). It is also possible to obtain the contribution (%) of each variable
    in the fused image.
    
    Parameters:
    
        optical: Optical image. It must be numpy.ndarray with 3d.
        
        radar: Radar image. It must be numpy.ndarray with 3d.
        
        stand_varb: Logical. If ``stand.varb = True``, the PCA is calculated using the correlation 
                    matrix (standardized variables) instead of the covariance matrix 
                    (non-standardized variables).
        nan: Logical. If ``na.rm = True`` the NaN values of the images will be omitted from 
               the analysis
    
    Return:
        numpy.ndarray with 3d.
    
    Note:
    Before executing the function, it is recommended that images coming from different sensors 
    or from the same sensor have a co-registration.

    References:
    - Tarazona, Y., Zabala, A., Pons, X., Broquetas, A., Nowosad, J., and Zurqani, H.A. 
      Fusing Landsat and SAR data for mapping tropical deforestation through machine learning 
      classification and the PVts-β non-seasonal detection approach, Canadian Journal of Remote 
      Sensing., vol. 47, no. 5, pp. 677–696, Sep. 2021.
    
    '''
    
    for args in [optical, radar]:
        if not isinstance(args, (rasterio.io.DatasetReader)): 
            raise TypeError('The arguments A and B must be rasterio.io.DatasetReader.')
    
    if not optical.width != radar.width and optical.height != radar.height:
        raise ValueError('Both optical and radar must have the same dimensions in rows and cols.')
        
    bands_total = optical.count + radar.count
        
    rows = optical.height
        
    cols = optical.width
        
    opt = optical.read(); opt = np.moveaxis(opt, 0, -1)
    
    rad = radar.read(); rad = np.moveaxis(rad, 0, -1)
    
    # stack both images
    st = np.dstack([opt, rad])
    
    # data in [rows*cols, bands]
    arr = st.reshape((rows*cols, bands_total))
    
    # standardized variables
    if stand_varb:
        arr = StandardScaler().fit_transform(arr)
    
    inst_pca = PCA(**kwargs)
    
    fit_pca = inst_pca.fit(arr)
    
    pC = fit_pca.transform(arr)
    
    # fused images
    pc = pC.reshape((rows, cols, bands_total))
    
    # variance
    var = fit_pca.explained_variance_
    
    # Proportion variance
    pro_var = fit_pca.explained_variance_ratio_
    
    # Cumulative variance
    cum_var = np.array([np.sum(fit_pca.explained_variance_ratio_[:i]) for i in range(1, bands_total + 1)])
    
    # Correlation between original variables and pc
    df_ori = pd.DataFrame(arr, 
                          columns = [f'var{i}' for i in range(1, bands_total + 1)])
    df_pca = pd.DataFrame(pC, 
                          columns = [f'pc{j}' for j in range(1, bands_total + 1)])
    
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
