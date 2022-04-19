<!-- markdownlint-disable -->

<a href="..\scikit-eo\linearTrend.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `linearTrend`






---

<a href="..\scikit-eo\linearTrend.py#L6"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `linearTrend`
Linear Trend in Remote Sensing 

<a href="..\scikit-eo\linearTrend.py#L10"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(image, nodata=-99999)
```



**Parameters:**
 


 - <b>`image`</b>:  Optical images. It must be rasterio.io.DatasetReader with 3d. 


 - <b>`nodata`</b>:  The NoData value to replace with -99999. 




---

<a href="..\scikit-eo\linearTrend.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `LN`

```python
LN(**kwargs)
```

Linear trend is useful for mapping forest degradation, land degradation, etc. This algorithm is capable of obtaining the slope of an ordinary least-squares  linear regression and its reliability (p-value). 



**Parameters:**
 


 - <b>`**kwargs`</b>:  These will be passed to LN, please see full lists at: 
 - <b>`https`</b>: //docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html 

Return: a dictionary with slope, intercept and p-value obtained. All of them in numpy.ndarray  with 2d. 



References: 
- Crist, E.P., R. Laurin, and R.C. Cicone. 1986. Vegetation and soils information  contained in transformed Thematic Mapper data. Pages 1465-1470 Ref. ESA SP-254.  
 - <b>`European Space Agency, Paris, France. http`</b>: //www.ciesin.org/docs/005-419/005-419.html. 


- Baig, M.H.A., Shuai, T., Tong, Q., 2014. Derivation of a tasseled cap transformation  based on Landsat 8 at-satellite reflectance. Remote Sensing Letters, 5(5), 423-431.  


- Li, B., Ti, C., Zhao, Y., Yan, X., 2016. Estimating Soil Moisture with Landsat Data  and Its Application in Extracting the Spatial Distribution of Winter Flooded Paddies.  Remote Sensing, 8(1), 38. 



**Note:**

> Linear regression is widely used to analyze forest degradation or land degradation. Specifically, the slope and its reliability are used as main parameters and they can be obtained with this function. On the other hand, logistic regression allows obtaining a degradation risk map, in other words, it is a probability map. 
>References: - Tarazona, Y., Maria, Miyasiro-Lopez. (2020). Monitoring tropical forest degradation using remote sensing. Challenges and opportunities in the Madre de Dios region, Peru. Remote Sensing Applications: Society and Environment, 19, 100337. 
>- Wilkinson, G.N., Rogers, C.E., 1973. Symbolic descriptions of factorial models for analysis of variance. Appl. Stat. 22, 392-399. 
>- Chambers, J.M., 1992. Statistical Models in S. CRS Press. 

---

<a href="..\scikit-eo\linearTrend.py#L113"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `MLN`

```python
MLN(**kwargs)
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
