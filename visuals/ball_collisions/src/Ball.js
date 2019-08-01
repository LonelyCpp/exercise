class Ball {
  constructor(x, y, radius) {
    this.radius = radius;
    this.body = Matter.Bodies.circle(x, y, radius, {
      friction: 0.2,
      restitution: 0.8,
      frictionAir: 0
    });
  }

  draw = () => {
    circle(this.body.position.x, this.body.position.y, this.radius * 2);
  };

  pushLeft = magnitude => {
    const force = Matter.Vector.create(-magnitude * 0.01, 0);
    Matter.Body.applyForce(this.body, this.body.position, force);
  };

  pushRight = magnitude => {
    const force = Matter.Vector.create(magnitude * 0.01, 0);
    Matter.Body.applyForce(this.body, this.body.position, force);
  };

  pushUp = magnitude => {
    const force = Matter.Vector.create(0, -magnitude * 0.01);
    Matter.Body.applyForce(this.body, this.body.position, force);
  };
  pushDown = magnitude => {
    const force = Matter.Vector.create(0, magnitude * 0.01);
    Matter.Body.applyForce(this.body, this.body.position, force);
  };
}
