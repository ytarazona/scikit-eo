---
title: 'A Python package for Remote Sensing Tools'
tags:
  - Python
  - Remote Sensing
  - Earth Observation
  - Machine Learning
  - Deep Learning
  - Spatial Analysis
authors:
  - name: Yonatan Tarazona
    orcid: 0000-0002-5208-1004
    affiliation: 1
  - name: Pratyush Tripathy
    affiliation: 2
    orcid: 0000-0000-0000-0000
  - name: Antony Barja
    affiliation: 3
    orcid: 0000-0001-5921-2858
affiliations:
  - name: Pontifical Catholic University of Peru, Polytechnic University of Catalonia, Autonomous University of Barcelona
    index: 1
  - name: Department of Geography, University of California, USA
    index: 2
  - name: Universidad Peruana Cayetano Heredia, Lima, Peru
    index: 3
date: 07 Dec 2022
bibliography: paper.bib
---

<!-- #region -->
# Summary
Nowadays, remotely sensed data has increased dramatically. Microwaves and optical images with different spatial and temporal resolutions are available and are using to monitor a variaty of environmental issues such as deforestation [@Tarazona2018], [@Tarazona2021], land degradation, crop classifications, among other . Although there are efforts (i.e., Python packages, forums, communities, etc.) to make available line-of-code tools for pre-processing, processing and analysis of satellite imagery, there is still a gap that needs to be filled. In other words, too much time is still spent by many users in developing Python lines of code. Algorithms for mapping land degradation through linear trend of vegetation indices (Tarazona and Miyasiro, 2020), fusion optical and radar images to classify vegetation cover, calibration of machine learning lagorithms, among others, are not available yet.

Therefore, **scikit-eo** is a Python package that provides tools for remote sensing. This package was developed to fill the gaps in remotely sensed data processing tools. Most of the tools are based on scientific publications, and others are useful algorithms that will allow processing to be done in a few lines of code. With these tools, the user will be able to invest time in analyzing the results of their data and not spend time on elaborating lines of code, which can sometimes be stressful.

# Highlights



# Audience

**scikit-eo** is intended for students, professionals, researchers, and organizations involved in satellite images processing and analysis. **scikit-eo** puede ser usado para enseñanza universitaria y de posgrado de Teledetección. Determinar 

# Funtionalities


## Main tools

Scikit-eo comes with several algorithms in order to process satelitte images. Atmospheric Correction, Machine Learning (ML), linear trend, combining optical and radar images, among others are some main functions listed below:

| Name of functions  | Description|
| -------------------| --------------------------------------------------------------------------|
| **`mla`**          | Supervised classification in Remote Sensing                               |
| **`calmla`**       | Calibrating supervised classification in Remote Sensing                   |
| **`deepLearning`** | Deep Learning algorithms                                                  |
| **`atmosCorr`**    | Radiometric and atmospheric correction                              |
| **`rkmeans`**      | K-means classification                                                    |
| **`calkmeans`**    | This function allows to calibrate the kmeans algorithm. It is possible to obtain the best k value and the best embedded algorithm in kmeans.                               |
| **`pca`**          | Principal Components Analysis                                             |
| **`linearTrend`**  | Linear trend is useful for mapping forest degradation or land degradation |
| **`fusionrs`**     | This algorithm allows to fusion images coming from different spectral sensors (e.g., optical-optical, optical and SAR or SAR-SAR). Among many of the qualities of this function, it is possible to obtain the contribution (%) of each variable in the fused image |
| **`sma`**          | Spectral Mixture Analysis - Classification sup-pixel                      |
| **`tassCap`**      | The Tasseled-Cap Transformation                                           |

: Main tools available for **scikit-eo** package. \label{table:1}

Of course, some others functions Will be found in the package.
<!-- #endregion -->

## Brief examples

### Example 01

