<p align="center">
  <a href="https://alter-gall.herokuapp.com/">
    <h1>ALTER CONCEPTS GALLERY</h1>
  </a>
</p>

# Table of Contents
1. [Overview](#overview)
2. [Usage](#usage)
3. [Setup](#setup)
4. [Technologies](#technology)


https://user-images.githubusercontent.com/65060500/172038125-987df9c1-99e0-4680-8011-56efb271e167.mov


## Overview: 
Alter Concepts Gallery is a platform for showcasing digital art (NFTs) using WebGL rendered interractive 3D scenes and models accompanied by music (and audio visualiser). This was made possible using the Flask App, Three JS and Blender among other tools for the best results.

## Usage:
<p> When the user enters the URL, they'll be brought to the landing page where they must register or login if already registered. Here the user can also browse thumbnails for the available demos.
</p>

    Tabs include:
    • 'Collections' tab: showing all purchases made.
    • 'Records' tab: showing all your transactions and total balance.
    • 'Password Change' tab: for password change.
    
    3D environment:
    • Clicking on the thumbnails the user can enter any 3D environment and purchase the NFT they want. 

(The default cash for registered users is set at $500. Assuming that in real life scenerio they have a coupon code or something similar to register with, gift cards, or credit cards.)

## Setup:
<p>
    • The main project folder contains two Python scripts, 'app.py' and 'helpers.py' and one SQL database file, 'gallery.db'. The 'app.py' file basically handles all the routing and logic for users to navigate the app easily, taking in GET and POST requests from the user which also allow for parsing data to and from a SQL database with tables for 'users' and 'purchases' made. Also included in the main project folder there are subfolders for 'static' files and 'templates' as arranged according to the Flask app configuration.</p>    
<p>
    • The 'static' folder has four JS files per NFT demo display. These are all very similar and product of the same functions with only slight variations in file names, inputs and outputs. Each file contains code with THREE JS libraries that enable uploading, setting and updating animated glb/ gltf 3D models, including HDRI backgrounds/ environments exported from Blender with added lights and an audio visualizer. Then we have a 'styles.css' file, a 'three.js-master' module nodes folder containing the required THREEJS dependencies, subfolders for images, 3D models (.glb) files, music and a folder named 'world' for the various HDRI backgrounds used.
</p>
<p>
    • The 'templates' folder has all the html pages used to display the app data for the user to make requests. The layout html files help make things a lot easier by handling redundancy issues thanks to jinja code. These templates help execute the 'buy', 'sell', 'collections', 'records' functions and 3D scenes per NFT demo model.
</p> 

<a href= "https://alter-gall.herokuapp.com"><h5>Web App</h5></a>

<a href= "https://youtu.be/ZcxbrEl1SWU"><h5>YouTube Demo</h5></a>

    
## Technologies <a name="technology"></a>
<table>
  <tr>
    <td>Languages</td>
    <td> <img alt="Python" src="https://img.shields.io/pypi/pyversions/html?style=for-the-badge&logo=python&logoColor=white"/> <img alt="JavaScript" src="https://img.shields.io/badge/javascript%20-%23323330.svg?&style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/> <img alt="HTML5" src="https://img.shields.io/badge/html5%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white"/> <img alt="CSS3" src="https://img.shields.io/badge/css3%20-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white"/></td>
  </tr>
  <tr>
    <td>Frameworks & Libraries</td>
    <td><img alt="Flask" src="https://img.shields.io/badge/flask%20-%2320232a.svg?&style=for-the-badge&logo=flask&logoColor=%white"/> <img alt="ThreeJS" src="https://img.shields.io/badge/three.js%20-%2320232a.svg?&style=for-the-badge&logo=three.js&logoColor=%white"/></td>
  </tr>
  <tr>
    <td>Hosting</td>
    <td><img alt="Heroku" src="https://img.shields.io/badge/heroku%20-%c9c3e6.svg?&style=for-the-badge&logo=heroku&logoColor=white"/>
    <img alt="AWS" src="https://img.shields.io/badge/AWS%20-%23FF9900.svg?&style=for-the-badge&logo=amazon-aws&logoColor=white"/> </td>
  </tr>
  <tr>
    <td>Databases</td>
    <td><img alt="SQL" src ="https://img.shields.io/badge/SQLite%20-C0098.svg?&style=for-the-badge&logo=SQLite&logoColor=white"/> </td>
  </tr>
</table>
