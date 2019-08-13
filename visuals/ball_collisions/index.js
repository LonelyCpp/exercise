// module aliases
const Engine = Matter.Engine,
  World = Matter.World,
  Bodies = Matter.Bodies;

// create an engine
const engine = Engine.create();

const bodies = [];
const constraints = [];

var wallLeft = new Wall(0, 0, 60, 1200);
var wallRight = new Wall(800, 0, 60, 1200);
var ground = new Wall(400, 610, 860, 60);
var ceiling = new Wall(400, 0, 810, 60);

bodies.push(wallLeft, wallRight, ground, ceiling);

for (let i = 0; i < 100; i++) {
  let t = new Ball(Math.random() * 100 + 300, Math.random() * 100 + 300, 10);
  t.pushLeft(Math.random() * 2);
  t.pushUp(Math.random() * 2);
  t.pushRight(Math.random() * 2);
  t.pushDown(Math.random() * 2);
  bodies.push(t);
}

let pendulumBall1 = new Ball(100, 100, 10);
let pendulumBall2 = new Ball(200, 200, 10);
pendulumBall1.body.mass = 100;
pendulumBall2.body.mass = 100;
bodies.push(pendulumBall1);
bodies.push(pendulumBall2);
constraints.push(
  new Matter.Constraint.create({
    bodyA: pendulumBall1.body,
    bodyB: ceiling.body,
    length: 200,
    stiffness: 1,
    damping: 1
  })
);
constraints.push(
  new Matter.Constraint.create({
    bodyA: pendulumBall1.body,
    bodyB: pendulumBall2.body,
    length: 200,
    stiffness: 1,
    damping: 1
  })
);

// add all of the bodies to the world
World.add(engine.world, bodies.map(item => item.body));
World.add(engine.world, constraints);

// run the engine
Engine.run(engine);

document.addEventListener(
  'keydown',
  event => {
    const keyName = event.key;

    if (keyName === 'Control') {
      // do not alert when only Control key is pressed.
      return;
    }

    if (event.ctrlKey) {
      // Even though event.key is not 'Control' (e.g., 'a' is pressed),
      // event.ctrlKey may be true if Ctrl key is pressed at the same time.
      console.log(`Combination of ctrlKey + ${keyName}`);
    } else {
      console.log(`Key pressed ${keyName}`);
      switch (keyName) {
        case 'ArrowLeft':
          bodies.forEach(item => {
            if (!item.body.isStatic) {
              item.pushLeft(Math.random() * 2);
            }
          });
          break;
        case 'ArrowRight':
          bodies.forEach(item => {
            if (!item.body.isStatic) {
              item.pushRight(Math.random() * 2);
            }
          });
          break;
        case 'ArrowUp':
          bodies.forEach(item => {
            if (!item.body.isStatic) {
              item.pushUp(Math.random() * 2);
            }
          });
          break;
      }
    }
  },
  false
);

function setup() {
  createCanvas(810, 610);
  background(100);
}

function draw() {
  background(100);
  stroke(255);
  bodies.forEach(body => {
    body.draw();
  });

  // var wallLeft = new Wall(0, 0, 60, 1200);
  constraints.forEach(constraint => {
    line(
      constraint.bodyA.position.x,
      constraint.bodyA.position.y,
      constraint.bodyB.position.x,
      constraint.bodyB.position.y
    );
  });
}
