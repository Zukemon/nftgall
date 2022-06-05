import * as THREE from './three.js-master/build/three.module.js';

import {
  OrbitControls
} from 'https://cdn.jsdelivr.net/npm/three@0.119.1/examples/jsm/controls/OrbitControls.js';
import {
  GLTFLoader
} from './three.js-master/examples/jsm/loaders/GLTFLoader.js';
import {
  RGBELoader
} from 'https://cdn.jsdelivr.net/npm/three@0.119.1/examples/jsm/loaders/RGBELoader.js';


var container, stats, controls;
var camera, scene, renderer;

var raycaster, INTERSECTED;
// var raycaster;
var mixer;

var demo = document.querySelector("demo");

var mouse = { x: 0, y: 0 }, INTERSECTED;


init();
render();

function init() {


  container = document.createElement('div');
  document.body.appendChild(container);

  camera = new THREE.PerspectiveCamera(55, window.innerWidth / window.innerHeight, 0.25, 20);
  camera.position.set(-8.2, -0.5, 6.7);

  scene = new THREE.Scene();

  raycaster = new THREE.Raycaster();
  mouse = new THREE.Vector2();
  

  new RGBELoader()
    .setDataType(THREE.UnsignedByteType)
    
    .setPath('static/world/')
    .load('yello4.hdr', function(texture) {

      var envMap = pmremGenerator.fromEquirectangular(texture).texture;

      scene.background = envMap;
      scene.environment = envMap;

      texture.dispose();
      pmremGenerator.dispose();

      // model

      var loader = new GLTFLoader().setPath('static/models/');
      loader.load('dem_say.glb', function(gltf) {

        gltf.scene.traverse(function(child) {

          if (child.isMesh) {

            child.material.envMap = envMap;

          }

        });

        var nft = gltf.scene;
	      nft.scale.set(0.3, 0.3, 0.3)

        mixer = new THREE.AnimationMixer( gltf.scene );
        var action = mixer.clipAction( gltf.animations[ 0 ]);
        var action_b = mixer.clipAction( gltf.animations[ 1 ]);
        // var action_c = mixer.clipAction( gltf.animations[ 2 ]);
          
        action.play();
        action_b.play();
        // action_c.play();

        scene.add(nft);
        
        render();

      });

    });

  renderer = new THREE.WebGLRenderer({
    antialias: true
  });
  renderer.setPixelRatio(window.devicePixelRatio);
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1;
  renderer.outputEncoding = THREE.sRGBEncoding;
  container.appendChild(renderer.domElement);

  var pmremGenerator = new THREE.PMREMGenerator(renderer);
  pmremGenerator.compileEquirectangularShader();

  controls = new OrbitControls(camera, renderer.domElement);
  controls.addEventListener('change', render); // use if there is no animation loop
  controls.minDistance = 2;
  controls.maxDistance = 10;
  controls.target.set(0, 0, -0.2);
  controls.update();

  window.addEventListener('resize', onWindowResize, false);

  renderer.domElement.addEventListener('click', onClick, false);

	// Alternative onclick function for mobile devices incase of raycaster not working...
  document.getElementById("funk").addEventListener('click', mClick, false);

	// when the mouse moves, call the given function
	renderer.domElement.addEventListener( 'mousemove', onMouseMove, false );

}

function mClick() {
  
  
  if (audio.paused) {
    audio.play();
    
    
  } else  {
    audio.pause();
    
  }
  
  
  // audio visualizer source code credit to Author Special Agent Squeaky (specialagentsqueaky.com) --> Thanks man!
  (function () {

    // The number of bars that should be displayed
    const NBR_OF_BARS = 40;
  
    // Get the audio element tag
    // const audio = document.querySelector('audio');
  
    // Create an audio context
    const ctx = new AudioContext();
  
    // Create an audio source
    const audioSource = ctx.createMediaElementSource(audio);
  
    // Create an audio analyzer
    const analayzer = ctx.createAnalyser();
  
    // Connect the source, to the analyzer, and then back the the context's destination
    audioSource.connect(analayzer);
    audioSource.connect(ctx.destination);
  
    // Print the analyze frequencies
    const frequencyData = new Uint8Array(analayzer.frequencyBinCount);
    analayzer.getByteFrequencyData(frequencyData);
    console.log("frequencyData", frequencyData);
  
    // Get the visualizer container
    const visualizerContainer = document.querySelector(".visualizer-container");
  
    // Create a set of pre-defined bars
    for( let i = 0; i < NBR_OF_BARS; i++ ) {
  
        const bar = document.createElement("DIV");
        bar.setAttribute("id", "bar" + i);
        bar.setAttribute("class", "visualizer-container__bar");
        visualizerContainer.appendChild(bar);
  
    }
  
    // This function has the task to adjust the bar heights according to the frequency data
    function renderFrame() {
  
        // Update our frequency data array with the latest frequency data
        analayzer.getByteFrequencyData(frequencyData);
  
        for( let i = 0; i < NBR_OF_BARS; i++ ) {
  
            // Since the frequency data array is 1024 in length, we don't want to fetch
            // the first NBR_OF_BARS of values, but try and grab frequencies over the whole spectrum
            const index = (i + 10) * 2;
            // fd is a frequency value between 0 and 255
            const fd = frequencyData[index];
  
            // Fetch the bar DIV element
            const bar = document.querySelector("#bar" + i);
            if( !bar ) {
                continue;
            }
  
            // If fd is undefined, default to 0, then make sure fd is at least 4
            // This will make make a quiet frequency at least 4px high for visual effects
            const barHeight = Math.max(2, fd || 0);
            bar.style.height = barHeight + "px";
  
        }
  
        // At the next animation frame, call ourselves
        window.requestAnimationFrame(renderFrame);
  
    }
  
    renderFrame();
  
    audio.volume = 0.10;
    audio.play();
    animate();
  })();    
}


