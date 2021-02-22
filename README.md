# ICESat-2 ATLAS $K_{d532}$ Tutorial
<img src="ICESat2_Schematic.png"></img>
## Overview
Turbidity, the capacity of water to attenuate light, is an important metric in many fields of coastal ocean research and engineering. As a result, a number of techniques have been developed to measure the diffuse attenuation coefficient – a common metric for turbidity – both in situ and via remote sensing. On a global scale, turbidity is most commonly measured using passive satellite spectrometry. While these techniques have been shown to be reliable in many regions, they are not able to directly measure diffuse attenuation at depth and instead rely on the water leaving irradiance. In this study, we propose an active remote sensing method to measure the diffuse attenuation at 532nm ($K_{d532}$) using the Advance Topographic Laser Altimeter System (ATLAS) on board NASA’s Ice, Cloud, and land Elevation Satellite 2 (ICESat-2). This method, in contrast to previous studies, does not rely heavily on signal processing techniques such as deconvolution, but instead employs a Random Forest Regression model. The method is designed such that it can be deployed across a broad range of geographic locations, as opposed to a single site. Additionally, it is compatible with imagery-based Kd products, such that it can be seamlessly integrated with those products and used to fill in data gaps—especially close to shore. We tested this regression model against $K_{d532}$ measurements taken by the NOAA’s Visible Infrared Imaging Radiometer (VIIRS) and found that it scored an R2 of 0.67 ± 0.12 with a mean squared error of 0.34 ± 0.14 m-1, a mean absolute error of 0.31 ± 0.4 m-1 and a mean relative difference of 1.07±0.25. These accuracy metrics serve as a benchmark for future machine learning regression studies of turbidity using ICESat-2.
<br></br>
<br></br>
**For more information on the scientific and algorithmic background for this project, please refer to** (INSERT DOI/LINK HERE)
<br></br> 
<br></br>
*Prefered Citation:*
<br></br>
(INSERT PREFERED CITATION)
<br></br>
<br></br>
*This work was completed under NASA Grant XXXXXXXXXX*


```python
import os
import pickle
```

## Load Data


```python

```

## Preprocessing


```python

```

## Import Model


```python
model_path = os.path.join(".","RF_Regression","Kd532_model.pickle")
model = pickle.load(open(fpath, "rb"))

print(type(model))
```

    <class 'sklearn.ensemble._forest.RandomForestRegressor'>



```python

```




    RandomForestRegressor()




```python

```
