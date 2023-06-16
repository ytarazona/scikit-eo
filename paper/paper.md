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
  - name: Fernando Benitez-Paez
    affiliation: 3
    orcid: 0000-0002-9884-6471
  - name: Fabian Drenkhan
    orcid: 0000-0002-9443-9596
    affiliation: 4
  - name: Martín E. Timaná
    orcid: 0000-0003-1559-4449
    affiliation: 1
affiliations:
  - name: Applied Geography Research Center, Department of Humanities, Pontificia Universidad Católica del Perú, Lima, Peru
    index: 1
  - name: Adam Mickiewicz University in Poznań
    index: 2
  - name: The school of geography and sustainable development, University of St Andrews
    index: 3
  - name: Geography and the Environment, Department of Humanities, Pontificia Universidad Católica del Perú, Lima, Peru
    index: 4
date: 19 May 2023
bibliography: paper.bib
---

<!-- #region -->
# Summary

In recent years the availability of remote sensing data has increased substantially. A growing body of spaceborne and drone imagery including optical and radar imagery with increasing spatial (i.e. sub-metric) and temporal resolutions is now available. This remotely sensed data has enabled researchers to address and tackle a broader range of challenges effectively, by using novel tools and data at multiple scales that help to shed new light into the underlying factors that contribute to both local and global issues. 

As more accessible the data is, the bigger the need is for open-source tools to read, process and execute analysis that contributes to underpin patterns, changes and trends that are critical for environmental studies. Applications that integrate spatial-temporal data are used to map, analyze and monitor a variety of complex environmental processes and impacts, such as monitoring and assessment land cover changes [@Chaves2020], crop classifications [@POTT2021196], deforestation [@TARAZONA2018367], impact on urbanization level [@Trinder2020], climate change impacts [@Yang2013]  including assessments of glacier retreat [@Hugonnet2021] and related hydrological change [@Huss2018], biodiversity conservation [@Jeannine2022], and natural disaster management [@Kucharczyk2021].

But more availability of data, does not necessary means easier way to process the data. Analysts spend an important amount of time finding the correct libraries that allow them to read and process the remotely sensed data. 

Although there are multiple efforts to make available command line tools for selecting, processing and analyzing satellite imagery, tools for mapping land degradation through linear trend of vegetation indices [@TARAZONA2020100337], data fusion process for optical and radar images to quickly classify the vegetation cover, and the integration of machine learning techniques are still separate in multiple libraries, along with diffuse documentation that limits the analysis where the main concerns of the causes or patterns of the environmental conditions should be the main focus.

Therefore, here we present **scikit-eo**, a new Python package that provides the necessary tools for remote sensing analysis. It is a centralized, scalable and open source toolkit, developed to fill the gaps in remotely sensed data processing tools. This toolkit can be used in multiple venues from a lecturer room as a toolkit for introduction of programming skills using python and remote sensing for environmental studies, or can be usedd as part of any Python setting in a research project. The majority of the tools included in **scikit-eo** are derived from scientific publications, while others are valuable algorithms that streamline data processing into just a few lines of code. By integrating this set of diverse tools, users can focus their time and energy on analyzing the results of their data, rather than being challenged by the intricacies lines of code. By centralizing, integrating use cases and example of data, **scikit-eo** serves as a way to allow researchers to optimize their resources and dedicate their focus to the meaningful interpretation of their findings with greater efficiency.

# Highlights

**scikit-eo** is an open-source package built entirely in Python, through Object-Oriented Programming and Structured Programming, that provides a useful variety of remote sensing tools, from basic and exploratory functions to more advanced methods to classify, calibrate, or fusing satellite imagery. Depending on users' needs, **scikit-eo** can provide the basic but essential land cover characterization mapping including the confusion matrix and the required metrics such as user's accuracy, producer's accuracy, omissions and commissions errors. The combination of these required metrics can be obtained in a form of a pandas ```DataFrame``` object. Furthermore, a class prediction map as a result of land cover mapping, i.e., a land cover map which represents the output of the classification algorithm or the output of the segmentation algorithm. These two outcomes must include uncertainties with a confidence levels (e.g., at $95$% or $90$%). All required metrics from the confusion matrix can be easily computed and included confidence levels with **scikit-eo**. There are other useful tools for remote sensing analysis that can be found in this package, for more information about the full list of the supported function as well as how to install and execute the package within a python setting, visit the [scikit-eo](https://ytarazona.github.io/scikit-eo/) website.

