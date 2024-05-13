from tkinter import *
from tkinter import font
from random import randint, choice

# make the tkinter window
window = Tk()

# variables
# first part is a check list for starting cross color
color_list = {
    "white": IntVar(value = 1),
    "yellow": IntVar(),
    "green": IntVar(),
    "blue": IntVar(),
    "red": IntVar(),
    "orange": IntVar()
}
# counter clockwise
color_order = {
    "white": ["blue", "red", "green", "orange"],
    "yellow": ["green", "red", "blue", "orange"],
    "green": ["white", "red", "yellow", "orange"],
    "blue": ["yellow", "red", "white", "orange"],
    "red": ["blue", "yellow", "green", "white"],
    "orange": ["blue", "white", "green", "yellow"],
}

# check list for permutations
perm_list = {
    "aa": IntVar(value = 1),
    "ab": IntVar(value = 1),
    "e": IntVar(value = 1),
    "f": IntVar(value = 1),
    "ga": IntVar(value = 1),
    "gb": IntVar(value = 1),
    "gc": IntVar(value = 1),
    "gd": IntVar(value = 1),
    "h": IntVar(value = 1),
    "ja": IntVar(value = 1),
    "jb": IntVar(value = 1),
    "na": IntVar(value = 1),
    "nb": IntVar(value = 1),
    "ra": IntVar(value = 1),
    "rb": IntVar(value = 1),
    "t": IntVar(value = 1),
    "ua": IntVar(value = 1),
    "ub": IntVar(value = 1),
    "v": IntVar(value = 1),
    "y": IntVar(value = 1),
    "z": IntVar(value = 1),
}

def rotate(ll, auf):
    for i in range(0, auf * 3):
        ll.append(ll.pop(0))
    return ll

def cube_create(ll):
    for i in range(1, 4):
        cube_canvas.create_rectangle(50 * i, 50, 50 * (i + 1), 100, width = 2, fill = ll[i - 1], outline = "black")
    for i in range(4, 7):
        cube_canvas.create_rectangle(50 * i + 5, 50, 50 * (i + 1) + 5, 100, width = 2, fill = ll[i - 1], outline = "black")


