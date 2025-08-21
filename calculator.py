import tkinter

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values) # 5
column_count = len(button_values[0]) # 4

color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "white"

#window setup 
window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text = "0", font=("Arial, 45"), background=color_black, foreground=color_white, anchor="e") #anschor = e , east side floating

label.grid(row=0,column=0, columnspan=column_count, sticky="we" ) #we means west to east stretch

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30),
                             width= column_count-1, height=1,
                             command= lambda value=value: button_clicked(value))
        
        if value in top_symbols:
            button.config(foreground=color_black, background=color_light_gray)
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_orange)
        else:
            button.config(foreground=color_white, background=color_dark_gray)

        button.grid(row = row+1, column=column)


frame.pack()

#a+b, a-b, a*b, a/b

A = "0"
operator = None
B = None

def button_clicked(value):
    global right_symbols, top_symbols, A, B, operator

    if value in right_symbols:
        pass 
    elif value in top_symbols:
        pass
    else: #digits or 
        if value == ".":
            pass
        elif value == "0123456789":
            if label["text"] == "0":
                label["text"] = value #replace 0
            else:
                label["text"] += value #append digit


window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width - window_width) / 2)
window_y = int((screen_height - window_height) / 2)

#format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()


 