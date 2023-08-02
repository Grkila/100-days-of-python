import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape( image)
turtle.shape(image)

states=pandas.read_csv("50_states.csv")

number_of_states=len(states)
guessed_states=0
guessed_states_list=[]
missing_states=[]
while number_of_states>guessed_states:
    answer_state = screen.textinput(title="Guess the State", prompt="What is another states name")

    if answer_state =="Exit":
        for state in states.state.to_list():
            if state not in guessed_states_list:
                missing_states.append(state)
        new_data= pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if (states['state'].eq(answer_state)).any():
        jimmy=turtle.Turtle()
        jimmy.hideturtle()
        jimmy.penup()
        x_cor=states[states.state==answer_state].x
        y_cor=states[states.state==answer_state].y
        jimmy.goto(int(x_cor),int(y_cor))
        jimmy.write(answer_state)
        guessed_states_list.append(answer_state)