# Audience

**scikit-eo** is a versatile Python package designed to cover a wide range of users, including students, professionals of remote sensing, researchers of environmental analysis, and organizations looking for satellite image analysis. Its comprehensive features make it well-suited for various applications, such as university teaching, that include technical and practical sessions, and cutting-edge research using the most recent machine learning and deep learning techniques applied to the field of remote sensing. Whether the user are students seeking to get insights from a satellite image analysis or a experienced researcher looking for advanced tools, **scikit-eo** offers a valuable resource to support the most valuable methods for environmental studies.

### **scikit-eo** as Research tool:

In the field of environmental studies, particularly in the study of land cover classification, the availability of scalable but user-friendly software tools is crucial for facilitating research, analysis, and modeling. With the widespread adoption of Python as one of the most popular programming language, particularly in the GIScience and remote sensing fields, the development of specialized packages has greatly enhanced the effectiveness of environmental research. **scikit-eo** is a dedicated piece of software tailored to address unique challenges encountered in the land cover mapping, forest or land degradation as well the fusion of multiple satellite imagery from several formats. **scikit-eo** provides the assessment and calibration metrics to evaluate the provided outputs. In the current version **scikit-eo** requires that users provide the dataset to process but we expect in the near future provide a wide range of functionalities for acquiring environmental data from diverse sources and file formats, enabling researchers to access satellite imagery.

One of the key strengths of **scikit-eo** lies in its advanced analysis capabilities. It provides a rich suite of algorithms specifically designed for environmental studies. These include statistical analysis, machine learning, deep learning, data fusion and spatial analysis. Researchers can leverage these tools to explore patterns, relationships, and trends within their datasets, to uncover complex land or forest degradation or mapping and classify the land cover, and generate insightful visualizations.

### **scikit-eo** in the lecture room:

 **scikit-eo** can be part of a lecturer room as part of the set of tools for environmental studies where a quantitative approach and computer labs are required. After the appropriate introduction of Python, basics of remote sensing, and the relevance of environmental studies to address climate change challenges or impacts of anthropogenic activity. Lectures can take advance of the simplicity of **scikit-eo** routines to execute supervised classification methods, Principal Components Analysis, Spectral Mixture Analysis, Mapping forest or land degradation and more types of analysis. By reducing the number of required lines of code, students can focus on the analysis and how the methods work rather of dealing with complex, and unnecessary programming tasks. Lecturers can structure their computer labs using open data sources and integrate **scikit-eo** to allow students understand the importance of the calibration and assessment metrics, get insights about the classification mapping suing satellite imagery as well as providing an introduction to more advances methods that include machine learning techniques.

### **scikit-eo** as open source tool:

