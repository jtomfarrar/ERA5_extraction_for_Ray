# -*- coding: utf-8 -*-
"""

Attempt to read ERA 5 data from https://cds.climate.copernicus.eu/user
See this site to get this set up to work on your machine (requires account):
https://cds.climate.copernicus.eu/api-how-to

The dataset and API code are here:
    https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=form

Queued requests can be viewed here:
    https://cds.climate.copernicus.eu/live/queue

Created on Wed Jan  6 18:02:24 2021

@author: jtomf
"""
import cdsapi
import datetime
import sys

# N, W, S, E valid range is 90, -180, -90, 180
# could use lon0=0 lat0=0 dlon=180 dlat=90

# E-W valid range is -180, 180
#lon0 = -158 # NORSE=3, WHOTS=-158
#lat0 = 22.67 # NORSE=70, WHOTS=22.67
#dlat = 5
#dlon = 5
#yr = '2011'


def get_vars_for_Ray(var,yr,mon):
    '''
    Extract ERA5 pressure-level data using Copernicus Climate Data System API.  
    Saves file 'ERA5_{lon0}E_{lat0}N_{yr}.nc' in local directory

    Parameters
    ----------
    var : str
        Variable to extract.
    yr : str
        Year to extract.
    yr : str
        Year to extract.
    region_name (optional) : str 
        If provided, output filename is ERA5_surface_{region_name}_{yr}.nc (i.e., region_name + '_' + yr +'.nc')
        If not provided, output fileanme is 'ERA5_surface_{lon0}E_{lat0}N_{yr}.nc'

    Returns
    -------
    None, but saves output file in local directory.
    'ERA5_{lon0}E_{lat0}N_{yr}.nc'

    '''
    path = '../data/raw/'
    outputfile = 'SPURS2_ERA5_Ray_' + var + '_' + yr + '_' + mon + '.nc'
    
    c = cdsapi.Client()
    c.retrieve(
        'reanalysis-era5-pressure-levels',
        {
            'product_type': 'reanalysis',
            'format': 'netcdf',
            'variable': [var],
            'pressure_level': [
                '1', '2', '3', '5', '7', '10',
                '20', '30', '50', '70', '100', '125',
                '150', '175', '200', '225', '250', '300',
                '350', '400', '450', '500', '550', '600',
                '650', '700', '750', '775', '800', '825',
                '850', '875', '900', '925', '950', '975',
                '1000'],
            'year': [yr],
            'time': [
                '00:00', '01:00', '02:00', '03:00', '04:00', '05:00',
                '06:00', '07:00', '08:00', '09:00', '10:00', '11:00',
                '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
                '18:00', '19:00', '20:00', '21:00', '22:00', '23:00',
            ],
            'area': [
                12, -127, 8,
                -123,
            ],# Lat: 8.5 - 11.5 N Lon: 126.5 - 123.5 W

        'month': [mon],
        'day': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
        ],
        },
        path+outputfile)

    
    # Write a readme file to say when and by what script the file was written
    calling_fname = str(sys.argv[0])
    ReadmeFile = open("readme_"+outputfile.replace('.nc', '')+".txt", "w")
    ReadmeFile.write ('Written using ERA5_extraction_tool.get_surface_vars() on \n' + str(datetime.datetime.now()) + 
                      '\n Invoked from ' + calling_fname) 
    ReadmeFile.close()


'''
Contact

copernicus-support@ecmwf.int
Licence

Licence to use Copernicus Products
Publication date
2018-06-14
References

Citation

DOI: 10.24381/cds.adbb2d47
Related data

ERA5 hourly data on pressure levels from 1950 to 1978 (preliminary version)

ERA5 hourly data on pressure levels from 1979 to present

ERA5 hourly data on single levels from 1950 to 1978 (preliminary version)

ERA5 monthly averaged data on pressure levels from 1950 to 1978 (preliminary version)

ERA5 monthly averaged data on pressure levels from 1979 to present

ERA5 monthly averaged data on single levels from 1950 to 1978 (preliminary version)

ERA5 monthly averaged data on single levels from 1979 to present
'''
