---
title: 'scikit-eo: A Python package for Remote Sensing Data Analysis'
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
  - name: Jakub Nowosad
    affiliation: 2
    orcid: 0000-0002-1057-3721
affiliations:
  - name: Pontifical Catholic University of Peru
    index: 1
  - name: Adam Mickiewicz University in Poznan
    index: 2
date: 19 May 2023
bibliography: paper.bib
---
<!-- #TODO -->

1. Fix the data paths and make a folder to refer a sample data for testing and review.
3. Finish the writing - Add examples related to data fusion and RS Trends.
4. Link Documentation 

<!-- #region -->
# Summary & Propose

Remote sensing and, more importantly, the growing accessibility of remotely sensed data, has fundamentally transformed our capacity to comprehend, classify, and monitor the connected environmental conditions of our planet. This enhanced understanding has enables researchers to address and tackle a broader range of challenges effectively, by using novel tools and data at multiple scales that help to shed new light into the underlying factors that contribute to both local and global issues. 

As more accessible the data is, the bigger the need is for open-source tools to read, process and execute analysis that contribute to underpin patterns, changes and trends that are critical for environmental studies. Applications that integrate spatial-temporal data are currently used for several purposes, such as monitoring and assessment land cover changes [@Liping2018], deforestation [@Blanc2016], impact on urbanization level [@Trinder2020], climate change impacts [@Yang2013], water quality [@Wang2019], air pollution [@Seham2022], biodiversity conservation [@Jeannine2022], and natural disaster management [@Kucharczyk2021], to name a few. By collecting data over large periods of time researchers can identify or measure the impact of human activities on ecosystems and support the data-driven decision-making process for more sustainable resource management [@Jensen2000].

But more availability of data, does not necessary more easy ways to process the data. Analysts spend an important among of time time finding the correct libraries that allow them to read and process the data.  Tools for mapping land degradation through linear trend of vegetation indices [@TARAZONA2018367], [@Tarazona2022], data fusion process for optical and radar images to quickly classify the vegetation cover, and the integration of machine learning techniques are still separate in multiple libraries, along with diffuse documentation that limits the analysis where the main concerns of the causes or patterns of the environmental conditions should be the main focus.

Therefore, **scikit-eo** is a Python package that provides the necessary tools for remote sensing analysis. It is a centralized, scalable and open source toolkit, developed to fill the gaps in remotely sensed data processing tools. This toolkit can be use in multiple venues from a lecturer room as a toolkit for introduction of programming skills using python and remote sensing for environmental studies, or can be use as part of any Python setting in a research project. The majority of the tools including in **scikit-eo** are derived from scientific publications, while others are valuable algorithms that streamline data processing into just a few lines of code. By integrating this set of diverse tools, users can focus their time and energy on analyzing the results of their data, rather than getting bogged down in the intricacies lines of code. By centralizing, integrating use cases and example of data, **scikit-eo** serves as a way to allow researchers to optimize their resources and dedicate their focus to the meaningful interpretation of their findings with greater efficiency, rather to stress out with coding task. 

# Highlights

<!-- NEEDS TO GET UPDATED-->
**scikit-eo** is a toolkit that provides a variety of remote sensing tools. Initially users can start with one of the most popular and yet useful techniques like Principal Components Analysis - PCA, then is the land cover characterization by using deep learning algorithms to obtain the confusion matrix and metrics such as user's accuracy, producer's accuracy, omissions and commissions. This metrics combination can be obtained with **scikit-eo** on a pandas ```DataFrame``` object. On the other hand, a predicted classes map, i.e., a land cover map which represents the output of the classification algorithm (machine learning) or the output of the segmentation algorithm (deep learning), must be accompanied by its uncertainties with a confidence interval ($95$% or $90$%), and additionally, any metric obtained from the confusion matrix must be represented with a confidence level as well. All these metrics can be obtained with **scikit-eo**. Other useful tools for remote sensing can be found in this python package.

# Audience

**scikit-eo** is intended for students, professionals, researchers, and organizations involved in satellite image processing and analysis. **scikit-eo** can be used for university teaching, lectures, research and so on.

