```python
# Using ML to classify LAEs in the NEP Field
import tables as tb
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

from astropy import constants as const
from astropy.table import Table, column, join
from astropy.io import fits
import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.visualization import ZScaleInterval

from regions import CircleSkyRegion, CirclePixelRegion

from hetdex_api.survey import Survey, FiberIndex
from hetdex_api.config import HDRconfig
from hetdex_api.detections import Detections
from hetdex_api.elixer_widget_cls import ElixerWidget

from hetdex_tools.get_spec import get_spectra

import pandas as pd
import seaborn as sb
```


```python
det_object = Detections('hdr2.1', loadtable = False)
```


```python
# Once it has loaded you want to filter out the data by selecting those that are in the NEP field
# to do this I will give you the verticies of a box that will encompass all the NEP field - Oscar

# The center of the NEP field is given by:
# NEP Central Coordinates:
# R.A. = 18hours00minutes00seconds, decl. = 66 degree 33minute 38.552 arcmin
# Then make a radius of 3.5 degrees centered above and find all the RA and DEC coordinates
# in the DF that are within this circle

# creating the circle region in the sky (NEP field)
ra = '18h00m00s'
dec = '+66d33m38.552s'
center_sky_coords = SkyCoord(ra, dec, frame = 'icrs')

maskregion = det_object.query_by_coords(center_sky_coords, 3.5 * u.deg)
detects_in_NEP = det_object[maskregion]     # Sources within the NEP footprint
```


```python
spec_test = spec_table = detects_in_NEP.get_spectrum(detects_in_NEP.detectid[0])
```


```python
spec_test
```




<div><i>Table length=1036</i>
<table id="table140588441005792" class="table-striped table-bordered table-condensed">
<thead><tr><th>wave1d</th><th>spec1d</th><th>spec1d_err</th></tr></thead>
<thead><tr><th>Angstrom</th><th>1e-17 erg / (Angstrom cm2 s)</th><th>1e-17 erg / (Angstrom cm2 s)</th></tr></thead>
<thead><tr><th>float32</th><th>float32</th><th>float32</th></tr></thead>
<tr><td>3470.0</td><td>1.3739702</td><td>3.301174</td></tr>
<tr><td>3472.0</td><td>1.3739702</td><td>3.301174</td></tr>
<tr><td>3474.0</td><td>1.3739702</td><td>3.301174</td></tr>
<tr><td>3476.0</td><td>1.3739702</td><td>3.301174</td></tr>
<tr><td>3478.0</td><td>1.3739702</td><td>3.301174</td></tr>
<tr><td>3480.0</td><td>1.3739702</td><td>3.301174</td></tr>
<tr><td>3482.0</td><td>1.3739702</td><td>3.301174</td></tr>
<tr><td>3484.0</td><td>1.3739702</td><td>3.301174</td></tr>
<tr><td>3486.0</td><td>1.3739702</td><td>3.301174</td></tr>
<tr><td>...</td><td>...</td><td>...</td></tr>
<tr><td>5522.0</td><td>1.9421544</td><td>1.8177477</td></tr>
<tr><td>5524.0</td><td>1.9345994</td><td>1.8484716</td></tr>
<tr><td>5526.0</td><td>1.9345994</td><td>1.8484716</td></tr>
<tr><td>5528.0</td><td>1.9345994</td><td>1.8484716</td></tr>
<tr><td>5530.0</td><td>1.9345994</td><td>1.8484716</td></tr>
<tr><td>5532.0</td><td>1.9345994</td><td>1.8484716</td></tr>
<tr><td>5534.0</td><td>1.9345994</td><td>1.8484716</td></tr>
<tr><td>5536.0</td><td>1.9345994</td><td>1.8484716</td></tr>
<tr><td>5538.0</td><td>1.9345994</td><td>1.8484716</td></tr>
<tr><td>5540.0</td><td>1.9345994</td><td>1.8484716</td></tr>
</table></div>




```python
num_detects = np.size(detects_in_NEP.detectid)    # getting the number of detections in NEP which is 69799

# this part is creating a 2d list which will then be inputting into a dictionary to be converted into an astropy Table
# 2d list because I wanted a list of lists to hold all the spec1d and spec1d error values
rows, cols = (num_detects, 1)
spec_ls = [[0 for i in range(cols)] for j in range(rows)]

# going from a list to an astropy array
for i in range(len(spec_ls)):
    spec_table = detects_in_NEP.get_spectrum(detects_in_NEP.detectid[i])
    spec_ls[i] = np.array(spec_table['spec1d'])    # turned into array because astropy column ['spec1d'] was confusing to work with
```


```python
# same code as above except this one is for the spec1d error column
# only change is getting erorr numbers so all past comments apply to here too
# I would've put them in the same block but these blocks take awhile to finish running so I didn't want to overload
specErr_ls = [[0 for i in range(cols)] for j in range(rows)]

# going from a list to an astropy array
for i in range(len(specErr_ls)):
    spec_table = detects_in_NEP.get_spectrum(detects_in_NEP.detectid[i])
    specErr_ls[i] = np.array(spec_table['spec1d_err'])
```

Want to make a table where the first row is the detectid, then I have rows for, spect1d  (array), spec1d error (array), line info like EW, line flux, magnitude, RA, and DEC.


```python
# Using a dict of column data to initialize an astropy Table
dic_to_table = {'detects': detects_in_NEP.detectid,
               'wavelength': detects_in_NEP.wave,
                'ra': detects_in_NEP.ra,
                'dec': detects_in_NEP.dec,
                'spec1d': spec_ls,
               'spec1d_err': specErr_ls}

detect_info = Table(dic_to_table)
```


