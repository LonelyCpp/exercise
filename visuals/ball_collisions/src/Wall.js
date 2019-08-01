class Wall {
  constructor(x, y, width, height) {
    this.width = width;
    this.height = height;
    this.body = Matter.Bodies.rectangle(x, y, width, height, {
      isStatic: true,
      friction: 0,
      frictionStatic: 0
    });
    console.log(this.body);
  }
  draw = () => {
    rect(
      this.body.vertices[0].x,
      this.body.vertices[0].y,
      this.width,
      this.height
    );
  };
}
