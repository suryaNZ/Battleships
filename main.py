from tkinter import *


# - Functions
def on_button_click_1(r, c):
    new_list = find_coords([r, c], main_frame, ships1)
    if new_list != None:
        ships1.extend(new_list)
    if len(ships1) == 13:
        main.quit()
        main.destroy()

def find_coords(main_coord, root, cur):
    global pc1, ships
    new = []

    if radio_var.get() == 0:
        if main_coord[0] + ships[pc1] > 10:
            return None

        for i in range(main_coord[0], main_coord[0] + ships[pc1]):
            if (i, main_coord[1]) in cur:
                return None
        for i in range(main_coord[0], main_coord[0] + ships[pc1]):
            Button(root, text="X", width=5, height=2, bg="yellow").grid(row=i, column=main_coord[1])
            new.append((i, main_coord[1]))

    elif radio_var.get() == 1:
        if main_coord[1] + ships[pc1] > 10:
            return None
        for i in range(main_coord[1], main_coord[1] + ships[pc1]):
            if (main_coord[0], i) in cur:
                return None
        for i in range(main_coord[1], main_coord[1] + ships[pc1]):        
            Button(root, text="X", width=5, height=2, bg="yellow").grid(row=main_coord[0], column=i)
            new.append((main_coord[0], i))
    if new:
        pc1 += 1
    return new

def on_button_click_2(r, c):
    new_list = find_coords([r, c], main_frame2, ships2)
    if new_list != None:
        ships2.extend(new_list)
    if len(ships2) == 13:
        main2.quit()
        main2.destroy()

def attacking1(r, c):
    global hit1, turn
    if not turn:
        return
    if (r, c) in ships2:
        Button(frame1, text="X", width= 5, height=2, bg="green").grid(row=r, column=c)
        hit1 += 1
        score1.configure(text=f"Score: {hit1}")
    else:
        Button(frame1, text="-", width= 5, height=2, bg="red").grid(row=r, column=c)
    if hit1 == 13:
        winner.append(player1[0])
        attacking.quit()
        attacking.destroy()
    
    turn = False

def attacking2(r, c):
    global hit2, turn
    if turn:
        return
    if (r, c) in ships1:
        Button(frame2, text="X", width= 5, height=2, bg="green").grid(row=r, column=c)
        hit2 += 1
        score2.configure(text=f"Score: {hit2}")
    else:
        Button(frame2, text="-", width= 5, height=2, bg="red").grid(row=r, column=c)
    if hit2 == 13:
        winner.append(player2[0])
        attacking.quit()
        attacking.destroy()
    turn = True

def get_input():
        player1.append(entry.get())
        player2.append(entry2.get())
        userinfo.destroy()

def on_close():
    if hit1 > hit2:
        winner.append(player1[0])
    else:
        winner.append(player2[0])
    attacking.quit()
    attacking.destroy()

# - Variables
ships = [2, 3, 3, 5]


ships1 = []
ships2 = []

hit1 = 0
hit2 = 0

player1 = []
player2 = []

winner = []

turn = True

pc1 = 0

# Loop for player info

userinfo = Tk()

label = Label(userinfo, text="Enter Player Information:", padx=10, pady=10)
label.pack()

entry = Entry(userinfo)
entry2 = Entry(userinfo)

entry.pack(pady=5)
entry2.pack(pady=5)

submit = Button(userinfo, text="Submit", command=get_input)
submit.pack()

mainloop()

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Loop for first player
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#setting up
main = Tk()
main.title("Player 1: Setting up")

main_frame = Frame(main, relief="ridge", borderwidth=2)

main_frame.pack(side="bottom", padx=10, pady=10, fill="both", expand=True)

# Radio buttons
radio_var = IntVar()

vertical = Radiobutton(main, text="Vertical", variable=radio_var, value=0)
horizontal = Radiobutton(main, text="Horizontal", variable=radio_var, value=1)

vertical.pack()
horizontal.pack()

# grid
for i in range(10):
    for j in range(10):
        btn = Button(main_frame, text="O", width= 5, height=2, command=lambda r=i, c=j: on_button_click_1(r, c)).grid(row=i, column=j)

mainloop()

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Loop for second player 
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
pc1 = 0

main2 = Tk()
main2.title("Player 2: Setting up")

main_frame2 = Frame(main2, relief="ridge", borderwidth=2)

main_frame2.pack(side="bottom", padx=10, pady=10, fill="both", expand=True)

radio_var = IntVar()

vertical2= Radiobutton(main2, text="Vertical", variable=radio_var, value=0)
horizontal2 = Radiobutton(main2, text="Horizontal", variable=radio_var, value=1)

vertical2.pack()
horizontal2.pack()

for i in range(10):
    for j in range(10):
        btn = Button(main_frame2, text="O", width=5, height=2,command=lambda r=i, c=j: on_button_click_2(r, c)).grid(row=i, column=j)

mainloop()

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Loop for attacking 
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

attacking = Tk()
attacking.title("Attacking")

attacking.protocol("WM_DELETE_WINDOW", on_close)

subt1 = Label(attacking, text=f"{player1[0]}", padx=20)
subt1.pack(side="left")

subt2 = Label(attacking, text=f"{player2[0]}", padx=20)
subt2.pack(side="right")

score1 = Label(attacking, text=f"Score: {hit1}")
score1.pack(anchor="nw")
score2 = Label(attacking, text=f"Score: {hit2}")
score2.pack(anchor="ne")

frame1 = Frame(attacking, relief="ridge", borderwidth=2)
frame2 = Frame(attacking, relief="ridge", borderwidth=2)

frame1.pack(side="left", padx=10, pady=10, fill="both", expand=True)
frame2.pack(side="right", padx=10, pady=10, fill="both", expand=True)

for i in range(10):
    for j in range(10):
        Button(frame1, text="O", width=5, height=2,command=lambda r=i, c=j: attacking1(r, c)).grid(row=i, column=j)
        Button(frame2, text="O", width=5, height=2,command=lambda r=i, c=j: attacking2(r, c)).grid(row=i, column=j)

mainloop()



winscreen = Tk()

winscreen.title("You Won!")
winscreen.geometry("500x400")

winscreen.configure(bg="green")

win_label = Label(winscreen, text=f"Congratulations! {winner[0]} won!", font=("Arial", 16), anchor="center").grid(row=10, column=10)

mainloop()