An example of ML will be obtain. For this, Landsat-8 OLI (Operational Land Imager) will be used to classify using the Random Forest (RF) classifier. The datasets to be used in these examples can be downloaded [here](https://drive.google.com/drive/folders/193RhNpACu9THcOZu8OzMh-btnFCOgHrU?usp=sharing):

```python
# 01. Libraries to used in these examples
import rasterio
import numpy as np
from dbfread import DBF
from scikeo.mla import MLA
from scikeo.fusionrs import fusionrs
from scikeo.calmla import calmla
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# 02. Image and endmembers
path_raster = r"C:\data\ml\LC08_232066_20190727_SR.tif"
path_raster = r"F:\RepositoriosGitHub\scikit-eo-tutorials\data\02_ml\LC08_232066_20190727_SR.tif"
img = rasterio.open(path_raster)

path_endm = r"F:\RepositoriosGitHub\scikit-eo-tutorials\data\02_ml\endmembers.dbf"
endm = DBF(path_endm)

# 03. Instance of mla()
inst = MLA(image = img, endmembers = endm)

# 04. Applying RF with 70% of data to train
rf_class = inst.RF(training_split = 0.7)
```

Classification results:

![Original image and Image classified in the left and right panel respectively. \label{fig:AIM}](scikit_eo_00.png){ width=50% }


### Example 02

On the other hand, calibration methods [@Tarazona2021] such as Leave One Out Cross-Validation (LOOCV), Cross-Validation (CV) and Monte Carlos Cross-Validation (MCCV) are embedded in this python package. 
In this second example, MCCV will be used in order to calibrate a supervised classification with different algorithms.

```python
# 01. Endmembers
path_endm = r"C:\data\ml\endmembers.dbf"
endm = DBF(path_endm)

# 02. Instance of calmla()
inst = calmla(endmembers = endm)

# 03. Applying the splitData() method
data = inst.splitData()
```

**Calibrating with *Monte Carlo Cross-Validation Calibration* (MCCV)**

**Parameters**:
- ```split_data```: A instance obtaind with ```splitData()```
- ```models```: Support Vector Machine (svm), Decision Tree (dt), Random Forest (rf) and Naive Bayes (nb)
- ```n_iter```: Number of iterations

```python
# 04. Running MCCV
error_mccv = inst.MCCV(split_data = data, models = ('svm', 'dt', 'rf', 'nb'), n_iter = 10)
```

Calibration results:


![Original image and Image classified in the left and right panel respectively. \label{fig:AIM}](scikit_eo_01.png){ width=50% }


### Example 03




In this example we cover the topic of fusion of images with different observation geometry and that record information in different ranges of the electromagnetic spectrum (Tarazona et al., 2021). The fusion of radar and optical images, although well used to improve land cover mapping, has so far not been developed tools to discuss the contributions of both images in data fusion. In ```scikit-eo``` we developed the function ```fusionrs()``` which provides us with a dictionary with the following image fusion interpretation features:

- *Fused_images*: The fusion of both images into a 3d array
- *Variance*: The variance obtained
- *Proportion_of_variance*: The proportion of the obtained variance
- *Cumulative_variance*: The cumulative variance
- *Correlation*: Correlation of the original bands with the principal components
- *Contributions_in_%*: The contributions of each optical and radar band in the fusion

```python
# 01 
path_optical = "/content/drive/MyDrive/Packages/scikit-eo_data/04_fusionrs/LC08_003069_20180906.tif"
optical = rasterio.open(path_optical)

path_radar = "/content/drive/MyDrive/Packages/scikit-eo_data/04_fusionrs/S1_2018_VV_VH.tif"
radar = rasterio.open(path_radar)

# 02 Applying the fusionrs:
fusion = fusionrs(optical = optical, radar = radar)

# 03 Dictionary of results:
fusion.keys()

# 04 Proportion of variance:
prop_var = fusion.get('Proportion_of_variance')

# 05 Cumulative variance (%):
cum_var = fusion.get('Cumulative_variance')*100

# 06 Showing the proportion of variance and cumulative:
x_labels = ['PC{}'.format(i+1) for i in range(len(prop_var))]

fig, axes = plt.subplots(figsize = (6,5))
ln1 = axes.plot(x_labels, prop_var, marker ='o', markersize = 6,  label = 'Proportion of variance')

axes2 = axes.twinx()
ln2 = axes2.plot(x_labels, cum_var, marker = 'o', color = 'r', label = "Cumulative variance")

ln = ln1 + ln2
labs = [l.get_label() for l in ln]

axes.legend(ln, labs, loc = 'center right')
axes.set_xlabel("Principal Component")
axes.set_ylabel("Proportion of Variance")
axes2.set_ylabel("Cumulative (%)")
axes2.grid(False)
plt.show()
```

![Proportion of Variance and acumulative. \label{fig:AIM}](scikit_eo_02.png){ width=50% }

```python
# 07 Contributions of each variable in %:
fusion.get('Contributions_in_%')
```

![Contributions. \label{fig:AIM}](scikit_eo_03.png){ width=50% }

```python
# 08 Preparing the image:
arr = fusion.get('Fused_images')

def stretch_percentiles(arr):
    p10 = np.percentile(arr, 10) # percentile10
    p90 = np.percentile(arr, 90) # percentile90
    clipped_arr = np.clip(arr, p10, p90)
    img = (clipped_arr - p10)/(p90 - p10)
    return img

arr_fusion = stretch_percentiles(arr)

## Let´s plot
fig, axes = plt.subplots(figsize = (8, 8))
axes.imshow(arr_fusion[:,:,0:3])
axes.set_title("Fusion of optical and radar images")
axes.grid(False)
```

![Fusion of optical and radar images. \label{fig:AIM}](scikit_eo_04.png){ width=50% }

<!-- #region -->
# Acknowledgments

The authors would like to thank to David Montero Loaiza for the idea of the package name and Qiusheng Wu for the suggestions that helped to improve the package.


# References
<!-- #endregion -->
