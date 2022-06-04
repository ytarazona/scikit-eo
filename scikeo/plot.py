# +
import rasterio
import numpy as np
import matplotlib.pyplot as plt

def plotRGB(image, bands = [4,3,2], stretch = 'std', title = None, xlabel = None, ylabel = None, ax = None, **kwargs):
    
    '''
    Plotting an image in RGB
    
    This function allows to plot an satellite image in RGB channels.
        
        Parameters:
            
            image: Optical images. It must be rasterio.io.DatasetReader with 3d.
            
            bands: A list contain the order of bands to be used in order to plot in RGB. For example,
                   for six bands (blue, green, red, nir, swir1 and swir2), number four (4) indicates 
                   the swir1 band, number three (3) indicates the nir band and the number two (2) indicates
                   the red band.
                   
            stretch: Contrast enhancement using the histogram. There are two options here: i) using
                     standard deviation ('std') and ii) using percentiles ('per'). For default is 'std', which means
                     standard deviation.
            
            title: Assigned title.
        
            xlabel: X axis title.
        
            ylabel: Y axis title.
        
            ax: current axes
        
            **kwargs: These will be passed to the matplotlib imshow(), please see full lists at:
                https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html
    
        Return:
        
            ax : Graphic of change detection using the matplotlib plot function.
        
    '''
    
    if not isinstance(image, (rasterio.io.DatasetReader)):
        raise TypeError('"image" must be raster read by rasterio.open().')
        
    st = image.read()
    
    # data in [rows, cols, bands]
    st = np.moveaxis(st, 0, -1) 
    
    bands = bands
    
    arr_rgb = np.dstack([st[:, :, bands[0]], st[:, :, bands[1]], st[:, :, bands[2]]])
    
    if stretch == 'std':
        
        mean = np.mean(arr_rgb)
        
        std = np.std(arr_rgb)*1.5
        
        min_val = np.max([mean - std, np.min(arr_rgb)])
        
        max_val = np.min([mean + std, np.max(arr_rgb)])
        
        clipped_arr = np.clip(arr_rgb, min_val, max_val)
        
        arr_rgb_norm = (clipped_arr - min_val)/(max_val - min_val)

    elif stretch == 'per':
        
        p10 = np.percentile(arr_rgb, 10) # percentile10
        
        p90 = np.percentile(arr_rgb, 90) # percentile90
        
        clipped_arr = np.clip(arr_rgb, p10, p90)
        
        arr_rgb_norm = (clipped_arr - p10)/(p90 - p10)
        
    else:
        raise TypeError('Stretch type is not implemented. Please select either "std" or "per".')

    if ax is None:
        ax = plt.gca()

    ax.imshow(arr_rgb_norm, **kwargs)
    ax.grid(False)
    
    # title
    if title is not None:
        ax.set_title(title)
    
    # ylabel
    if ylabel is not None:
        ax.set_ylabel(ylabel)
    
    # xlabel
    if xlabel is not None:
        ax.set_xlabel(xlabel)
    
    #ax.set_axis_off()

    return ax
