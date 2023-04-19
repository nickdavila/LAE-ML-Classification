<div id="top"></div>

<div align="center">
  
[![LinkedIn][linkedin-shield]][linkedin-url]

</div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  
  <h2 align="center">Classifying High-Redshift Galaxies from the HETDEX Survey Using a Random Forest Classifier</h2>
  
  <a>
    <img src="images/GEVIP LOGO/Purple Logo/GEVIP LOGO BOTTOM TEXT WHITE.png" alt="Logo" width="100" height="115">
  </a>
  
  <h5 align="center"> https://sites.utexas.edu/vip/ </h5>

  <p align="center">
    Created by Nick Davila with the help from the awesome people at GEVIP
    <br />
    <a href="https://github.com/nickdavila/LAE-ML-Classification/tree/main/research"><strong>Explore the secondary research for this project»</strong></a>
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About Of The Project</a>
    </li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#installation">Installation</a></li>
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

[![Product Name Screen Shot][product-screenshot]](secondary-research/posters/nick_davila_cns_urf_2023_poster.pdf)

One of GEVIP’s (Galaxy Evolution Vertically Integrated Project) themes is working with HETDEX (Hobby-Eberly Telescope Dark Energy Experiment). HETDEX is an unbiased spectroscopic survey using the 10m Hobby Eberly Telescope (HET) and its VIRUS integral-field unit (IFU) spectrograph. HETDEX is in the process of discovering distant galaxies on the basis of their strong Lyman-α emissions. In some GEVIP projects, we use the discovered Lyman-α emitting galaxies with the goal of understanding how the Milky Way galaxy was formed. In order to get usable data, we work on classifying Lyman-α emitting galaxies from large sets of data which contain different astronomical objects. To classify, we divide astronomical objects into groups based on their visual appearance. However, data in astronomy is getting larger and more complex, so we are turning to machine learning algorithms that can adapt to increasingly large sets of data. Therefore, this project aims to train a Random Forest Classifier to classify astronomical spectra and differentiate between noise spectra and high-redshift galaxy spectra. 

In order to maximize our discovery space, we need to push our detections to low signal-to-noise (very noisy data), so we need to find a robust way to differentiate between true astrophysical objects and noise features in the data catalog. Historically ML algorithms struggle with differentiating real spectra and noise spectra. The motivation for this project was to implement an algorithm to solve this problem specifically. This will allow for more high-redshift sources to be studied, which will help us learn more about the period of reionization in the universe.

<p align="right">(<a href="#top">back to top</a>)</p>

## Prerequisites

We used the HETDEX HDR3 internal day release 3.0.1 and the HETDEX API: https://github.com/HETDEX/hetdex_api

Import the following libraries:

```
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns # statistical data visualization

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics 

# Can use pip install for these
```

### Installation

This part is under construction!

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Whenever you need to classify galaxies based on their strong Lyman-α emissions. You input an image (specify type later) and data (also specify later) and then the program will classify for you and tell you if those partain to a Lyman-α emitting galaxy.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

So basically I want to automate the classification process we do by training an AI to do it. What I'm going to do is have it basically retrace our steps and automate all of them. So when we classify, these are our steps:
1. Look at spectrum and inspect it
2. Look at CCD’s
3. Look at upper left information
4. Look at images
5. Etc.

It seems very ambitious but I have to try. So the final goal is to automate all of these, and slowly but surely I have to work through each one. Automating each one is probably like its own mini-project. So I’ll first start with automating step 1, and let’s say we get a probability based on number 1 alone. Then we get a probability based on automating number 2 alone. We repeat this until we get a final probability of all of them and we add it up to get a final probability (idk if that's how the statistics works but that's the goal).


- [ ] Get all the data required to train the machine learning algorithm
- [ ] Find and compare algorithms to see which performs best 
- [ ] Implement the 'best' and have it output 
    - [ ] Write a note about this?

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request or you can also simply email me!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Nick Davila - ndavila@utexas.edu

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Very special thanks to Oscar A. Chavez Ortiz for guiding me throughout the entire project.
* Thank you to Gene Leung and Steven Finkelstein for their expert advice along the way.
* Thank you to all my peers in GEVIP for the tips and inspiration.
<!-- * []() use this so that it's like a link to something -->

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License.

[MIT](https://choosealicense.com/licenses/mit/)

<p align="right">(<a href="#top">back to top</a>)</p>

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/nickmdavila/
[product-screenshot]: images/nick_davila_cns_urf_2023_poster.jpg
