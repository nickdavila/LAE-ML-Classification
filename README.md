# LAE-ML-Classification

A python program that uses Machine Learning to classify Lyman Alpha emitting galaxies (LAE).

This is a project made by Nick Davila (with a lot of help/guidance from Oscar A. Chavez from UT Astronomy)

## Ideation

Classification is what we all want to do better and more efficiently, Want to maybe use a layered ML approach to use all the data available to use to best come up with a classification.

So it would be something like,

<ol>
  <li>Using 2D data to make an estimate of LAE or Low-z galaxy, this would be something like the imaging cutout and maybe 2D CCD, though we can start with the imaging for now</li>
  <li>Using the spectra to come up with a classification</li>
  <li>Use the EAZY P(z) information to come up with an estimate as well</li>
  <li>Use single value number such as EW, Magnitude, and maybe the angular size of the source in arc seconds to help with classification and using the info from the previous three methods</li>
</ol>

Three is something that the HETDEX group has because we have the imaging counterparts in a photometric catalog so we use a SED fitting code to come up with our classification scheme.

Some tasks I have start with is look through the HETDEX database using the HETDEX api (https://github.com/HETDEX/hetdex_api) and try to manuever around the data and getting detectids that are in the NEP field, will stick with HDR2.1 for now.

Once I have those, see if I'm able to get:
<ol>
  <li>The spectra</li>
  <li>Line information such as EW, line flux</li>
  <li>Magnitude of the source</li>
  <li>RA and DEC</li>
</ol>

## Installation

Must be part of the HETDEX group to use (uses required HETDEX data/libraries).

Import the following libraries:

```
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

import pandas as pd
import seaborn as sb

# (Can use pip install for these)
```

## Usage

Feed in HETDEX data. Get out a classification

## Contributing
For any changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
