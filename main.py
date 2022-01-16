import turtle, pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# to get coordinates of each state
# def get_mouse_click_cor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_cor)
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 State", prompt="What is another state's name ?").title()

    data = pandas.read_csv("50_states.csv")
    states = data.state.to_list()

    if answer == "Exit":
        unknown_states = []
        for i in states:
            if i not in guessed_states:
                unknown_states.append(i)

        x = pandas.DataFrame(unknown_states)
        x.to_csv("unknown States")

        break

    if answer in states and answer not in guessed_states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        d = data[data.state == answer]
        t.goto(int(d.x),int(d.y))
        t.write(answer)



# turtle.mainloop()
