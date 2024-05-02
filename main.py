import struct
from turtle import Turtle, Screen
import pandas as p

t = Turtle()
screen = Screen()
data = p.read_csv("50_states.csv")

#Screen
image = "blank_states_img.gif"
screen.addshape(image)
name = Turtle()
t.shape(image)
screen.title("Guess the state.")

#Lists
states_list = data["state"].to_list()
state_cords_x = data["x"].to_list()
state_cords_y = data["y"].to_list()
correct_guesses = []


def write_name(index):
    name.hideturtle()
    name.penup()
    name.goto(int(state_cords_x[index]), int(state_cords_y[index]))
    name.write(states_list[index])


while len(correct_guesses) < 50:
    guess = screen.textinput(title=f"{len(correct_guesses)}/{len(states_list)} States Correct.",
                             prompt="Type name of the state:").title()

    if guess == "Exit":
        states_to_learn = [x for x in states_list if x not in correct_guesses]
        data_dict = {
            "States to learn": states_to_learn
        }
        p.DataFrame(data_dict).to_csv("states_to_learn")
        break

    if guess in states_list:
        correct_guesses.append(guess)
        state_index = states_list.index(guess)
        write_name(state_index)
        print(correct_guesses)

    else:
        pass

#States to learn
