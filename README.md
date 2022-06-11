# ALTER GALLERY


#### Video Demo:



https://user-images.githubusercontent.com/65060500/172038125-987df9c1-99e0-4680-8011-56efb271e167.mov





YouTube LINK: <https://youtu.be/ZcxbrEl1SWU>


#### Description: 
Alter Gallery is a platform for showcasing digital art (NFTs) using WebGL rendered interractive 3D scenes and models accompanied by music (with attached audio visualiser). This was made possible by using the Flask App, Three JS and Blender among other tools for the best results. Putting this whole project together was done using Visual Studio Code.


    
#### Files used in this Project include:

    - The main project folder which has two python scripts namely 'app.py' and 'helpers.py' and one SQL database file namely 'gallery.db'. The 'app.py' file basically handles all the routing and logic for users to navigate the app easily which also allows for parsing of data to and from a sql data base that has tables for 'users' and 'purchases' made. The 'helpers.py' file was a bit of a challenge cause I wanted to create a url type data structure that could parse data as per request made which took a little bit of time and so I found a work around by placing the data directly into my 'lookup' function(s). This also had me create separate 'buy' and 'sell' functions as per the requested NFT. I would prefer the first option but due to the deadline I set for myself I had to settle on using the 2nd option - especially because the data for my 'NFTs' aren't available anywhere online yet. I did however notice that my second option gave an increase in app speed for users.
    
    Also, in the main project folder there are subfolders namely 'static' and 'templates' as arranged according to my Flask app configuration.    

    - The 'static' folder I has four written JS files for each NFT. They are all very similar and product of the same functions with only slight changes in file names, inputs and outputs. Each file contains code with THREE JS tools that enable uploading, arranging and updating animated .glb/ gltf 3D models, including HDRI backgrounds exported from Blender and adding more elements like lights, audio visualizer etc to complete the 3D scenes and give the full experience as I had imagined. The static folder also includes a 'styles.css' file, a 'three.js-master' module nodes folder that contains my required THREE JS dependencies. Lastly, within this folder are subfolders for images, 3D model (.glb) files, music and a 'world' folder for the various HDRI backgrounds used.

    For my styling I depended on bootstrap and css which gave the app that "oomph" look and feel and effective responsiveness.

    - The 'templates' folder has all the html pages used to display the app data that is being passed to and from the user. The layout html files help make things a lot easier by handling redundancy issues thanks to jinja code. This templates help execute the 'buy', 'sell', 'collections', 'records' functions and most importantly the 3D scenes as per NFT model. 


#### Use:
    - Within the ThreeJS 3D (NFT Demo) scenes I've created click events to call and run functions on both the 3D objects (works best on desktop version) and on the title of the tracks (works on both desktop and mobile versions). So you can play music with animation, while you navigate the 3D environments. You can also pause/ play the music on command, while animation plays, hit browser reload button to reset, buy NFT from display and return to gallery at any point by clicking on the Gallery logo.

    - 'Collections' tab: showing all purchases made.
    - 'Records' tab: showing all your transactions and total balance.
    - 'Password Change' tab: for password change.

#### PS.
    The default cash for registered users is set at $500. Assuming that in real life application they have a coupon code or something to register with, or even by the use of gift or credit cards.
    


**This is my final Project and this is CS50! Thank you!**
    
