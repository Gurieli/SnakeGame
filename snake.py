from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

starting_pos = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for positions in starting_pos:
            self.add_segment(positions)

    def add_segment(self, position):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.speed("fastest")
        tim.goto(position)
        self.snake.append(tim)

    def extend(self):
        # adds new segment to the file
        self.add_segment(self.snake[-1].position())

    def move(self, number=20):
        for num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[num - 1].xcor()
            new_y = self.snake[num - 1].ycor()
            self.snake[num].goto(new_x, new_y)
        self.head.forward(number)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.move(11)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.move(11)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.move(11)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.move(11)

    def reset(self):
        for part in self.snake:
            part.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
