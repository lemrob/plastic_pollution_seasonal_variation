# Data Folder: Instructions for Running Code

This folder contains local datasets needed to run the project.

## Git Ignored

This folder is **excluded from version control** via `.gitignore`, so you need to manually upload the data files to run the code!


# Data Folder Instructions

## Overview
This folder contains the input data required for the Plastic Pollution Seasonality Model.

## Data Files and Sources

(For each Shapefile, you need all files with the same name, but different file extensions, included in the same folder)


### **Plastic Pollution Data**

From The Ocean Cleanup 
- all links to sources found from here: https://theoceancleanup.com/sources/

***Relative paths:***
    data/Meijer2021_midpoint_emissions.shp
    data/Meijer2021_midpoint_emissions.shx
    data/Meijer2021_midpoint_emissions.prj
    data/Meijer2021_midpoint_emissions.sbn
    data/Meijer2021_midpoint_emissions.dbf
    data/Meijer2021_midpoint_emissions.sbx

### **River Basin and River Name Data** (for future versions)

From Natural Earth Data:
    - https://www.naturalearthdata.com/
    - README: https://github.com/nvkelso/natural-earth-vector/blob/master/README.md
    - Dataset: https://www.naturalearthdata.com/downloads/50m-physical-vectors/50m-rivers-lake-centerlines/

***Relative paths:***
    data/ne_50m_rivers_lake_centerlines/ne_50m_rivers_lake_centerlines.shp        
    data/ne_50m_rivers_lake_centerlines/ne_50m_rivers_lake_centerlines.shx
    data/ne_50m_rivers_lake_centerlines/ne_50m_rivers_lake_centerlines.prj
    data/ne_50m_rivers_lake_centerlines/ne_50m_rivers_lake_centerlines.sbn
    data/ne_50m_rivers_lake_centerlines/ne_50m_rivers_lake_centerlines.dbf
    data/ne_50m_rivers_lake_centerlines/ne_50m_rivers_lake_centerlines.sbx


### **River Location/Country Data**

From HydroShed HydroRIVERS:
    - https://www.hydrosheds.org/products/hydrorivers#downloads
        - Download the 'Asia' option from this link

***Relative paths:***
        data/HydroRIVERS_v10_as_shp/HydroRIVERS_v10_as.shp        
        data/HydroRIVERS_v10_as_shp/HydroRIVERS_v10_as.shx
        data/HydroRIVERS_v10_as_shp/HydroRIVERS_v10_as.prj
        data/HydroRIVERS_v10_as_shp/HydroRIVERS_v10_as.sbn
        data/HydroRIVERS_v10_as_shp/HydroRIVERS_v10_as.dbf
        data/HydroRIVERS_v10_as_shp/HydroRIVERS_v10_as.sbx


### **Rainfall Data**

From WorldClim2 - historical monthly weather:
    - https://www.worldclim.org/data/monthlywth.html
        - Go to "5 minutes" data, and download all datasets from 1960-2019 (version 1)
        - Save each folder inside a folder named 'rain_decades', and then store this dataset in the repository data folder

***Base Directory Path***
    data/raim_decades