```python
detect_info
```




<div><i>Table length=69799</i>
<table id="table140587334291168" class="table-striped table-bordered table-condensed">
<thead><tr><th>detects</th><th>wavelength</th><th>ra</th><th>dec</th><th>spec1d [1036]</th><th>spec1d_err [1036]</th></tr></thead>
<thead><tr><th>int64</th><th>float32</th><th>float32</th><th>float32</th><th>float32</th><th>float32</th></tr></thead>
<tr><td>2100395300</td><td>4795.6</td><td>274.08817</td><td>66.04029</td><td>1.3739702 .. 1.9345994</td><td>3.301174 .. 1.8484716</td></tr>
<tr><td>2100395301</td><td>3684.0</td><td>274.10938</td><td>66.03482</td><td>0.25948396 .. 0.104944706</td><td>4.9196553 .. 1.5617634</td></tr>
<tr><td>2100395303</td><td>4407.54</td><td>274.08798</td><td>66.04312</td><td>-0.18306294 .. 0.120995596</td><td>3.343359 .. 1.752679</td></tr>
<tr><td>2100395308</td><td>3779.01</td><td>274.16028</td><td>66.039375</td><td>3.5947866 .. 29.83107</td><td>5.0278735 .. 3.9272287</td></tr>
<tr><td>2100395309</td><td>3779.08</td><td>274.176</td><td>66.03694</td><td>7.810404 .. 8.485255</td><td>4.6782527 .. 2.2743156</td></tr>
<tr><td>2100395310</td><td>3777.96</td><td>274.16217</td><td>66.03878</td><td>5.4102297 .. 16.955706</td><td>5.465975 .. 3.143807</td></tr>
<tr><td>2100395312</td><td>3540.37</td><td>274.16037</td><td>66.039116</td><td>7.232119 .. 36.326458</td><td>5.369271 .. 4.3121314</td></tr>
<tr><td>2100395314</td><td>3779.73</td><td>274.17523</td><td>66.03811</td><td>5.690473 .. 39.514835</td><td>4.060331 .. 5.03607</td></tr>
<tr><td>2100395323</td><td>3783.45</td><td>274.17462</td><td>66.03752</td><td>6.0763054 .. 14.341705</td><td>4.181327 .. 2.8485444</td></tr>
<tr><td>2100395329</td><td>3911.59</td><td>274.1744</td><td>66.03752</td><td>3.6374705 .. 9.342827</td><td>3.9804099 .. 2.4529374</td></tr>
<tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr>
<tr><td>2102591133</td><td>3621.42</td><td>272.33502</td><td>65.94886</td><td>2.9745781 .. -0.15291205</td><td>8.845858 .. 2.1556869</td></tr>
<tr><td>2102591135</td><td>3798.57</td><td>272.3601</td><td>65.94865</td><td>6.340416 .. 43.41358</td><td>4.712274 .. 6.132177</td></tr>
<tr><td>2102591136</td><td>4496.66</td><td>272.3553</td><td>65.955605</td><td>0.41709733 .. -0.05633008</td><td>4.158766 .. 0.99008995</td></tr>
<tr><td>2102591137</td><td>3960.42</td><td>272.35065</td><td>65.95086</td><td>-0.2628514 .. 0.08616114</td><td>5.2677093 .. 1.1210852</td></tr>
<tr><td>2102591139</td><td>4664.4</td><td>272.33316</td><td>65.95318</td><td>-0.28486162 .. 0.3934254</td><td>3.0511537 .. 0.97738653</td></tr>
<tr><td>2102591140</td><td>4358.55</td><td>272.3581</td><td>65.954025</td><td>0.25720462 .. -0.06428938</td><td>4.398488 .. 1.6613194</td></tr>
<tr><td>2102591141</td><td>4198.65</td><td>272.35995</td><td>65.95431</td><td>0.8538195 .. 0.037515007</td><td>4.3777156 .. 1.1644461</td></tr>
<tr><td>2102591142</td><td>5337.0</td><td>272.33536</td><td>65.95191</td><td>-0.72364336 .. 0.034434147</td><td>3.8486855 .. 0.986437</td></tr>
<tr><td>2102591144</td><td>4173.24</td><td>272.3593</td><td>65.94936</td><td>1.5328524 .. 24.75373</td><td>4.7959304 .. 4.3725624</td></tr>
<tr><td>2102591145</td><td>3507.24</td><td>272.35077</td><td>65.94832</td><td>2.864891 .. 0.13571836</td><td>7.040993 .. 1.7914823</td></tr>
</table></div>




```python
# Once you have selected sources within the NEP footprint we can then go ahead and find some
# spectra from these sources - Oscar
spectra = detects_in_NEP.hdfile.root.Spectra
```

center_ksy.separations(skycoords entire)
    return indeces
    return distance
    return 3d

separate by dist
mask

main goal of algorithm
want it to distinguish lae vs o2 emitter. wouldn't impose cuts unless training.

cut = filter
cut = signal to noise could do plya

might need cuts for taining for confident lya and o2

increase confidence by visually inspecting

could visually inspect to increase confidence.

plotting histograms to look for outliers

hetdex isn't perfect and it catches emission lines that aren't real. visual inspections helps

no need for dataframes if i found another way

save as csv with astropy table

csv into get_spec()

    has nice documentation
        
get_spectrum good for ids ****USE*** returns all fiber spec with corresponding weights.

    try to see if can get LAE samples. O2 samples. and ambigious samples. Clasify some of them. Signal to noise (ask Oscar)
    
    
detection object filter by fields. turn to astropy table and then filter. 

Want psf weighted.


```python

```
