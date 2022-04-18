import * as THREE from "https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.module.min.js";

// Scene
const scene = new THREE.Scene();

// Add a cube to the scene
const geometry = new THREE.BoxGeometry(5, 0.5, 3); // width, height, depth
const material = new THREE.MeshLambertMaterial({ color: 0x0000ff });
const mesh = new THREE.Mesh(geometry, material);
mesh.position.set(0, 0, 0);
mesh.rotation.set(radToDeg(0), 0, 0);
scene.add(mesh);

// Set up lights
const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
scene.add(ambientLight);

const directionalLight = new THREE.DirectionalLight(0xffffff, 0.6);
directionalLight.position.set(10, 20, 0); // x, y, z
scene.add(directionalLight);

// Camera
const width = 10;
const height = width * (window.innerHeight / window.innerWidth);
const camera = new THREE.OrthographicCamera(
  width / -2, // left
  width / 2, // right
  height / 2, // top
  height / -2, // bottom
  1, // near
  100 // far
);

camera.position.set(1, 1, 10);
camera.lookAt(0, 0, 0);

// Renderer
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.render(scene, camera);

// Add it to HTML
document.body.appendChild(renderer.domElement);

$(document).ready(() => {
    reload();
})

function reload() {
    let data = getData();
    update(data["data"][0], 0, data["data"][1]);
    setTimeout(function() {
        reload();
    }, 66); //15 Hz
}

function getData() {
    let result = null;
    $.ajax({
        async: false,
        type: 'GET',
        url: 'http://192.168.1.184:5000/get-data/',
        success: function(data) {
            result = data
        }
    });
    return result;
}

function update(x, y, z) {
    mesh.rotation.set(radToDeg(x), radToDeg(y), radToDeg(z));
    renderer.render(scene, camera);
}

function radToDeg(rad) {
    return (rad / 180) * Math.PI
}
