from tkinter import *
import random

class BattleShips:

    def __init__(self):
        # - Variables
        self.ships = [2, 3, 3, 5]

        self.troll = False

        self.ships1 = []
        self.ships2 = []

        self.hit1 = 0
        self.hit2 = 0

        self.player1 = []
        self.player2 = []

        self.winner = []

        self.turn = True

        self.pc1 = 0
# - Functions
    def on_button_click_1(self, r, c):
        new_list = self.find_coords([r, c], self.main_frame, self.ships1)
        if new_list != None:
            self.ships1.extend(new_list)
        if len(self.ships1) == 13:
            self.main.quit()
            self.main.destroy()

    def find_coords(self, main_coord, root, cur):
        new = []

        if self.radio_var.get() == 0:
            if main_coord[0] + self.ships[self.pc1] > 10:
                return None

            for i in range(main_coord[0], main_coord[0] + self.ships[self.pc1]):
                if (i, main_coord[1]) in cur:
                    return None
            for i in range(main_coord[0], main_coord[0] + self.ships[self.pc1]):
                Button(root, text="X", width=5, height=2, bg="yellow").grid(row=i, column=main_coord[1])
                new.append((i, main_coord[1]))

        elif self.radio_var.get() == 1:
            if main_coord[1] + self.ships[self.pc1] > 10:
                return None
            for i in range(main_coord[1], main_coord[1] + self.ships[self.pc1]):
                if (main_coord[0], i) in cur:
                    return None
            for i in range(main_coord[1], main_coord[1] + self.ships[self.pc1]):        
                Button(root, text="X", width=5, height=2, bg="yellow").grid(row=main_coord[0], column=i)
                new.append((main_coord[0], i))
        if new:
            self.pc1 += 1
        return new

    def on_button_click_2(self, r, c):
        new_list = self.find_coords([r, c], self.main_frame2, self.ships2)
        if new_list != None:
            self.ships2.extend(new_list)
        if len(self.ships2) == 13:
            self.main2.quit()
            self.main2.destroy()

    def attacking1(self, r, c):
        if not self.turn:
            return
        if (r, c) in self.ships2:
            Button(self.frame1, text="X", width= 5, height=2, bg="green").grid(row=r, column=c)
            self.hit1 += 1
            self.score1.configure(text=f"Score: {self.hit1}")
        else:
            Button(self.frame1, text="-", width= 5, height=2, bg="red").grid(row=r, column=c)
        if self.hit1 == 13:
            self.winner.append(self.player1[0])
            self.attacking.quit()
            self.attacking.destroy()
        
        self.turn = False

    def attacking2(self, r, c):
        if self.turn:
            return
        if (r, c) in self.ships1:
            Button(self.frame2, text="X", width= 5, height=2, bg="green").grid(row=r, column=c)
            self.hit2 += 1
            self.score2.configure(text=f"Score: {self.hit2}")
        else:
            Button(self.frame2, text="-", width= 5, height=2, bg="red").grid(row=r, column=c)
        if self.hit2 == 13:
            self.winner.append(self.player2[0])
            self.attacking.quit()
            self.attacking.destroy()
        self.turn = True

    def get_input(self):
            self.player1.append(self.entry.get())
            self.player2.append(self.entry2.get())
            self.userinfo.destroy()

    def on_close(self):
        if self.hit1 > self.hit2:
            self.winner.append(self.player1[0])
        elif self.hit2 > self.hit1:
            self.winner.append(self.player2[0])
        else:
            self.winner.append("Draw")
        self.attacking.quit()
        self.attacking.destroy()

    def on_close_2(self):
        window = random.choices(["lajshasd", "Asdasjhdad", "asldhasld", "asdhaskdh", "akjhsdkajhd", "lasjdh"])
        window = Tk()
        window.geometry("4000x4000")    
        return

    def on_complete_loss(self):
        root = Tk()
        root.geometry("4000x4000")

        root.protocol("WM_DELETE_WINDOW", self.on_close_2)

    def run(self):
        # Loop for player info

        self.userinfo = Tk()

        label = Label(self.userinfo, text="Enter Player Information:", padx=10, pady=10)
        label.pack()

        self.entry = Entry(self.userinfo)
        self.entry2 = Entry(self.userinfo)

        self.entry.pack(pady=5)
        self.entry2.pack(pady=5)

        submit = Button(self.userinfo, text="Submit", command=self.get_input)
        submit.pack()

        mainloop()

        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        # Loop for first player
        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

        #setting up
        self.main = Tk()
        self.main.title("Player 1: Setting up")

        self.main_frame = Frame(self.main, relief="ridge", borderwidth=2)

        self.main_frame.pack(side="bottom", padx=10, pady=10, fill="both", expand=True)

        # Radio buttons
        self.radio_var = IntVar()

        vertical = Radiobutton(self.main, text="Vertical", variable=self.radio_var, value=0)
        horizontal = Radiobutton(self.main, text="Horizontal", variable=self.radio_var, value=1)

        vertical.pack()
        horizontal.pack()

        # grid
        for i in range(10):
            for j in range(10):
                btn = Button(self.main_frame, text="O", width= 5, height=2, command=lambda r=i, c=j: self.on_button_click_1(r, c)).grid(row=i, column=j)

        mainloop()

        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        # Loop for second player 
        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.pc1 = 0

        self.main2 = Tk()
        self.main2.title("Player 2: Setting up")

        self.main_frame2 = Frame(self.main2, relief="ridge", borderwidth=2)

        self.main_frame2.pack(side="bottom", padx=10, pady=10, fill="both", expand=True)

        self.radio_var = IntVar()

        vertical2= Radiobutton(self.main2, text="Vertical", variable=self.radio_var, value=0)
        horizontal2 = Radiobutton(self.main2, text="Horizontal", variable=self.radio_var, value=1)

        vertical2.pack()
        horizontal2.pack()

        for i in range(10):
            for j in range(10):
                btn = Button(self.main_frame2, text="O", width=5, height=2,command=lambda r=i, c=j: self.on_button_click_2(r, c)).grid(row=i, column=j)

        mainloop()

        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        # Loop for attacking 
        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

        self.attacking = Tk()
        self.attacking.title("Attacking")

        self.attacking.protocol("WM_DELETE_WINDOW", self.on_close)

        subt1 = Label(self.attacking, text=f"{self.player1[0]}", padx=20)
        subt1.pack(side="left")

        subt2 = Label(self.attacking, text=f"{self.player2[0]}", padx=20)
        subt2.pack(side="right")

        self.score1 = Label(self.attacking, text=f"Score: {self.hit1}")
        self.score1.pack(anchor="nw")
        self.score2 = Label(self.attacking, text=f"Score: {self.hit2}")
        self.score2.pack(anchor="ne")

        self.frame1 = Frame(self.attacking, relief="ridge", borderwidth=2)
        self.frame2 = Frame(self.attacking, relief="ridge", borderwidth=2)

        self.frame1.pack(side="left", padx=10, pady=10, fill="both", expand=True)
        self.frame2.pack(side="right", padx=10, pady=10, fill="both", expand=True)

        for i in range(10):
            for j in range(10):
                Button(self.frame1, text="O", width=5, height=2,command=lambda r=i, c=j: self.attacking1(r, c)).grid(row=i, column=j)
                Button(self.frame2, text="O", width=5, height=2,command=lambda r=i, c=j: self.attacking2(r, c)).grid(row=i, column=j)

        mainloop()

        if self.troll:
            if self.hit1 or self.hit2 == 0:
                self.on_complete_loss()

        winscreen = Tk()

        winscreen.title("You Won!")
        winscreen.geometry("500x400")

        winscreen.configure(bg="green")

        if self.winner[0] != "Draw":
            win_label = Label(winscreen, text=f"Congratulations! {self.winner[0]} won!", font=("Arial", 16), anchor="center")
        else:
            win_label = Label(winscreen, text=f"The game ended in a draw!", font=("Arial", 16), anchor="center")
        win_label.pack()
        mainloop()
    
engine = BattleShips()
engine.run()