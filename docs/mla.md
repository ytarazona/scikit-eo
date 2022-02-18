<!-- markdownlint-disable -->

<a href="..\eopy\mla.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `mla`






---

<a href="..\eopy\mla.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `mla`
Supervised and unsupervised classification in Remote Sensing 

<a href="..\eopy\mla.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(image, endmembers, nodata=-99999)
```

Parameter: 

 image: Optical images. It must be rasterio.io.DatasetReader with 3d.  

 endmembers: Endmembers must be a matrix (numpy.ndarray) and with more than one endmember.   Rows represent the endmembers and columns represent the spectral bands.  The number of bands must be equal to the number of endmembers.  E.g. an image with 6 bands, endmembers dimension should be $n*6$, where $n$   is rows with the number of endmembers and 6 is the number of bands   (should be equal).  In addition, Endmembers must have a field (type int or float) with the names   of classes to be predicted.  

 nodata: The NoData value to replace with -99999. 




---

<a href="..\eopy\mla.py#L205"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `DT`

```python
DT(training_split=0.8, random_state=None, **kwargs)
```

The Support Vector Machine (SVM) classifier is a supervised non-parametric statistical learning technique that  does not assume a preliminary distribution of input data. Its discrimination criterion is a  hyperplane that separates the classes in the multidimensional space in which the samples  that have established the same classes are located, generally some training areas. 

SVM support raster data read by rasterio (rasterio.io.DatasetReader) as input. 





**Parameters:**
 


 - <b>`training_split`</b>:  For splitting samples into two subsets, i.e. training data and for testing  data. 


 - <b>`kernel `</b>:  {'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'}, default='rbf' Specifies   the kernel type to be used in the algorithm. It must be one of 'linear', 'poly',   'rbf', 'sigmoid', 'precomputed' or a callable. If None is given, 'rbf' will  
 - <b>`be used. See https`</b>: //scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC for more details. 


 - <b>`**kwargs`</b>:  These will be passed to SVM, please see full lists at: 
 - <b>`https`</b>: //scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC 

Return: 

Labels of classification as numpy object. 

---

<a href="..\eopy\mla.py#L425"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `NB`

```python
NB(training_split=0.8, random_state=None, **kwargs)
```

The Support Vector Machine (SVM) classifier is a supervised non-parametric statistical learning technique that  does not assume a preliminary distribution of input data. Its discrimination criterion is a  hyperplane that separates the classes in the multidimensional space in which the samples  that have established the same classes are located, generally some training areas. 

SVM support raster data read by rasterio (rasterio.io.DatasetReader) as input. 





**Parameters:**
 


 - <b>`training_split`</b>:  For splitting samples into two subsets, i.e. training data and for testing  data. 


 - <b>`kernel `</b>:  {'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'}, default='rbf' Specifies   the kernel type to be used in the algorithm. It must be one of 'linear', 'poly',   'rbf', 'sigmoid', 'precomputed' or a callable. If None is given, 'rbf' will  
 - <b>`be used. See https`</b>: //scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC for more details. 


 - <b>`**kwargs`</b>:  These will be passed to SVM, please see full lists at: 
 - <b>`https`</b>: //scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC 

Return: 

Labels of classification as numpy object. 

---

<a href="..\eopy\mla.py#L535"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `NN`

```python
NN(training_split=0.8, max_iter=300, random_state=None, **kwargs)
```

The Support Vector Machine (SVM) classifier is a supervised non-parametric statistical learning technique that  does not assume a preliminary distribution of input data. Its discrimination criterion is a  hyperplane that separates the classes in the multidimensional space in which the samples  that have established the same classes are located, generally some training areas. 

SVM support raster data read by rasterio (rasterio.io.DatasetReader) as input. 





**Parameters:**
 


 - <b>`training_split`</b>:  For splitting samples into two subsets, i.e. training data and for testing  data. 


 - <b>`kernel `</b>:  {'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'}, default='rbf' Specifies   the kernel type to be used in the algorithm. It must be one of 'linear', 'poly',   'rbf', 'sigmoid', 'precomputed' or a callable. If None is given, 'rbf' will  
 - <b>`be used. See https`</b>: //scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC for more details. 


 - <b>`**kwargs`</b>:  These will be passed to SVM, please see full lists at: 
 - <b>`https`</b>: //scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC 

Return: 

Labels of classification as numpy object. 

---

<a href="..\eopy\mla.py#L315"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `RF`

```python
RF(training_split=0.8, random_state=None, **kwargs)
```

The Support Vector Machine (SVM) classifier is a supervised non-parametric statistical learning technique that  does not assume a preliminary distribution of input data. Its discrimination criterion is a  hyperplane that separates the classes in the multidimensional space in which the samples  that have established the same classes are located, generally some training areas. 

SVM support raster data read by rasterio (rasterio.io.DatasetReader) as input. 





**Parameters:**
 


 - <b>`training_split`</b>:  For splitting samples into two subsets, i.e. training data and for testing  data. 


 - <b>`kernel `</b>:  {'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'}, default='rbf' Specifies   the kernel type to be used in the algorithm. It must be one of 'linear', 'poly',   'rbf', 'sigmoid', 'precomputed' or a callable. If None is given, 'rbf' will  
 - <b>`be used. See https`</b>: //scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC for more details. 


 - <b>`**kwargs`</b>:  These will be passed to SVM, please see full lists at: 
 - <b>`https`</b>: //scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC 

Return: 

Labels of classification as numpy object. 

---

<a href="..\eopy\mla.py#L95"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `SVM`

```python
SVM(training_split=0.8, random_state=None, kernel='linear', **kwargs)
```

The Support Vector Machine (SVM) classifier is a supervised non-parametric statistical learning technique that  does not assume a preliminary distribution of input data. Its discrimination criterion is a  hyperplane that separates the classes in the multidimensional space in which the samples  that have established the same classes are located, generally some training areas. 

SVM support raster data read by rasterio (rasterio.io.DatasetReader) as input. 





**Parameters:**
 


 - <b>`training_split`</b>:  For splitting samples into two subsets, i.e. training data and for testing  data. 


 - <b>`kernel `</b>:  {'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'}, default='rbf' Specifies   the kernel type to be used in the algorithm. It must be one of 'linear', 'poly',   'rbf', 'sigmoid', 'precomputed' or a callable. If None is given, 'rbf' will  
 - <b>`be used. See https`</b>: //scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC for more details. 


 - <b>`**kwargs`</b>:  These will be passed to SVM, please see full lists at: 
 - <b>`https`</b>: //scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC 

Return: 

Labels of classification as numpy object. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
