# Welcome to

# scikit-eo: A Python package for Remote Sensing Tools

[![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)]()
[![License: MIT](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![PythonVersion]( https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7%20%7C%203.8-green)]()
[![PyPI version](https://badge.fury.io/py/scikeo.svg)](https://badge.fury.io/py/scikeo)
[![Youtube](https://img.shields.io/badge/YouTube-Channel-red)]()     
[![Twitter](https://img.shields.io/twitter/url?label=Follow%20%40GeoYons&style=social&url=https%3A%2F%2Ftwitter.com%2FGeoYons)](https://twitter.com/GeoYons)

<!-- #region -->
### Links of interest:

- GitHub repo: <https://github.com/ytarazona/scikit-eo>
- Documentation: <https://ytarazona.github.io/scikit-eo/>
- PyPI: <https://pypi.org/project/scikeo/>
- Notebooks examples: <https://github.com/ytarazona/scikit-eo/tree/main/examples>
- Google Colab examples: <https://github.com/ytarazona/scikit-eo/tree/main/examples>
- GitHub repo: <https://github.com/ytarazona/scikit-eo>
- Documentation: <https://ytarazona.github.io/scikit-eo/>
- PyPI: <https://pypi.org/project/scikeo/>
- Notebooks examples: <https://github.com/ytarazona/scikit-eo/tree/main/examples>
- Google Colab examples: <https://github.com/ytarazona/scikit-eo/tree/main/examples>
- Free software: Apache 2.0


<img src="https://raw.githubusercontent.com/ytarazona/scikit-eo/main/docs/images/scikit-eo_logo.jpg" align="right" width="220"/>

# Introduction

Now a day, remotely sensed data has increased dramatically. Microwaves and optical images with different spatial and temporal resolutions are available and are using to monitor a variaty of environmental issues such as deforestation, land degradation, crop classifications, among other. Although there are efforts (i.e., Python packages, forums, communities, etc.) to make available line-of-code tools for pre-processing, processing and analysis of satellite imagery, there is still a gap that needs to be filled. In other words, too much time is still spent by many users in developing Python lines of code. Algorithms for mapping land degradation through linear trend of vegetation indices, fusion optical and radar images to classify vegetation cover, calibration of machine learning lagorithms, among others, are not available yet.

Therefore, **scikit-eo** is a Python package that provides tools for remote sensing. This package was developed to fill the gaps in remotely sensed data processing tools. Most of the tools are based on scientific publications, and others are useful algorithms that will allow processing to be done in a few lines of code. With these tools, the user will be able to invest time in analyzing the results of their data and not spend time on elaborating lines of code, which can sometimes be stressful.

# Tools for Remote Sensing

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
<!-- #endregion -->

<!-- #region -->
# Installation

To use **scikit-eo** it is necessary to install it. There are two options:

## 1. From PyPI

```python
pip install scikeo
```

```python
dem = ee.Image('USGS/SRTMGL1_003')
landcover = ee.Image("ESA/GLOBCOVER_L4_200901_200912_V2_3").select('landcover')
landsat7 = ee.Image('LANDSAT/LE7_TOA_5YEAR/1999_2003')
states = ee.FeatureCollection("TIGER/2018/States")
```

## 2. Installing from source

It is also possible to install the latest development version directly from the GitHub repository with:

```python
pip install git+https://github.com/ytarazona/scikit-eo
```
<!-- #endregion -->


