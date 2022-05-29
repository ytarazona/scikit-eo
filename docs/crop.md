<!-- markdownlint-disable -->

<a href="..\scikeo\crop.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `crop`





---

<a href="..\scikeo\crop.py#L9"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `crop`

```python
crop(image, shp, filename=None, filepath=None)
```

This algorithm allows to clip a raster (.tif) including a satellite image using a shapefile. 



**Parameters:**
  


 - <b>`image`</b>:  This parameter can be a string with the raster path (e.g., r'/home/image/b3.tif') or it can be a rasterio.io.DatasetReader type. 


 - <b>`shp`</b>:  vector file, tipically shapefile. 


 - <b>`filename`</b>:  The image name to be saved. 


 - <b>`filepath`</b>:  The path which the image will be stored. 

Return: 

A raster in your filepath. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
