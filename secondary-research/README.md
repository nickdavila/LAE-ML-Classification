# Secondary Research

This folder is going to contain all the papers/courses/etc I have/will read to help me complete the project. It will also includes general notes and useful resources I find throughout my project. I won't put every single thing I have read/skimmed here, but only things I would like to maybe revisit someday.


## Papers/journals TO READ:

<details><summary>Spring 2023 semester</summary>

* Random forest classification data developed from multitemporal Landsat 8 spectral data and phenology metrics for a subregion in Sonoran and Mojave Deserts, April 2013 – December 2020 https://www.usgs.gov/data/random-forest-classification-data-developed-multitemporal-landsat-8-spectral-data-and

* A comparison of random forest and its Gini importance with standard chemometric methods for the feature selection and classification of spectral data https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-10-213

</details>

<details><summary>Dec 2022</summary>

 * "Random forest classification of stars in the Galactic Centre" by P M Plewa [Link](https://academic.oup.com/mnras/article/476/3/3974/4907985)

</details>

## Papers/journals archive:
#### (Skimmed or completely read)

<details><summary>Spring 2023 semester</summary>

* "Stellar spectral classification and feature evaluation based on a random forest" https://iopscience.iop.org/article/10.1088/1674-4527/19/8/111/meta

* "Application of random forest to stellar spectral classification" https://ieeexplore.ieee.org/document/5648041
</details>

<details><summary>May 2022</summary>

 * "Machine Learning in Astronomy: a practical overview" by Dalya Baron [Link](https://arxiv.org/abs/1904.07248)

</details>
 
## Links to all useful courses (complete or incomplete to show if I have finished or not):

(Complete, paid) CS 329E at University of Texas at Austin https://www.cs.utexas.edu/courses/329e-elements-data-analytics

(Complete, paid) CS 323E at University of Texas at Austin https://www.cs.utexas.edu/courses/323e-elements-scientific-computing

(Incomplete, FREE) Caltech's 'Learning From Data' https://work.caltech.edu/telecourse

## Links to the rest:

### Youtube videos TO WATCH:

<details><summary>Dec 2022 Papers</summary>

 * "Random Forest Algorithm Clearly Explained!" https://www.youtube.com/watch?v=v6VJ2RO66Ag&ab_channel=NormalizedNerd
 
 * "StatQuest: Random Forests Part 1 - Building, Using and Evaluating" https://www.youtube.com/watch?v=J4Wdy0Wc_xQ&ab_channel=StatQuestwithJoshStarmer
 
 * "59 - What is Random Forest classifier?" https://www.youtube.com/watch?v=6QSrgmMH4hE&ab_channel=DigitalSreeni

</details>


## General notes

<details><summary>Fall 2022</summary>

 I started off the semester with a really broad plan to automate the classification of LAEs. Since I couldn't just automate everything at once, I focused on a way to first classify the spectra. The ultimate goal is to finish classifying spectra and move to something else, but as of right now (Dec 1, 2022) I will only focus on spectra.
 
 In our subgroup meetings it was decided that I would first focus on training a ML algorithm to differentiate between High-Z spectra and noise spectra. To do this I spent time writing code to make me a noise sample. After that, I spent time making a sample of random sources in order to run them through an autoencoder and then t-SNE and finally Gaussian mixture (code for these was adapted from Valentina's old work). After that I wrote some code to give me a "high quality" sample of high-z spectra. My goal now is to train a Random Forest ML algorithm to differentiate between high-z spectra and noise.

</details>
