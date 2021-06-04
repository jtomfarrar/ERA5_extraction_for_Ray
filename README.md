ERA5_extraction_for_Ray
==============================

[![License:MIT](https://img.shields.io/badge/License-MIT-lightgray.svg?style=flt-square)](https://opensource.org/licenses/MIT)

This repo is to improve upon older code I had written to extract ERA5 data for Ray Graham.  (This is also my first test using my own cookiecutter science-project template!)  The code uses the Copernicus API to read data from this dataset:
    https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=form

It extracts a bunch of files (one per month).  Then, there is a matlab m-file to read and merge the data into arrays.

--------

<p><small>Project based on the <a target="_blank" href="https://github.com/jbusecke/cookiecutter-science-project">cookiecutter science project template</a>.</small></p>
