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
Alter Concepts Gallery is a platform for showcasing digital art (NFTs) using WebGL rendered interractive 3D scenes and models accompanied by music (and audio visualiser). This was made possible using the Flask App, Three JS and Blender among other tools for the best results. I also used Visual Studio Code for my text editing.

## Usage:
<p> When the user enters the URL, they'll be brought to the landing page where they must register or login if already registered. Here the user can also browse nft thumbnails.

    Once logged in the user will be able to use the following tabs:
    • 'Collections' tab: showing all purchases made.
    • 'Records' tab: showing all your transactions and total balance.
    • 'Password Change' tab: for password change.
    
    3D environment:
    • Using the thumbnails the user can enter 3D environments and purchase the NFT they want.</p> 

(The default cash for registered users is set at $500. Assuming that in real life scenerio they have a coupon code or something similar to register with, or even using of gift cards, or credit cards.)

## Setup:
<p>
    • The main project folder contains two Python scripts, 'app.py' and 'helpers.py' and one SQL database file, 'gallery.db'. The 'app.py' file basically handles all the routing and logic for users to navigate the app easily, taking in GET and POST requests from the user which also allow for parsing data to and from a SQL database with tables for 'users' and 'purchases' made. Also, in the main project folder there are subfolders for 'static' files and 'templates' as arranged according to the Flask app configuration.</p>    
<p>
    • The 'static' folder has four JS files for each NFT. They are all very similar and product of the same functions with only slight variations in file names, inputs and outputs. Each file contains code with THREE JS tools that enable uploading, arranging and updating animated glb/ gltf 3D models, including HDRI backgrounds exported from Blender and added elements like lights and an audio visualizer to complete the 3D scenes. The static folder also includes a 'styles.css' file, a 'three.js-master' module nodes folder containing the required THREEJS dependencies. Also included within this folder are subfolders for images, 3D models (.glb) files, music and a folder named 'world' for the various HDRI backgrounds used.
    For my styling I used bootstrap and css.</p>
<p>
    • The 'templates' folder has all the html pages used to display the app data for the user to make requests. The layout html files help make things a lot easier by handling redundancy issues thanks to jinja code. This templates help execute the 'buy', 'sell', 'collections', 'records' functions and most importantly the 3D scenes per NFT model.</p> 

<a href= "https://alter-gall.herokuapp.com"><h2>Web App LINK</h2></a>

<a href= "https://youtu.be/ZcxbrEl1SWU"><h2>YouTube Demo LINK</h2></a>

    
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
