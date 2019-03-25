# Efficient Image Processing with Python and GDAL


## Why GDAL?

GDAL is open source and conforms with the [OGC](http://www.opengeospatial.org/).

It has a wide variety of command line utilities and it is possible to define our own functions using its modules.

I have personally found that combining the command line utilities with Python is a highly effective way to solve applied problems.
It allows you to not re-write the wheel when it comes to processing geospatial data and concentrate on the domain application.

## Requirements and installation

GDAL is the main requirement of the approach used in this tutoriel.

The easiest way to configure python virtual envrionment with GDAL is [conda](https://conda.io/en/latest/).

Install the conda version for your system. Create a conda virtual environment and activate it. 
This step can be done with the conda navigator or with the [command line](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

In the activated environment, enter:

```bash
$ conda install -c conda-forge gdal 
```

Enter *y* when asked to install other requirements for GDAL. 

## Objectives

Following the tutorials on the command line and using the command line with Python 
([1](), [2](), [3]()),  
the focus of the article is process raster data usin the [*gdal_calc*](https://www.gdal.org/gdal_calc.html) utility.

If you found yourself googling through geospatial processing solutions, chances are you enventually landed on the 
[GDAL/OGR Cookbook](https://pcjericks.github.io/py-gdalogr-cookbook/). The cookbook is excellent for more specific cases,
but most of the time the command line utilities are sufficient for popular data processing needs.

Geospatial data is harder to work with. Writing data processing scripts from scratch can be a difficult task.
Check out the command line utilities, chances are that the process you are looking for already exists. 
You probably just saved yourself a lot of time.

Geospatial GUIs are great, they answer the needs for many different teams. 
However, in many cases they simply are not efficient enough or do not allow for enough customization in the workflows.
A striking example is the time necessary just to open rasters in such applications.

Command line utilities are an interesting solution to most problems but demand a certain expertise (less intuitive/visual).

This article is an introduction to a using geospatial command line tools and integrating them to data processing workflows.

The examples presented are with the raster calculator utility (*gdal_calc*), a utility that answer most your needs when it comes to processing raster data.

## Introduction to *gdal_calc*

We can see the usage of utility by navigating to the docs or by simply typing: 

```bash
$ python path_to_gdal_calc/gdal_calc.py -h
```
*Make sur your environment is activated!*

```bash
gdal_calc.py --calc=expression --outfile=out_filename [-A filename]
                    [--A_band=n] [-B...-Z filename] [other_options]
```

The utility allows to perform any type of calculation that can be represented with an expression.

A simple example is applying a mask raster (values of 0 and 1) to all bands of another raster by simply multiplying them together:

```bash
$ python path_to_gdal_calc/gdal_calc.py --calc="A*B" -A my_raster.tif -B my_mask.tif --allBands=A
```

An important note, is that by default only a single band is processed.

## Calculating an indice (NDVI)

It is possible to assign specific bands to different inputs in our command. 

This enables calculating indices like an NDVI. Example of a raster with RED at band 1 and NIR at band 4:

```bash
$ python path_to_gdal_calc/gdal_calc.py 
--calc="((B-A)/(B+A))" 
-A my_raster.tif --A_band=1 --B my_raster.tif --B_band=4
--outfile=ndvi.tif
```

## Note on raster data types

I have come across problems in the past when simply executing calculation expression as presented above. 
It is often necessary to cast our rasters to arrays in the calculation. The NDVI command would be re-written as:

```bash
$ python path_to_gdal_calc/gdal_calc.py 
--calc="((asarray(B, dtype=float32)-asarray(A, dtype=float32)/(asarray(B, dtype=float32)+asarray(A, dtype=float32)))" 
-A my_raster.tif --A_band=1 --B my_raster.tif --B_band=4
--outfile=ndvi.tif
```

It is not optimal when calling single commands in a shell. 
However, it is not to difficult to automate functions in Python scripts, such as in the following examples.

## Automate raster processing with *gdal_calc* and Python

Combining Python tools for calling command line utilities enables script to remain clean and for developers to 
concentrate on the logic of a problem.

Check out [Calling the cl from python]() for a reminder on how to use the command line in python scripts (if you are familiar with French).

## Example: radiance to reflectance corrections

If the interest of your application is the radiometric properties of your targets, correcting remote sensing images from radiance values 
to reflectance values might be necessary.

Radiance is the energy measured by the sensors, it is measured in watt/(steridian/square meter). 
It is the result of properties of the target but the environment such as atmospheric conditions.

Reflectance is the portion of energy reflected by the target, 
it it a property of a target independent of environmental conditions.

More on remote sensing here: [NRCAN, Fundamentals of Remote Sensing](https://www.nrcan.gc.ca/node/9309).

Having recently work on drone remote sensing projects, there was a need to automate image processing of large image datasets
to transform radiance values to reflectance values. The program had to receive correction parameters and apply them to each image of a folder. 
The correction parameters are different for every band. 
For this tutorial, we will assume that the corrections parameters are constant during drone image acquisition. 
In reality, this is rarely the case.

(how much energy the sensor measures) 
to reflectance values (the ratio of energy reflected by the target) might be necessary.

- Process image before SfM

- Folder containing images

- Base images in folder

- Extract corrections

- Apply corrections to images

## Conclusion