As open source software keeps transforming the landscape of scientific research [@Community2019], enabling collaboration, reproducibility and transparency, **scikit-eo** was specifically developed as an open source tool. **scikit-eo** integrates most of the popular open source python libraries from the so-called geo-python stack for remote sensing (e.g,. [numpy](https://numpy.org/), [pandas](https://pandas.pydata.org/), [rasterio](https://rasterio.readthedocs.io/en/stable/) and few more) to extent and create a centralise package for advanced spatial analysis of remotely sensed data. The package provides researchers and developers with a free, scalable, and community-driven platform to process, analyze, and visualize satellite imagery more specifically, built upon the most popular python libraries, but centralizes the use of multiple functions for classification and mapping land cover.

# Functionalities


## Main tools

**Scikit-eo** includes several algorithms to process satellite images to assess complex environmental processes and impacts. These include major functions, such as atmospheric correction, machine learning and deep learning techniques, estimating area and uncertainty, linear trend analysis, combination of optical and radar images, classification sub-pixel, to name a few. Some main functions are listed below:

| Name of functions/classes  | Description|
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
| **`fusionrs`**     | This algorithm allows to fuse images coming from different spectral sensors (e.g., optical-optical, optical and SAR or SAR-SAR). Among many of the qualities of this function, it is possible to obtain the contribution (%) of each variable in the fused image |
| **`sma`**          | Spectral Mixture Analysis - Classification sup-pixel                      |
| **`tassCap`**      | The Tasseled-Cap Transformation                                           |

: Main tools available for **scikit-eo** package. \label{table:1}

Of course, there are others functions will be found in the package. 
<!-- #endregion -->

## Brief examples

### Example 01: Random Forest (RF) classifier

In this example, in a small region of southern Brazil, optical imagery from Landsat-8 OLI (Operational Land Imager) will be used to classify land cover using the machine learning algorithm Random Forest (RF) [@Breiman2001]. Four types of land cover will be mapped, i.e., agriculture, forest, bare soil and water. The input data needed is the satellite image and the spectral signatures collected. The output as a dictionary will provide: i) confusion matrix, ii) overall accuracy, iii) kappa index and iv) a classes map.

```python
# 01. Libraries to be used in these examples
import rasterio
import numpy as np
from dbfread import DBF
from scikeo.mla import MLA
from scikeo.fusionrs import fusionrs
from scikeo.calmla import calmla
from scikeo.plot import plotRGB
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# 02. Image and endmembers
path_raster = "\data\ex_O1\LC08_232066_20190727_SR.tif"
img = rasterio.open(path_raster)

path_endm = "\data\ex_O1\endmembers\endmembers.dbf"
endm = DBF(path_endm)

# 03. An instance of mla()
inst = MLA(image = img, endmembers = endm)

# 04. Applying RF with 70% of data to train
rf_class = inst.RF(training_split = 0.7)
```

Classification results:

![Original image and classified image in the left and right panel respectively.](scikit_eo_00.png){ width=100% }


### Example 02: Calibration methods for supervised classification

Given a large number of machine learning algorithms, it is necessary to select the one with the best performance in the classification, i.e., the algorithm in which the training and testing data used converge the learning iteratively to a solution that appears to be satisfactory [@Tarazona2021].
To deal with this, users can apply the calibration methods Leave One Out Cross-Validation (LOOCV), Cross-Validation (CV) and Monte Carlo Cross-Validation (MCCV) in order to calibrate a supervised classification with different algorithms. The input data needed are the spectral signatures collected as a *.dbf* or *.csv*. The output will provide a graph with the errors of each classifier obtained.

```python
# 01. Endmembers
path_endm = "\data\ex_O2\\endmembers\endmembers.dbf"
endm = DBF(path_endm)

# 02. An instance of calmla()
inst = calmla(endmembers = endm)

# 03. Applying the splitData() method
data = inst.splitData()
```

**Calibrating with *Monte Carlo Cross-Validation Calibration* (MCCV)**

**Parameters**:

- ```split_data```: An instance obtaind with ```splitData()```.
- ```models```: Support Vector Machine (svm), Decision Tree (dt), Random Forest (rf) and Naive Bayes (nb).
- ```n_iter```: Number of iterations.

```python
# 04. Running MCCV
error_mccv = inst.MCCV(split_data = data, models = ('svm', 'dt', 'rf', 'nb'), 
                       n_iter = 10)
```

Calibration results:

![Result of the calibration methods using svm, dt, rf and nb.](scikit_eo_01.png){ width=90% }


### Example 03: Imagery Fusion.

