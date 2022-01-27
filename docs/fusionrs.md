<!-- markdownlint-disable -->

<a href="..\eopy\fusionrs.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `fusionrs`





---

<a href="..\eopy\fusionrs.py#L9"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `fusionrs`

```python
fusionrs(optical, radar, stand_varb=True, nodata=-99999, **kwargs)
```

Fusion of images with different observation geometries through Principal Component Analysis (PCA). 

This algorithm allows to fusion images coming from different spectral sensors  (e.g., optical-optical, optical and SAR, or SAR-SAR). It is also possible to obtain the contribution (%) of each variable in the fused image. 



**Parameters:**
 


 - <b>`optical`</b>:  Optical image. It must be numpy.ndarray with 3d. 


 - <b>`radar`</b>:  Radar image. It must be numpy.ndarray with 3d. 


 - <b>`stand_varb`</b>:  Logical. If ``stand.varb = True``, the PCA is calculated using the correlation   matrix (standardized variables) instead of the covariance matrix   (non-standardized variables).  


 - <b>`nodata`</b>:  The NoData value to replace with -99999. 


 - <b>`**kwargs`</b>:  These will be passed to scikit-learn PCA, please see full lists at: 
 - <b>`https`</b>: //scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html 

Return: numpy.ndarray with 3d. 



**Note:**

> Before executing the function, it is recommended that images coming from different sensors or from the same sensor have a co-registration. 
>References: - Tarazona, Y., Zabala, A., Pons, X., Broquetas, A., Nowosad, J., and Zurqani, H.A. Fusing Landsat and SAR data for mapping tropical deforestation through machine learning classification and the PVts-β non-seasonal detection approach, Canadian Journal of Remote Sensing., vol. 47, no. 5, pp. 677–696, Sep. 2021. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
