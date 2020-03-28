let letters;

function preload() {
    letters = loadJSON('\letters.json');
}

function setup() {
    createCanvas(windowWidth, windowHeight);
    noLoop();
}

function draw() {
    background(0);
    fill(255);
    beginShape();
    let letter = letters.h;
    for(let i=0; i<letter.length; i++) {
        v = letter[i];
        console.log(i+":", v);
        vertex(v.x, v.y);
    }
    endShape(CLOSE);
}