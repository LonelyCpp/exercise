class Wall {
  constructor(x, y, width, height) {
    this.body = Matter.Bodies.rectangle(x, y, width, height, {
      isStatic: true,
      friction: 0,
      frictionStatic: 0
    });
  }
}