This is an area where **scikit-eo** provides a novel approach to merge different types of satellite imagery. We are in a case where, after combining different variables into a single output, we want to know the contributions of the different original variables in the data fusion. The fusion of radar and optical images, despite of its well-know use, to improve land cover mapping, currently has no tools that help researchers to integrate or combine those resources. In this third example, users can apply imagery fusion with different observation geometries and different ranges of the electromagnetic spectrum [@Tarazona2021]. The input data needed are the optical satellite image and the radar satellite image, for instance.


In ```scikit-eo``` we developed the function ```fusionrs()``` which provides us with a dictionary with the following image fusion interpretation features:

- *Fused_images*: The fusion of both images into a 3-dimensional array (rows, cols, bands).
- *Variance*: The variance obtained.
- *Proportion_of_variance*: The proportion of the obtained variance.
- *Cumulative_variance*: The cumulative variance.
- *Correlation*: Correlation of the original bands with the principal components.
- *Contributions_in_%*: The contributions of each optical and radar band in the fusion.

```python
# 01 Loagind dataset
path_optical = "data/ex_03/LC08_003069_20180906.tif"
optical = rasterio.open(path_optical)

path_radar = "data/ex_03/S1_2018_VV_VH.tif"
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
ln1 = axes.plot(x_labels, prop_var, marker ='o', markersize = 6,  
                label = 'Proportion of variance')

axes2 = axes.twinx()
ln2 = axes2.plot(x_labels, cum_var, marker = 'o', color = 'r', 
                 label = "Cumulative variance")

ln = ln1 + ln2
labs = [l.get_label() for l in ln]

axes.legend(ln, labs, loc = 'center right')
axes.set_xlabel("Principal Component")
axes.set_ylabel("Proportion of Variance")
axes2.set_ylabel("Cumulative (%)")
axes2.grid(False)
plt.show()
```

![Proportion of Variance and accumulative.](scikit_eo_02.png){ width=70% }

```python
# 07 Contributions of each variable in %:
fusion.get('Contributions_in_%')
```

![Contributions of each variable in %.](scikit_eo_03.png){ width=90% }

```python
# 08 Preparing the image:
arr = fusion.get('Fused_images')

## Let´s plot
fig, axes = plt.subplots(figsize = (8, 8))
plotRGB(arr, bands = [1,2,3], title = 'Fusion of optical and radar images')
plt.show()
```

![Fusion of optical and radar images. Principal Component 1 corresponds to red channel, Principal Component 2 corresponds to green channel and Principal Component 3 corresponds to blue channel.](scikit_eo_04.png){ width=50% }


### Example 04: Accuracy assessment    

In this final example, after obtaining the predicted class map, we are in a case where we want to know the uncertainties of each class. The assessing accuracy and area estimate will be obtained following guidance proposed by `@OLOFSSON201442`. All that users need are the confusion matrix and a previously obtained predicted class map.

```confintervalML``` requires the following parameters:

- *matrix*: confusion matrix or error matrix in numpy.ndarray.
- *image_pred*: a 2-dimensional array (rows, cols). This array should be the classified image with predicted classes.
- *pixel_size*: Pixel size of the classified image. Set by default as 10 meters. In this example is 30 meters (Landsat).
- *conf*: Confidence interval. By default is 95% (1.96).
- *nodata*: No data must be specified as 0, NaN or any other value. Keep in mind with this parameter.

```python
# 01 Load raster data
path_raster = r"\data\ex_O4\ml\predicted_map.tif"
img = rasterio.open(path_optical).read(1)

# 02 Load confusion matrix as .csv
path_cm = r"\data\ex_O4\ml\confusion_matrix.csv"
values = pd.read_csv(path_radar)

# 03 Applying the confintervalML:
confintervalML(matrix = values, image_pred = img, pixel_size = 30, conf = 1.96, 
               nodata = -9999)
```

Results:

![Estimating area and uncertainty with 95%.](scikit_eo_05.png){ width=80%}


# Acknowledgments

The authors would like to thank to David Montero Loaiza for the idea of the package name and Qiusheng Wu for the suggestions that helped to improve the package.

# References
