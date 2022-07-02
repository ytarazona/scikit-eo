<!-- #region -->
# scikit-eo

[![License: MIT](https://img.shields.io/badge/licence-MIT-blue)](https://opensource.org/licenses/MIT)
[![PythonVersion]( https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7%20%7C%203.8-green)]()
[![image](https://img.shields.io/pypi/v/eopy.svg)](https://pypi.python.org/pypi/scikit-eo)

<p align="center">
  <a href="https://github.com/ytarazona/scikit-eo"><img src="https://raw.githubusercontent.com/ytarazona/scikit-eo/main/docs/images/scikit-eo_logo.jpg" align="right" width="220"></a>
</p>

<!-- #region -->
# Introduction

**scikit-eo** is a Python package that provides tools for remote sensing. This package was developed to fill the gaps in remotely sensed data processing tools. Most of the tools are based on scientific publications, and others are useful algorithms that will allow processing to be done in a few lines of code. With these tools, the user will be able to invest time in analyzing the results of their data and not spend time on elaborating lines of code, which can sometimes be stressful.

**scikit-eo** is intended for students, professionals, researchers, and organizations involved in satellite images processing and analysis.

Some available functions in this version:

| Name of functions  | Description|
| -------------------| --------------------------------------------------------------------------|
| **`mla`**          | Machine Learning                                                          |
| **`calmla`**       | Calibrating supervised classification in Remote Sensing                   |
| **`rkmeans`**      | K-means classification                                                    |
| **`calkmeans`**    | This function allows to calibrate the kmeans algorithm. It is possible to obtain the best k value and the best embedded algorithm in kmeans.                               |
| **`pca`**          | Principal Components Analysis                                             |
| **`atmosCorr`**    | Atmospheric Correction of satellite imagery                               |
| **`deepLearning`** | Deep Learning algorithms                                                  |
| **`linearTrend`**  | Linear trend is useful for mapping forest degradation or land degradation |
| **`fusionrs`**     | This algorithm allows to fusion images coming from different spectral sensors (e.g., optical-optical, optical and SAR or SAR-SAR). Among many of the qualities of this function, it is possible to obtain the contribution (%) of each variable in the fused image |
| **`sma`**          | Spectral Mixture Analysis - Classification sup-pixel                      |
| **`tassCap`**      | The Tasseled-Cap Transformation                                           |

You will find more algorithms!.


# Installation

To use **scikit-eo** it is necessary to install it. There are two options:

## 1. From PyPI

It is not available yet.

## 2. Installing from source

It is also possible to install the latest development version directly from the GitHub repository with:
<!-- #endregion -->

```python
pip install git+https://github.com/ytarazona/scikit-eo
```

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
path_raster = r"F:\RepositoriosGitHub\scikit-eo-tutorials\data\02_ml\LC08_232066_20190727_SR.tif"
img = rasterio.open(path_raster)

path_endm = r"F:\RepositoriosGitHub\scikit-eo-tutorials\data\02_ml\endmembers.dbf"
endm = DBF(path_endm)
```

```python
# endmembers
df = pd.DataFrame(iter(endm))
df.head()
```

<img src="https://raw.githubusercontent.com/ytarazona/scikit-eo/main/docs/images/endembers.png" width = 70%/ align="left">



<!-- #region -->


Instance of ```mla()```:
<!-- #endregion -->

```python
inst = MLA(image = img, endmembers = endm)
```

Applying Random Forest:

```python
import warnings 
warnings.filterwarnings("ignore")

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

<p align="center">
  <a href="https://github.com/ytarazona/scikit-eo"><img src="https://raw.githubusercontent.com/ytarazona/scikit-eo/main/docs/images/confusion_matrix.png" align="left" width="580"></a>
</p>


Preparing the image before plotting

```python
# convert to array
arr_img = img.read()
# stacking the image
rgb = np.stack([arr_img[4,:,:], arr_img[3,:,:], arr_img[2,:,:]], axis = -1)

# Normalizing bands
def stretch_std(arr, std_val):
    """ Returns the data with a standard deviation contrast applied """
    mean = np.mean(arr)
    std = np.std(arr)*std_val
    min_val = np.max([mean - std, np.min(arr)])
    max_val = np.min([mean + std, np.max(arr)])
    clipped_arr = np.clip(arr, min_val, max_val)
    img = (clipped_arr - min_val)/(max_val - min_val)
    return img

rgb_norm = stretch_std(rgb, 2.5)
```

```python
# Let's define the color palette
palette = mpl.colors.ListedColormap(["#2232F9","#F922AE","#229954","#7CED5E"])

# Let´s plot
fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize = (15, 9))
axes[0].imshow(rgb_norm)
axes[0].set_title("Image in Surface Reflectance")
axes[0].grid(False)

axes[1].imshow(rf_class.get('Classification_Map'), cmap = palette)
axes[1].set_title("Classification Map")
axes[1].grid(False)
```

<p align="center">
  <a href="https://github.com/ytarazona/scikit-eo"><img src="https://raw.githubusercontent.com/ytarazona/scikit-eo/main/docs/images/classification.png" align="left" width="700"></a>
</p>


-   Free software: Apache Software License 2.0
-   Documentation: <https://ytarazona.github.io/scikit-eo>

## Credits

This package was created with [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
