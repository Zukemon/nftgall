<p align="center">
  <a href="https://alter-gall.herokuapp.com/">
    <h1>ALTER CONCEPTS GALLERY</h1>
  </a>
  <p align="center">
    At Book Squid, your bookshelf is not only made of rich mahogany and filled with many leatherbound books -- it's virtual!
  </p>
</p>

# Table of Contents
1. [Overview](##overview)
2. [Usage](##usage)
3. [Setup](##setup)
4. [Technologies](##technology)


https://user-images.githubusercontent.com/65060500/172038125-987df9c1-99e0-4680-8011-56efb271e167.mov


## Overview: 
Alter Gallery is a platform for showcasing digital art (NFTs) using WebGL rendered interractive 3D scenes and models accompanied by music (with attached audio visualiser). This was made possible by using the Flask App, Three JS and Blender among other tools for the best results. Putting this whole project together was done using Visual Studio Code.

## Usage:
    When the user enters the URL, they'll be brought to the landing page where they must register or login if already registered. Here the user can also browse nft thumbnails.

    Once logged in the user will be able to use the following tabs:
    • 'Collections' tab: showing all purchases made.
    • 'Records' tab: showing all your transactions and total balance.
    • 'Password Change' tab: for password change.

(The default cash for registered users is set at $500. Assuming that in real life application they have a coupon code or something to register with, or even by the use of gift or credit cards.)

## Setup:

    • The main project folder which has two python scripts namely 'app.py' and 'helpers.py' and one SQL database file namely 'gallery.db'. The 'app.py' file basically handles all the routing and logic for users to navigate the app easily which also allows for parsing of data to and from a sql data base that has tables for 'users' and 'purchases' made. The 'helpers.py' file was a bit of a challenge cause I wanted to create a url type data structure that could parse data as per request made which took a little bit of time and so I found a work around by placing the data directly into my 'lookup' function(s). This also had me create separate 'buy' and 'sell' functions as per the requested NFT. I would prefer the first option but due to the deadline I set for myself I had to settle on using the 2nd option - especially because the data for my 'NFTs' aren't available anywhere online yet. I did however notice that my second option gave an increase in app speed for users.
    
    Also, in the main project folder there are subfolders namely 'static' and 'templates' as arranged according to my Flask app configuration.    

    • The 'static' folder I has four written JS files for each NFT. They are all very similar and product of the same functions with only slight changes in file names, inputs and outputs. Each file contains code with THREE JS tools that enable uploading, arranging and updating animated .glb/ gltf 3D models, including HDRI backgrounds exported from Blender and adding more elements like lights, audio visualizer etc to complete the 3D scenes and give the full experience as I had imagined. The static folder also includes a 'styles.css' file, a 'three.js-master' module nodes folder that contains my required THREE JS dependencies. Lastly, within this folder are subfolders for images, 3D model (.glb) files, music and a 'world' folder for the various HDRI backgrounds used.

    For my styling I depended on bootstrap and css which gave the app that "oomph" look and feel and effective responsiveness.

    • The 'templates' folder has all the html pages used to display the app data that is being passed to and from the user. The layout html files help make things a lot easier by handling redundancy issues thanks to jinja code. This templates help execute the 'buy', 'sell', 'collections', 'records' functions and most importantly the 3D scenes as per NFT model. 

Web App LINK: https://alter-gall.herokuapp.com

YouTube Demo LINK: <https://youtu.be/ZcxbrEl1SWU>
    
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
    