## **scikit-eo** as Research tool:
advance techniques for research proposes. 
## **scikit-eo** in the lecture room:
Simple methods for intro and RS practice, as well programming skills
## **scikit-eo** as open source tool:
Scalable, open and well documented tool.

# Functionalities


## Main tools

**Scikit-eo** comes with several algorithms to process satellite images in order to study different environmental issues. Atmospheric correction, machine learning and deep learning, estimating area and uncertainty, linear trend, combining optical and radar images, among others, are some main functions listed below:

| Name of functions  | Description|
| -------------------| --------------------------------------------------------------------------|
| **`mla`**          | Supervised Classification in Remote Sensing                               |
| **`calmla`**       | Calibrating Supervised Classification in Remote Sensing                   |
| **`confintervalML`**       | Information of Confusion Matrix by proportions of area, overall accuracy, user's accuracy with confidence interval and estimated area with confidence interval as well.                         |
| **`deepLearning`** | Deep Learning algorithms                                                  |
| **`atmosCorr`**    | Radiometric and Atmospheric Correction                              |
| **`rkmeans`**      | K-means classification                                                    |
| **`calkmeans`**    | This function allows to calibrate the kmeans algorithm. It is possible to obtain the best k value and the best embedded algorithm in kmeans.                               |
| **`pca`**          | Principal Components Analysis                                             |
| **`linearTrend`**  | Linear trend is useful for mapping forest degradation or land degradation |
| **`fusionrs`**     | This algorithm allows to fusion images coming from different spectral sensors (e.g., optical-optical, optical and SAR or SAR-SAR). Among many of the qualities of this function, it is possible to obtain the contribution (%) of each variable in the fused image |
| **`sma`**          | Spectral Mixture Analysis - Classification sup-pixel                      |
| **`tassCap`**      | The Tasseled-Cap Transformation                                           |

: Main tools available for **scikit-eo** package. \label{table:1}

Of course, there are others functions will be found in the package. 
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
img = rasterio.open(path_raster)

path_endm = r"C:\data\ml\endmembers.dbf"
endm = DBF(path_endm)

# 03. Instance of mla()
inst = MLA(image = img, endmembers = endm)

# 04. Applying RF with 70% of data to train
rf_class = inst.RF(training_split = 0.7)
```

Classification results:

![Original image and Image classified in the left and right panel respectively. \label{fig:AIM}](scikit_eo_00.png){ width=70% }


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


In this example we cover the topic of fusion of images with different observation geometry and that record information in different ranges of the electromagnetic spectrum [@Tarazona2021]. The fusion of radar and optical images, although well used to improve land cover mapping, has so far not been developed tools to discuss the contributions of both images in data fusion. In ```scikit-eo``` we developed the function ```fusionrs()``` which provides us with a dictionary with the following image fusion interpretation features:

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


### Example 04

In this final example, the assessing accuracy and area estimate will be obtained following guidance proposed by [@OLOFSSON201442]. All that we need is both the confusion matrix and a previously obtained predicted class map.

Paramaters:

- *matrix*: confusion matrix or error matrix in numpy.ndarray.
- *image_pred*: Array with 2d (rows, cols). This array should be the image classified with predicted classes.
- *pixel_size*: Pixel size of the image classified. By default is 10m of Sentinel-2. In this case is 30m (Landsat).
- *conf*: Confidence interval. By default is 95% (1.96).
- *nodata*: Nodata must be specified as 0, NaN or other any value. Keep in mind with this parameter.

```python
# 01 load raster data
path_raster = r"C:\data\ml\predicted_map.tif"
img = rasterio.open(path_optical).read(1)

# 02 load confusion matrix as .csv
path_cm = r"C:\data\ml\confusion_matrix.csv"
values = pd.read_csv(path_radar)

# 03 Applying the confintervalML:
confintervalML(matrix = values, image_pred = img, pixel_size = 30, conf = 1.96, nodata = -9999)
```

Results:

![Estimating area and uncertainty with 95%. \label{fig:AIM}](scikit_eo_05.png){ width=30%}

<!-- #region -->
# Acknowledgments

The authors would like to thank to David Montero Loaiza for the idea of the package name and Qiusheng Wu for the suggestions that helped to improve the package.


# References
<!-- #endregion -->
