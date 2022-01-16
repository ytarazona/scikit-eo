# +
from sklearn.cluster import KMeans
import rasterio
import numpy as np

def rkmeans(image, **kwargs):
    
    '''The Support Vector Machine (SVM) classifier is a supervised non-parametric statistical learning technique that 
        does not assume a preliminary distribution of input data. Its discrimination criterion is a 
        hyperplane that separates the classes in the multidimensional space in which the samples 
        that have established the same classes are located, generally some training areas.
        
        SVM support raster data read by rasterio (rasterio.io.DatasetReader) as input.
        
        
        Parameters:
            
            image: Optical images. It must be rasterio.io.DatasetReader with 3d.
    
            training_split: For splitting samples into two subsets, i.e. training data and for testing
                            data.
    
            kernel : {'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'}, default='rbf' Specifies 
                     the kernel type to be used in the algorithm. It must be one of 'linear', 'poly', 
                     'rbf', 'sigmoid', 'precomputed' or a callable. If None is given, 'rbf' will 
                     be used. See https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC
                     for more details.
                     
            **kwargs: These will be passed to SVM, please see full lists at:
                  https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC
    
        Return:
        
            Labels of classification as numpy object.
    '''
    
    if not isinstance(image, (rasterio.io.DatasetReader)):
        raise TypeError('"image" must be raster read by rasterio.open().')
        
    bands = image.count
        
    rows = image.height
        
    cols = image.width
        
    # stack images
    #l = []
    #for i in np.arange(1, bands+1): l.append(image.read(int(i)))
    #st = np.stack(l)
    st = image.read()
    
    # data in [rows, cols, bands]
    st_reorder = np.moveaxis(st, 0, -1) 
    # data in [rows*cols, bands]
    arr = st_reorder.reshape(rows*cols, bands)
    
    kmeans = KMeans(**kwargs) # max_iter=300 (por defecto)
    kmeans.fit(arr)
    
    labels_km = kmeans.labels_
    classKM = labels_km.reshape((rows, cols))
    
    return classKM
        
