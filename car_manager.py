from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_cars(self):
        min_distance = 40
        random_chance=random.randint(1,6)
        new_y = random.randint(-250, 250)
        if random_chance == 1:
            for car in self.cars:
                if abs(car.ycor() - new_y) < min_distance and abs(car.xcor() - 380) < 20:
                    # cars will not be overlapped to each other
                    return
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.setheading(180)
            car.goto(380,new_y)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed+=5