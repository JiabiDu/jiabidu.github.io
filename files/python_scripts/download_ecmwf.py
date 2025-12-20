#!/Users/JiabiDu/miniforge3/bin/python
'''
   The script will download the ecmwf wind, pressure, radiation and prcipitation to an nc file. 
   Sample call of this script (the command line argument will be used to define the year to download)
   python downloadECMWF_NGoM.py 2018 01 &
   Use the batch.py to download mulitple month or multiple year of data
'''
import cdsapi
import sys
import os

#================================================
area=[32, 46, 21, 61] #N/W/S/E
tyear,tmon='2018','01'
redo = False
if len(sys.argv)==3: tyear,tmon=sys.argv[1],sys.argv[2]  # the first commandline argument; the script name will be sys.argv[0]
#================================================

c = cdsapi.Client()
fname=f'{tyear}{tmon}.zip'
if os.path.exists(fname) and not redo: sys.exit(f'{fname} already exists')
print('Sending request for',fname)
c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type':'reanalysis',
        'variable':[
            '10m_u_component_of_wind','10m_v_component_of_wind','2m_temperature','2m_dewpoint_temperature',
            'mean_sea_level_pressure','mean_surface_downward_short_wave_radiation_flux','mean_surface_downward_long_wave_radiation_flux',
            'total_precipitation'
        ],
        'year':tyear,
        'month':[
            tmon,],
        'day':[
            '01','02','03',
            '04','05','06',
            '07','08','09',
            '10','11','12',
            '13','14','15',
            '16','17','18',
            '19','20','21',
            '22','23','24',
            '25','26','27',
            '28','29','30',
            '31'
        ],
        'time':[
            '00:00','01:00','02:00',
            '03:00','04:00','05:00',
            '06:00','07:00','08:00',
            '09:00','10:00','11:00',
            '12:00','13:00','14:00',
            '15:00','16:00','17:00',
            '18:00','19:00','20:00',
            '21:00','22:00','23:00'
        ],
        "data_format": "netcdf",
        "download_format": "unarchived",
        "area": area
    },
    f'{tyear}{tmon}.zip')

## steps to download the ecmwf data
# 1. prepare the credential file;
# copy the following content (subject to change after account renewal) to ".cdsapirc." under C:/Users/user_name/. (the final dot will automatically disappear) or '.cdsapirc' under ~/
# url: https://cds.climate.copernicus.eu/api/v2
# key: 12593:b35635ac-0773-4cf0-ae8d-7893e32c2bd2
#
# 2. install cdsapi
# >>pip install cdsapi
#
# 3. Prepare the python script (say DownloadECMWF_NoG.py) by pasting the on-line cds api request text from on-line form
# https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download
#
# 4. In the script, adding the following line to specify the area. Don't need to change the grid, by default, it is 0.25 degree resolution.
# 'area': [32, -98, 17, -78],   #for Gulf of Mexico
# 'area': "40/-78/34/-73",   #for CB
# 
# to check the request status
#https://cds.climate.copernicus.eu/requests?tab=all
# login info: tamug email + 

