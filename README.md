<div id="top"></div>

<div align="center">
  
[![LinkedIn][linkedin-shield]][linkedin-url]

</div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://sites.utexas.edu/vip/">
    <img src="images/GEVIP LOGO/Purple Logo/GEVIP LOGO BOTTOM TEXT WHITE.png" alt="Logo" width="100" height="115">
  </a>
  
<h5 align="center">(Click the logo to go to our official website)</h5>
  
<h3 align="center">Classifying Lyman-Alpha Emitters With Machine Learning</h3>

  <p align="center">
    <br />
    <a href="https://github.com/nickdavila/LAE-ML-Classification/tree/main/research/papers"><strong>Explore the papers I used »</strong></a>
    <br />
    Created by Nick Davila with the help from the awesome people at GEVIP.
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About Of The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](research/posters/cns_urf_2022_poster.pdf){:height="5px" width="5px"}

One of GEVIP’s (Galaxy Evolution Vertically Integrated Project) themes is working with HETDEX (Hobby-Eberly Telescope Dark Energy Experiment). HETDEX is an unbiased spectroscopic survey using the 10m Hobby Eberly Telescope (HET) and its VIRUS integral-field unit (IFU) spectrograph. HETDEX is in the process of discovering distant galaxies on the basis of their strong Lyman-α emissions. In some GEVIP projects, we use the discovered Lyman-α emitting galaxies with the goal of understanding how the Milky Way galaxy was formed. In order to get usable data, we work on classifying Lyman-α emitting galaxies from large sets of data which contain different astronomical objects. To classify, we divide astronomical objects into groups based on their visual appearance. However, data in astronomy is getting larger and more complex, so we are turning to machine learning algorithms that can adapt to increasingly large sets of data. Therefore, this project aims to create a machine learning algorithm to accelerate the classification of Lyman-α galaxies. Our first step is to explore different machine learning algorithms related to classification. We then want to compare the algorithms and find which one is best suited for our purposes. We want an algorithm that takes images as input and can output a Lyman-α score between 0 and 1 (a probability the source is Lyman- α, where 0 is not probable at all and 1 is very probable). Lastly, we want to implement our chosen algorithm to the smaller NEP field data, and then optimize it, to one day use it with other data sets.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

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

import seaborn as sb

# Can use pip install for these
```

### Installation

This part is under construction!

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - ndavila@utexas.edu

Project Link: [https://github.com/nickdavila/LAE-ML-Classification](https://github.com/nickdavila/LAE-ML-Classification)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p>

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/nickmdavila/
[product-screenshot]: images/cns_urf_2022_poster-1.jpg
