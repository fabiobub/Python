import turtle

#Screen setup
screen = turtle.Screen()
screen.title("U.S. States")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)



answer_state = screen.textinput(title="Guess the State", prompt="What is another state name?")


screen.exitonclick()