# class stuff
class last_layer:
    def __init__(self):
        self.auf = randint(0, 3)
        self.start_index = randint(0,3)
        self.cross_color = choice([k for k, v in color_list.items() if v.get() == 1])

        self.c1 = color_order[self.cross_color][self.start_index % 4]
        self.c2 = color_order[self.cross_color][(self.start_index + 1) % 4]
        self.c3 = color_order[self.cross_color][(self.start_index + 2) % 4]
        self.c4 = color_order[self.cross_color][(self.start_index + 3) % 4]
        # c1 = blue
        # c2 = red
        # c3 = green
        # c4 = orange
        self.b = self.c1
        self.r = self.c2
        self.g = self.c3
        self.o = self.c4

    def aa_perm(self):
        ll = [self.c1, self.c1, self.c3, 
            self.c4, self.c2, self.c1,
            self.c2, self.c3, self.c2,
            self.c3, self.c4, self.c4]
        ll = rotate(ll, self.auf)
        cube_create(ll)

    def ab_perm(self):
        ll = [self.c1, self.c1, self.c2, 
            self.c3, self.c2, self.c3,
            self.c4, self.c3, self.c1,
            self.c2, self.c4, self.c4]
        ll = rotate(ll, self.auf)
        cube_create(ll)

    def e_perm(self):
        ll = [self.c2, self.c1, self.c4, 
            self.c1, self.c2, self.c3,
            self.c4, self.c3, self.c2,
            self.c3, self.c4, self.c1]
        ll = rotate(ll, self.auf)
        cube_create(ll)

    def f_perm(self):
        ll = [self.c4, self.c4, self.c4, 
            self.c1, self.c3, self.c2,
            self.c3, self.c2, self.c1,
            self.c2, self.c1, self.c3]
        ll = rotate(ll, self.auf)
        cube_create(ll)
        
    def ga_perm(self):
        ll = [self.b, self.r, self.r,
              self.g, self.o, self.b,
              self.r, self.b, self.g,
              self.o, self.g, self.o]
        ll = rotate(ll, self.auf)
        cube_create(ll)

    def gb_perm(self):
        ll = [self.b, self.g, self.r,
              self.g, self.b, self.b,
              self.r, self.o, self.g,
              self.o, self.r, self.o]
        ll = rotate(ll, self.auf)
        cube_create(ll) 

    def gc_perm(self):
        ll = [self.b, self.g, self.r,
              self.g, self.o, self.b,
              self.r, self.r, self.g,
              self.o, self.b, self.o]
        ll = rotate(ll, self.auf)
        cube_create(ll)   

    def gd_perm(self):
        ll = [self.b, self.o, self.r,
              self.g, self.g, self.b,
              self.r, self.b, self.g,
              self.o, self.r, self.o]
        ll = rotate(ll, self.auf)
        cube_create(ll)

    def h_perm(self):
        ll = [self.b, self.g, self.b, 
              self.r, self.o, self.r,
              self.g, self.b, self.g,
              self.o, self.r, self.o]
        ll = rotate(ll, self.auf)
        cube_create(ll)
    
    def ja_perm(self):
        ll = [self.o, self.o, self.b,
              self.r, self.r, self.r,
              self.g, self.g, self.o, 
              self.b, self.b, self.g]
        ll = rotate(ll, self.auf)
        cube_create(ll)
    
    def jb_perm(self):
        ll = [self.b, self.r, self.r,
              self.g, self.b, self.b,
              self.r, self.g, self.g,
              self.o, self.o, self.o]
        ll = rotate(ll, self.auf)
        cube_create(ll)

    def na_perm(self):
        ll = [self.r, self.o, self.o,
              self.b, self.g, self.g,
              self.o, self.r, self.r, 
              self.g, self.b, self.b]
        ll = rotate(ll, self.auf)
        cube_create(ll)

    def nb_perm(self):
        ll = [self.r, self.r, self.o,
              self.b, self.b, self.g,
              self.o, self.o, self.r, 
              self.g, self.g, self.b]
        ll = rotate(ll, self.auf)
        cube_create(ll)

    def ra_perm(self):
        ll = [self.r, self.b, self.r,
              self.g, self.g, self.o,
              self.b, self.o, self.g,
              self.o, self.r, self.b]
        ll = rotate(ll, self.auf)
        cube_create(ll)

    def rb_perm(self):
        ll = [self.o, self.b, self.o,
              self.b, self.o, self.r,
              self.g, self.r, self.b,
              self.r, self.g, self.g]
        ll = rotate(ll, self.auf)
        cube_create(ll)
    
    def t_perm(self):
        ll = [self.b, self.b, self.r, 
              self.g, self.o, self.b,
              self.r, self.g, self.g,
              self.o, self.r, self.o]
        ll = rotate(ll, self.auf)
        cube_create(ll)

    def ua_perm(self):
        ll = [self.b, self.b, self.b, 
              self.r, self.g, self.r, 
              self.g, self.o, self.g, 
              self.o, self.r, self.o]
        ll = rotate(ll, self.auf)
        cube_create(ll)
    
    def ub_perm(self):
        ll = [self.b, self.b, self.b, 
              self.r, self.o, self.r, 
              self.g, self.r, self.g, 
              self.o, self.g, self.o]
        ll = rotate(ll, self.auf)
        cube_create(ll)

    def v_perm(self):
        ll = [self.o, self.o, self.r, 
              self.g, self.r, self.b, 
              self.r, self.b, self.o, 
              self.b, self.g, self.g]
        ll = rotate(ll, self.auf)
        cube_create(ll)

    def y_perm(self):
        ll = [self.b, self.b, self.g, 
              self.o, self.r, self.r, 
              self.g, self.o, self.b,
              self.r, self.g, self.o]
        ll = rotate(ll, self.auf)
        cube_create(ll)

    def z_perm(self):
        ll = [self.g, self.o, self.g, 
              self.o, self.g, self.o, 
              self.b, self.r, self.b, 
              self.r, self.b, self.r]
        ll = rotate(ll, self.auf)
        cube_create(ll)

    def __str__(self):
        return "auf: " + str(self.auf) + " cc: " + self.cross_color

