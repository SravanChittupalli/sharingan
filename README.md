# SHARINGAN
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
<!-- [![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) -->



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="">
    <img src="assets\readme\sharingan.jpg" alt="Logo" width="100" height="100">
  </a>

  <h3 align="center">SHARINGAN</h3>

  <p align="center">
    A Computer Vision library
    <br />
    <a href="https://github.com/SravanChittupalli/sharingan"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!-- <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a> -->
    ·
    <a href="https://github.com/SravanChittupalli/sharingan/issues">Report Bug</a>
    ·
    <a href="https://github.com/SravanChittupalli/sharingan/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
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
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

I guess everyone must have used opencv at least once and it is a really good library for image processing. The problem is that we are soo much reliant on it that we generally tend to missout on the implementation. I have done the same and made projects by just importing `cv2` and  using the plethora of functions it provides. Therefore I am starting this repo to work with pixels and produce the same magic that opencv produces.

### Built With

The repo is completely in [Python](https://www.python.org/). We will only be using the following libraries:-

* [Numpy](https://numpy.org/): Python library that provides a multidimensional array object, various derived objects and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting etc.
<!-- * [Matplotlib](https://matplotlib.org/): Python library to make beautiful plots -->
* [OpenCV](https://opencv.org/): Python library that will strictly be used only for reading/displaying images.

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

* Anaconda/Miniconda

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/SravanChittupalli/sharingan
   ```
2. To replicate my environment do
   ```sh
   conda env create -f environment.yml
   ``` 
   else

   If you already have an environment ready then do
   ```sh
   pip install -r requirements.txt
   ```
3. To test installation
   ```sh
   python
   import sharingan
   ``` 



<!-- USAGE EXAMPLES -->
## Usage

Please refer to the test_scripts directory

1. run the test scripts
   ```sh
   python test_negative.py
   python test_log_transform.py
   ```
2. I will be documenting everything in detail after some considerable progress is made.



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/SravanChittupalli/sharingan/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

First create an issue and discuss about the feature you want to implement. If the implementation sounds good you will be assigned to implement the feature.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@SChittupalli](https://twitter.com/SChittupalli) - sravanchittupalli7@gmail.com

Project Link: [https://github.com/SravanChittupalli/sharingan](https://github.com/SravanChittupalli/sharingan)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/SravanChittupalli/sharingan.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/SravanChittupalli/sharingan.svg?style=for-the-badge
[forks-url]: https://github.com/SravanChittupalli/sharingan/network/members
[stars-shield]: https://img.shields.io/github/stars/SravanChittupalli/sharingan.svg?style=for-the-badge
[stars-url]: https://github.com/SravanChittupalli/sharingan/stargazers
[issues-shield]: https://img.shields.io/github/issues/SravanChittupalli/sharingan.svg?style=for-the-badge
[issues-url]: https://github.com/SravanChittupalli/sharingan/issues
[license-shield]: https://img.shields.io/github/license/SravanChittupalli/sharingan.svg?style=for-the-badge
[license-url]: https://github.com/SravanChittupalli/sharingan/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png