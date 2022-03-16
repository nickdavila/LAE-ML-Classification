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

import seaborn as sb

#picking which survey to get our data from
config = HDRconfig(survey = 'hdr2.1')
file_elix = tb.open_file(config.elixerh5)

#getting the detections info from the h5 file
Detections_h5 = file_elix.root.Detections

# Creating a detections object with ALL the dections in HDR2.1.
# This may take some time to load since it is reading in all the millions of Spectra in HDR2.1
det_object = Detections('hdr2.1', loadtable=False)

# Once loaded I want to filter out the data by selecting those that are in the NEP field
# to do this I will use the verticies of a 'box' that will encompass all the NEP field

# The center of the NEP field is given by:
# NEP Central Coordinates:
# R.A. = 18hours00minutes00seconds, decl. = 66 degree 33minute 38.552 arcmin
# Then make a radius of 3.5 degrees centered above and find all the RA and DEC coordinates
# in the DF that are within this circle

ra = '18h00m00s'
dec = '+66d33m38.552s'
center_sky_coords = SkyCoord(ra, dec, frame = 'icrs')
maskregion = det_object.query_by_coords(center_sky_coords, 3.5 * u.deg)
detects_in_region = det_object[maskregion]
print(np.size(detects_in_region.detectid))

# Once selected sources within the NEP footprint I can then go find some
# spectra from these sources