# funtion stuff
def pick_perm():
    choices = [k for k, v in perm_list.items() if v.get() >= 1]  
    if(len(choices) == 0):
        print("DONE!")
        return
    perm = choice(choices)
    
    ll = last_layer()
    match perm:
        case "aa": ll.aa_perm()
        case "ab": ll.ab_perm()
        case "e": ll.e_perm()
        case "f": ll.f_perm()
        case "ga": ll.ga_perm()
        case "gb": ll.gb_perm()
        case "gc": ll.gc_perm()
        case "gd": ll.gd_perm()
        case "h": ll.h_perm()
        case "ja": ll.ja_perm()
        case "jb": ll.jb_perm()
        case "na": ll.na_perm()
        case "nb": ll.nb_perm()
        case "ra": ll.ra_perm()
        case "rb": ll.rb_perm()
        case "t": ll.t_perm()
        case "ua": ll.ua_perm()
        case "ub": ll.ub_perm()
        case "v": ll.v_perm()
        case "y": ll.y_perm()
        case "z": ll.z_perm()
    answer.set(perm)

# get user guess, which is a StringVar and determine correctness
def get_guess():
    if(user_guess.get() == answer.get()):
        print("correct")
        # perm_list[answer.get()] = perm_list[answer.get()] - 1
    else:
        print("incorrect")
        # perm_list[answer.get()] = perm_list[answer.get()] + 1
    input_box.delete(0, len(user_guess.get()))
    pick_perm()
def get_guess_return(event):
    if(user_guess.get() == answer.get()):
        print("correct")
        # perm_list[answer.get()] = perm_list[answer.get()] - 1
    else:
        print("incorrect")
        # perm_list[answer.get() style={borderBottomColor="white"}] = perm_list[answer.get()] + 1
    input_box.delete(0, len(user_guess.get()))
    pick_perm()

# title the window and make it so it is square (grid)
window.title("PLL Recognition Trainer")
window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(1, minsize=500, weight=1)
# Font Config stuff
# defaultFont = font.nametofont("TkDefaultFont")
# defaultFont.configure(family="", size = 10, weight=font.NORMAL)

# the right side of the window is the canvas, in column 1
cube_canvas = Canvas(window, bg = "white")
cube_canvas.grid(row = 0, column = 1, sticky = "nsew")

# make the space on the left for the various options (bd is border width)
frame_left = Frame(window, relief = RAISED, bd = 2)

# make the space on the right side of the window for the next button
frame_right = Frame(window, relief = RAISED, bd = 2)

# make the answer entry box at the bottom of the window
frame_text = Frame(window, relief = RAISED, bd = 2)

# create the user guess and answer StringVars
user_guess = StringVar()
answer = StringVar()

# create and add the check list for cross colors to the left menu
for i, k in enumerate(color_list):
    check = Checkbutton(frame_left, text = k, variable = color_list[k], cursor = "hand2")
    check.grid(row = i, column = 0, sticky = "W", padx = 5)

# The button for skipping the current perm
button_start = Button(frame_right, text = "Next", command = pick_perm, cursor = "hand2")
button_start.grid(row = 0, column = 0, sticky = "e", padx = 5)

# the box where the user enters their guess
input_box = Entry(frame_text, textvariable = user_guess, relief = FLAT)
input_box.bind("<Return>", get_guess_return)
input_box.grid(row = 0, column = 0, sticky = "nsew")

# enter button for user answer, clears the input box and picks new perm
input_enter = Button(frame_text, text = "Enter", cursor = "hand2", command = get_guess)
input_enter.grid(row = 0, column = 1, sticky = "s")

# place frames
frame_left.grid(row = 0, column = 0, sticky = "ns")
frame_right.grid(row = 0, column = 2, sticky = "nse")
frame_text.grid(row = 1, column = 1, columnspan = 4, sticky = "s")

# cube_canvas.create_polygon(700, 700,
#  d                           width = 2, fill = "blue", outline = "black")

pick_perm()
window.mainloop()