function onClick() {

  event.preventDefault();

  mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
  mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;

  raycaster.setFromCamera(mouse, camera);

  var intersects = raycaster.intersectObjects(scene.children, true);
  
  

  if (intersects.length > 0) {

    console.log('Intersection:', intersects[0]);
    console.log('TOM TOM!');
    
    // var obj = intersects[0].object; // the object that was intersected
    // // rotate = false;
    // outlinePass.selectedObjects = obj;

    
    if (audio.paused) {
      audio.play();
    
    } else  {
      audio.pause(); 
     
    }
    
    
    
    (function () {

      // The number of bars that should be displayed
      const NBR_OF_BARS = 40;
    
      // Get the audio element tag
      // const audio = document.querySelector('audio');
    
      // Create an audio context
      const ctx = new AudioContext();
    
      // Create an audio source
      const audioSource = ctx.createMediaElementSource(audio);
    
      // Create an audio analyzer
      const analayzer = ctx.createAnalyser();
    
      // Connect the source, to the analyzer, and then back the the context's destination
      audioSource.connect(analayzer);
      audioSource.connect(ctx.destination);
    
      // Print the analyze frequencies
      const frequencyData = new Uint8Array(analayzer.frequencyBinCount);
      analayzer.getByteFrequencyData(frequencyData);
      console.log("frequencyData", frequencyData);
    
      // Get the visualizer container
      const visualizerContainer = document.querySelector(".visualizer-container");
    
      // Create a set of pre-defined bars
      for( let i = 0; i < NBR_OF_BARS; i++ ) {
    
          const bar = document.createElement("DIV");
          bar.setAttribute("id", "bar" + i);
          bar.setAttribute("class", "visualizer-container__bar");
          visualizerContainer.appendChild(bar);
    
      }
    
      // This function has the task to adjust the bar heights according to the frequency data
      function renderFrame() {
    
          // Update our frequency data array with the latest frequency data
          analayzer.getByteFrequencyData(frequencyData);
    
          for( let i = 0; i < NBR_OF_BARS; i++ ) {
    
              // Since the frequency data array is 1024 in length, we don't want to fetch
              // the first NBR_OF_BARS of values, but try and grab frequencies over the whole spectrum
              const index = (i + 10) * 2;
              // fd is a frequency value between 0 and 255
              const fd = frequencyData[index];
    
              // Fetch the bar DIV element
              const bar = document.querySelector("#bar" + i);
              if( !bar ) {
                  continue;
              }
    
              // If fd is undefined, default to 0, then make sure fd is at least 4
              // This will make make a quiet frequency at least 4px high for visual effects
              const barHeight = Math.max(2, fd || 0);
              bar.style.height = barHeight + "px";
    
          }
    
          // At the next animation frame, call ourselves
          window.requestAnimationFrame(renderFrame);
    
      }
    
      renderFrame();
    
      audio.volume = 0.10;
      audio.play();
      animate();
    
    })();


    
  } 
  
}

var audio = new Audio('static/music/dem_say.mp3');
audio.volume = 0.05;
      
function onMouseMove( event ) {

	// calculate mouse position in normalized device coordinates
	// (-1 to +1) for both components

	mouse.x = ( event.clientX / window.innerWidth ) * 2 - 1;
	mouse.y = - ( event.clientY / window.innerHeight ) * 2 + 1;

  // update the picking ray with the camera and mouse position
	raycaster.setFromCamera( mouse, camera );

	// calculate objects intersecting the picking ray
	const intersects = raycaster.intersectObjects( scene.children, true );

	for ( let i = 0; i < intersects.length; i ++ ) {

    console.log('TING!');
    
    // if there is one (or more) intersections
    if ( intersects.length > 0 )
    {
      // if the closest object intersected is not the currently stored intersection object
      if ( intersects[ 0 ].object != INTERSECTED ) 
      {
          // restore previous intersection object (if it exists) to its original color
        if ( INTERSECTED ) 
          INTERSECTED.material.color.setHex( INTERSECTED.currentHex );
        // store reference to closest object as current intersection object
        INTERSECTED = intersects[ 0 ].object;
        // store color of closest object (for later restoration)
        INTERSECTED.currentHex = INTERSECTED.material.color.getHex();
        // set a new color for closest object
        INTERSECTED.material.color.setHex( 0xffff00 );
      }
    } 
    else // there are no intersections
    {
      // restore previous intersection object (if it exists) to its original color
      if ( INTERSECTED ) 
        INTERSECTED.material.color.setHex( INTERSECTED.currentHex );
      // remove previous intersection object reference
      //     by setting current intersection object to "nothing"
      INTERSECTED = null;
    }
	}
  

  // update();
  // window.requestAnimationFrame(renderFrame);
}




function onWindowResize() {

  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();

  renderer.setSize(window.innerWidth, window.innerHeight);
  
  render();

}

// const pointLight = new THREE.PointLight(0xffffff)
// pointLight.position.set(5,5,5);

// // const ambientLight = new THREE.AmbientLight(0xffffff);
// scene.add(pointLight);

// const lightHelper = new THREE.PointLightHelper(pointLight);
// // const gridHelper = new THREE.GridHelper(200, 50);
// scene.add(lightHelper);


function render() {
  
  renderer.render(scene, camera);

}




const clock = new THREE.Clock();

function animate () {
  requestAnimationFrame( animate );

  var delta = clock.getDelta();

	if ( mixer ) mixer.update( delta );

  // if ( mixer_2 ) mixer_2.update( delta );

  // sphere1.rotation.x += 0.02
  // sphere1.rotation.y += 0.02

  controls.update ();
  
  

  renderer.render( scene, camera );
}

