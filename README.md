# LAE-ML-Classification

A python program that uses Machine Learning to classify Lyman Alpha emitting galaxies (LAE).

## Installation

Must be part of the HETDEX group to use (uses required HETDEX data/libraries).

Import the following libraries:

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

(Can use pip install for these)

## Usage

Feed in HETDEX data. Get out a classification
```python
    blank for now
```

## Contributing
For any changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
