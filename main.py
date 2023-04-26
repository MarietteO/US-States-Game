import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
map_img = turtle.Turtle()
map_img.shape(image)
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

game_is_on = True
list_of_answers = []
score = 0

while game_is_on:
    user_answer = screen.textinput(title=f"{score}/50 States Correct", prompt="Name a US state").title()
    dataframe = pd.read_csv("50_states.csv")
    list_of_states = dataframe["state"].tolist()
    list_of_x_coors = dataframe["x"].tolist()
    list_of_y_coors = dataframe["y"].tolist()

    if user_answer in list_of_states:
        position = list_of_states.index(user_answer)
        x_cor = list_of_x_coors[position]
        y_cor = list_of_y_coors[position]
        coordinates = (x_cor, y_cor)
        pen.goto(coordinates)
        pen.write(user_answer, True, align="center", font=("Arial", 8, "normal"))
        list_of_answers.append(user_answer)
        for answer in list_of_answers:
            score += 1


screen.exitonclick()
