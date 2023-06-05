<!-- markdownlint-disable -->

# <kbd>module</kbd> `process`





---

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

## <kbd>function</kbd> `extract`

```python
extract(image, shp)
```

This algorithm allows to extract raster values using a shapefile. 



**Parameters:**
  


 - <b>`image`</b>:  Optical images. It must be rasterio.io.DatasetReader with 3d or 2d. 


 - <b>`shp`</b>:  Vector file, typically shapefile. 

Return: 

A dataframe with raster values obtained. 



**Note:**

> This function is usually used to extract raster values to be used on machine learning algorithms. 


---

## <kbd>function</kbd> `confintervalML`

```python
confintervalML(matrix, image_predicted, pixel_size=10, conf=1.96)
```

The error matrix is a simple cross-tabulation of the class labels allocated by the classification of the remotely  sensed data against the reference data for the sample sites. The error matrix organizes the acquired sample data  in a way that summarizes key results and aids the quantification of accuracy and area. The main diagonal of the error  matrix highlights correct classifications while the off-diagonal elements show omission and commission errors.  The cell entries and marginal values of the error matrix are fundamental to both accuracy assessment and area  estimation. The cell entries of the population error matrix and the parameters derived from it must be estimated  from a sample. This function shows how to obtain a confusion matrix by estimated proportions of area with a confidence interval at 95% (1.96). 



**Parameters:**
 


 - <b>`matrix`</b>:  confusion matrix or error matrix in numpy.ndarray.  


 - <b>`image_predicted`</b>:  Array with 2d. This array should be the image classified with classes.  


 - <b>`pixel_size`</b>:  Pixel size of the image classified. By default is 10m of Sentinel-2.  


 - <b>`conf`</b>:  Confidence interval. By default is 95%. 

Return: 

Information of confusion matrix by proportions of area, overall accuracy, user's accuracy with confidence interval  and estimated area with confidence interval as well. 



**Note:**

> Columns and rows in a confusion matrix indicate reference and prediction respectively. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
