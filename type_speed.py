from tkinter import *
from tkinter import messagebox
from timeit import default_timer as timer
import random

def create_gui():
    '''Create the basic layout of the application'''
    global root
    root = Tk()
    root.title('Typing Speed Test')
    root.iconbitmap('logo.ico')
    width = root.winfo_screenmmwidth()
    height = root.winfo_screenheight()
    #set the width of the app
    root.geometry(f'{width}x{height}')
    
    heading = Label(root, text='Check Your Tying Speed', font='arial 30 bold underline')
    heading.grid(row=0, column=0, columnspan=3)
    for _ in range(2): root.columnconfigure(_, weight=1)
    display_label()
    display_text_box()
    root.mainloop()

def display_label():
    '''Display the  text that is to be typed by the user'''

    global text
    words = ['''In the United States, most e-bomb research has been carried out at the Air Force Research Laboratory at Kirtland AirForce Base in New Mexico, where researchers have been exploring the use of high power microwaves (HPM). Although the devices themselves may be relatively uncomplicated to manufacture  (Popular Mechanics illustrated a simple design in September 2001), their usage poses a number of problems.''',
            '''Kissflow has successfully created a Great Place to Work FOR ALL their employees as they have excelled on the 5 dimensions that are a hallmark of a High-Trust, High-Performance Culture™ – Credibility, Respect,  Fairness, Pride and Camaraderie. Great Place to Work® is considered the ‘Gold Standard’ in workplace culture assessment and recognition. As a certified organization, Kissflow became eligible to be considered among 'India's Best Workplaces in IT & IT-BPM 2020' – a list that features the 'Best of the Best.'''
        ]

    text = words[random.randint(0,1)]
    # set the stringvar to text_label
    label_text = StringVar()
    label_text.set(text)

    text_label = Label(root, textvar= label_text, font='arial 19', justify=LEFT, relief=RAISED, bg='skyblue', fg='black', wraplength=1200,bd=5)
    text_label.grid(row=1, column=0,columnspan=2, ipadx=30, ipady=30, pady=(30, 20))

def display_text_box():
    '''display the textbox in which the user can type'''
    global text_box 
    #create the text box
    textbox_header = Label(root, text="Start Typing", font='arial 20 bold')
    textbox_header.grid(row=2, column=0, sticky='ew', columnspan=2)

    text_box = Text(root, font='arial 19', fg='black', bg='skyblue', width=90, height=10)
    text_box.grid(row=3, column=0, columnspan=2)
    #bind the click event to text_box to calculate start_time
    text_box.bind('<Key>', started_typing)

    reset = Button(root, text='Reset', font='arial 12', bg='orange', fg='black', command=clear_text)
    reset.grid(row=4, column=0, pady=10)
    submit_button = Button(root, text='Submit', font='arial 12', bg='orange', fg='black', command=calc_time)
    submit_button.grid(row=4, column=1, pady=10)

def started_typing(event):
    '''to store the start time'''
    global already, start

    if already: pass
    else:
        start = timer()    
        already = True

def calc_time():
    '''calculate the time required for typing the text'''
    end = timer()
    #get words
    words = text_box.get('1.0', 'end')
    if len(words) != len(text) + 1:
        messagebox.showerror('Error', 'Check the errors', parent=root)
        return

    no_of_words = len([word for word in words.split(' ') if len(word)>2])
    time = end - start
    wpm = round((no_of_words)/(time/60))
    #create the popup window to show the results
    top_window = Toplevel(root)

    score_header = Label(top_window, text='Score', font='arial 50 bold', justify=LEFT, relief=RAISED, bg='blue', fg='white')
    score_header.grid(row=0, column=0, sticky='ew', columnspan=2)

    time_label = Label(top_window, text=f'Speed: {round(wpm)}', font='arial 35 bold', justify=LEFT)
    time_label.grid(row=1, column=0, sticky='ew', columnspan=2)

    #get the high score from the file
    with open('high_score.txt', 'r') as file:
        score  = int(file.readlines()[0])

    with open('high_score.txt', 'w') as file:
        if score < wpm:
            file.truncate(0)
            file.write(str(wpm))
            score = wpm

    score_header = Label(top_window, text='High Score', font='arial 50 bold', justify=LEFT, relief=RAISED, bg='green', fg='white')
    score_header.grid(row=2, column=0, sticky='ew', columnspan=2)

    highscore_label = Label(top_window, text="Speed: {}".format(score), font='arial 35 bold', justify=LEFT)
    highscore_label.grid(row=3, column=0, sticky='ew', columnspan=2)

    for _ in range(1): top_window.columnconfigure(_, weight=1)

def clear_text():
    '''clear the text of text_box and reset the timer'''
    global start
    text_box.delete('1.0', 'end')
    start = timer()

if __name__ == '__main__':
    already = False
    create_gui()

