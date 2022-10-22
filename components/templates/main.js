'use strict'

let WIDTH = 800, HEIGHT = WIDTH;

function drawCylinder(h, r, x, y, z) {

    let step = int(document.getElementById('n_number_of_sides').value);
    let ang = int(document.getElementById('angle').value);

	for (var fi = 0; fi < ang; fi += step) { // array of vertices
		beginShape();
		vertex(x, y + h / 2, z);
		vertex(x + cos(fi / 360 * 2 * PI) * r,
			y + h / 2,
			z + sin(fi / 360 * 2 * PI) * r);
		vertex(x + cos((fi + step) / 360 * 2 * PI) * r,
			y + h / 2,
			z + sin((fi + step) / 360 * 2 * PI) * r);
		endShape(); // соединение вершин в одну плоскость

		beginShape();
		vertex(x, y - h / 2, z);
		vertex(x + cos(fi / 360 * 2 * PI) * r,
			y - h / 2,
			z + sin(fi / 360 * 2 * PI) * r);
		vertex(x + cos((fi + step) / 360 * 2 * PI) * r,
			y - h / 2,
			z + sin((fi + step) / 360 * 2 * PI) * r);
		endShape();

		beginShape();
		vertex(x + cos(fi / 360 * 2 * PI) * r,
			y - h / 2,
			z + sin(fi / 360 * 2 * PI) * r);

		vertex(x + cos(fi / 360 * 2 * PI) * r,
			y + h / 2,
			z + sin(fi / 360 * 2 * PI) * r);

		vertex(x + cos((fi + step) / 360 * 2 * PI) * r,
			y + h / 2,
			z + sin((fi + step) / 360 * 2 * PI) * r);

		vertex(x + cos((fi + step) / 360 * 2 * PI) * r,
			y - h / 2,
			z + sin((fi + step) / 360 * 2 * PI) * r);

		endShape();
	}
}

function setup() {
	createCanvas(WIDTH, HEIGHT, WEBGL);
	background(200);
	debugMode(AXES);
}

function draw() {
	stroke(0, 0, 0);
	strokeWeight(2);
	background(300);
	ambientLight(100);

	let x1 = map(mouseX, 0, WIDTH, -200, 200);
	let x2 = map(mouseY, 0, HEIGHT, 200, -200);

	directionalLight(100, 100, 100, x1, x2, 200);
	ambientMaterial(255, 92, 122);
	orbitControl();

	drawCylinder(260, 100, 10, -20, 0);
}

// main : sketch.js *.js ; open -a Safari index.html