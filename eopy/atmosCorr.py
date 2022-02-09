# -*- coding: utf-8 -*-
# +
import os
import glob
import numpy as np
import rasterio

class atmosCorr(object):
    
    '''Atmospheric Correction in Optical domain'''
    
    def __init__(self, path, nodata = -99999):
        
        '''
        
        '''
        
        self.path = path
        self.nodata = nodata
        
        path = path.replace(os.sep, '/')
        
        path = os.chdir(path)
        
        file_mtl = glob.glob("*_MTL.txt")

        dict_mtl = {}

        with open(file_mtl[0], 'r') as mtl:
            for lines in mtl:
                lines = lines.strip()
                if lines != 'END':
                    key, value = lines.split('=')
                    dict_mtl[key] = value

        names_bands = glob.glob("*B?*.TIF")
        names_bands.sort()
        
        self.dict_mtl = dict_mtl
        self.names_bands = names_bands

    def TOA(self, sat = 'LC08'):
        
        '''
        
        '''
        
        if sat == 'LC08':
            # Landsat-8 bands -> blue, green, red, nir, swir1 and swir2
            bands_lc08 = ['B2.','B3.','B4.','B5.','B6.','B7.']
            output_names = [name for name in self.names_bands if (name[41:44] in bands_lc08)]
        
        if sat == 'LT05':
            # Landsat-5 bands -> blue, green, red, nir, swir1 and swir2
            bands_lt05 = ['B1.','B2.','B3.','B4.','B5.','B7.']
            output_names = [name for name in self.names_bands if (name[41:44] in bands_lt05)]

        list_bands = []
        for i in output_names:
            with rasterio.open(i, 'r') as b:
                list_bands.append(b.read(1))

        dn = np.stack(list_bands)

        # data in [rows, cols, bands]
        #dn = np.moveaxis(st, 0, -1) 
        
        rows = dn.shape[1]
        
        cols = dn.shape[2]

        bands = dn.shape[0]

        # nodata
        if np.isnan(np.sum(dn)):
            dn[np.isnan(dn)] = self.nodata
        
        tetha = float(self.dict_mtl['SUN_ELEVATION '])
        
        toa_bands = []
        
        for i in range(bands):
            
            Mp = float(self.dict_mtl['REFLECTANCE_MULT_BAND_' + str(i+1) + ' '])
            
            Ap = float(self.dict_mtl['REFLECTANCE_ADD_BAND_' + str(i+1) + ' '])
            
            plambda = np.add(np.multiply(dn[i,:,:], Mp), Ap) # ρλ′ = Mρ*DN + Aρ
            
            TOA = plambda/np.sin((tetha*np.pi/180)) # ρλ = ρλ′/sin(theta)
            
            toa_bands.append(TOA)
        
        arr_toa = np.moveaxis(np.stack(toa_bands), 0, -1) 
        
        return arr_toa
    
    def DOS(self, sat = 'LC08', mindn = None):
        
        '''
        
        '''
        
        if sat == 'LC08':
            bands_lc08 = ['B2.','B3.','B4.','B5.','B6.','B7.']
            output_names = [name for name in self.names_bands if (name[41:44] in bands_lc08)]
            # ESUN for Landsat-8 bands -> blue, green, red, nir, swir1 and swir2
            # https://www.usgs.gov/landsat-missions/using-usgs-landsat-level-1-data-product
            ESUN = [2067, 1893, 1603, 972.6, 245.0, 79.72]

        if sat == 'LT05':
            # Landsat-5 bands -> blue, green, red, nir, swir1 and swir2
            bands_lt05 = ['B1.','B2.','B3.','B4.','B5.','B7.']
            output_names = [name for name in self.names_bands if (name[41:44] in bands_lt05)]
            
        list_bands = []
        for i in output_names:
            with rasterio.open(i, 'r') as b:
                list_bands.append(b.read(1))

        dn = np.stack(list_bands)

        # data in [rows, cols, bands]
        #dn = np.moveaxis(st, 0, -1) 
        
        rows = dn.shape[1]
        
        cols = dn.shape[2]

        bands = dn.shape[0]

        # Min of digital number for each band
        if mindn is None:
            dn_mins = [np.nanmin(dn[i,:,:][np.nonzero(dn[i,:,:])]) for i in range(bands)]
        else:
            dn_mins = mindn
            
            if not len(mindn) == bands:
                raise ValueError(f'The length of the "mindn" argument must be equal to the number'
                                f'of bands. Length of "mindn" is {len(mindn)}, and length of bands'
                                f'is {bands}')
                
        # nodata
        if np.isnan(np.sum(dn)):
            dn[np.isnan(dn)] = self.nodata
        
        tetha = float(self.dict_mtl['SUN_ELEVATION '])
        u_a = float(self.dict_mtl['EARTH_SUN_DISTANCE '])
        
        dos_bands = []
        
        for i in range(bands):
            
            ML = float(self.dict_mtl['RADIANCE_MULT_BAND_' + str(i+1) + ' '])
            
            AL = float(self.dict_mtl['RADIANCE_ADD_BAND_' + str(i+1) + ' '])
            
            L = np.add(np.multiply(dn[i,:,:], ML), AL) # L = ML*DN+AL
            
            L_min = np.add(np.multiply(dn_mins[i], ML), AL) # for each band
            
            DOS = np.pi*(np.multiply((L - L_min), (u_a)**2))/(ESUN[i]*np.sin((tetha*np.pi/180)))
            
            dos_bands.append(DOS)
        
        arr_dos = np.moveaxis(np.stack(dos_bands), 0, -1) 
        
        return arr_dos
