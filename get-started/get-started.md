# Get Started

In these lines, a machine learning approach will be used to classify a satellite image. 


# Example

## 1. Applying Machine Learning

Libraries to be used:

```python
import rasterio
import numpy as np
from scikeo.mla import MLA
import matplotlib.pyplot as plt
from dbfread import DBF
import matplotlib as mpl
import pandas as pd
```

## 2.0 Optical image


Landsat-8 OLI (Operational Land Imager) will be used to obtain in order to classify using Random Forest (RF). This image, which is in surface reflectance with bands:
- Blue -> B2
- Green -> B3 
- Red -> B4
- Nir -> B5
- Swir1 -> B6
- Swir2 -> B7

The image and signatures to be used can be downloaded [here](https://drive.google.com/drive/folders/193RhNpACu9THcOZu8OzMh-btnFCOgHrU?usp=sharing):


## 3.0 Supervised Classification using Random Forest

Image and endmembers

```python
path_raster = r"C:\data\ml\LC08_232066_20190727_SR.tif"
img = rasterio.open(path_raster)

path_endm = r"C:\data\ml\endmembers.dbf"
endm = DBF(path_endm)
```

```python
# endmembers
df = pd.DataFrame(iter(endm))
df.head()
```
<p align="left">
  <a href="https://github.com/ytarazona/scikit-eo"><img src="https://raw.githubusercontent.com/ytarazona/scikit-eo/main/docs/images/endembers.png" alt ="header" width = 75%>
</a>
</p>


Instance of ```mla()```:

```python
inst = MLA(image = img, endmembers = endm)
```

Applying Random Forest:

```python
rf_class = inst.SVM(training_split = 0.7)
```

## 4.0 Results

Dictionary of results

```python
rf_class.keys()
```

Overall accuracy

```python
rf_class.get('Overall_Accuracy')
```

Kappa index

```python
rf_class.get('Kappa_Index')
```

Confusion matrix or error matrix

```python
rf_class.get('Confusion_Matrix')
```

<p align="left">
  <a href="https://github.com/ytarazona/scikit-eo"><img src="https://raw.githubusercontent.com/ytarazona/scikit-eo/main/docs/images/confusion_matrix.png" alt ="header" width = 80%>
</a>
</p>


Preparing the image before plotting

```python
# Let's define the color palette
palette = mpl.colors.ListedColormap(["#2232F9","#F922AE","#229954","#7CED5E"])
```

Applying the ```plotRGB()``` algorithm is easy:

```python
# Let´s plot
fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize = (15, 9))

# satellite image
plotRGB(img, title = 'Image in Surface Reflectance', ax = axes[0])

# class results
axes[1].imshow(svm_class.get('Classification_Map'), cmap = palette)
axes[1].set_title("Classification map")
axes[1].grid(False)
```

<p align="left">
  <a href="https://github.com/ytarazona/scikit-eo"><img src="https://raw.githubusercontent.com/ytarazona/scikit-eo/main/docs/images/classification.png" alt ="header" width = "750">
</a>
</p>
