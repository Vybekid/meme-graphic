import turtle
import time

screen = turtle.Screen()
screen.bgcolor("#16E60F")
screen.title("Plane Collision Animation")

plane1_frames = ["Plane 1/plane 1, 1.gif", "Plane 1/plane 1, 2.gif", "Plane 1/plane 1, 3.gif"]
plane2_frames = ["Plane 2/plane 2, 1.gif", "Plane 2/plane 2, 2.gif", "Plane 2/plane 2, 3.gif"]
blow_frames = ["blow/blow 1.gif", "blow/blow 2.gif"]

for frame in plane1_frames + plane2_frames + blow_frames:
    screen.addshape(frame)


plane1 = turtle.Turtle()
plane1.penup()
plane1.speed("fastest")

plane1.setposition(screen.window_width() // 2, 0)
plane1.setheading(180)  

plane2 = turtle.Turtle()
plane2.penup()
plane2.speed("fastest")

plane2.setposition(-screen.window_width() // 2, 0)

explosion = turtle.Turtle()
explosion.hideturtle()
explosion.speed("fastest")

frame_index = 0

while plane1.xcor() > plane2.xcor() + 20:

    plane1.shape(plane1_frames[frame_index % len(plane1_frames)])
    plane1.forward(20)

    plane2.shape(plane2_frames[frame_index % len(plane2_frames)])
    plane2.forward(20)

    frame_index += 1
    screen.update()
    time.sleep(0.1)

plane1.hideturtle()
plane2.hideturtle()

explosion.setposition(plane2.xcor(), plane2.ycor())
explosion.showturtle()

for frame in blow_frames * 3: 
    explosion.shape(frame)
    screen.update()
    time.sleep(0.2)

explosion.hideturtle()

turtle.done()