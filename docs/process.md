<!-- markdownlint-disable -->

<a href="..\scikeo\process.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `process`





---

<a href="..\scikeo\process.py#L10"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `crop`

```python
crop(image, shp, filename=None, filepath=None)
```

This algorithm allows to clip a raster (.tif) including a satellite image using a shapefile. 



**Parameters:**
  


 - <b>`image`</b>:  This parameter can be a string with the raster path (e.g., r'/home/image/b3.tif') or it can be a rasterio.io.DatasetReader type. 


 - <b>`shp`</b>:  Vector file, tipically shapefile. 


 - <b>`filename`</b>:  The image name to be saved. 


 - <b>`filepath`</b>:  The path which the image will be stored. 

Return: 

A raster in your filepath. 


---

<a href="..\scikeo\process.py#L110"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `extract`

```python
extract(image, shp)
```

This algorithm allows to extract raster values using a shapefile. 



**Parameters:**
  


 - <b>`image`</b>:  Optical images. It must be rasterio.io.DatasetReader with 3d or 2d. 


 - <b>`shp`</b>:  Vector file, tipically shapefile. 

Return: 

A dataframe with raster values obtained. 



**Note:**

> This function is usually used to extract raster values to be used on machine learning algorithms. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
