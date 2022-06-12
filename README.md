# scikit-eo

[![License: MIT](https://img.shields.io/badge/licence-MIT-green)](https://opensource.org/licenses/MIT)
[![PythonVersion]( https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7%20%7C%203.8-green)]()
[![image](https://img.shields.io/pypi/v/eopy.svg)](https://pypi.python.org/pypi/scikit-eo)

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

To used **scikit-eo** it is necessary to install first. There are three options:

## 1. From PyPI

It is not yet available

## 2. Installing from source

It is also possible to install the latest development version directly from the GitHub repository with:
    
    pip install git+https://github.com/ytarazona/scikit-eo
<!-- #endregion -->

## Features

-   TODO

## Credits

This package was created with [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
