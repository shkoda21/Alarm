from datetime import datetime
from playsound import playsound
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox


def alarm(set_time):
    if len(set_time) != 8:
        messagebox.showinfo('Error', "Incorrect time format, try again")
    else:
        if int(set_time[0:2]) > 23:
            messagebox.showinfo('Error', "Incorrect hours, try again")
        elif int(set_time[3:5]) > 59:
            messagebox.showinfo('Error', "Incorrect minutes, try again")
        elif int(set_time[6:8]) > 59:
            messagebox.showinfo('Error', "Incorrect seconds, try again")
        else:
            while True:
                now = datetime.now().strftime("%H:%M:%S")
                if now == set_time:
                    if melody.get() == 'laugh':
                        playsound('laugh.mp3')
                    elif melody.get() == 'funny':
                        playsound('funny.mp3')
                    messagebox.showinfo('Alarm', "Wake up!")
                    break


def alarm_time():
    set_time = f"{hour.get()}:{mins.get()}:{sec.get()}"
    print(f"Alarm time  {set_time}...")
    alarm(set_time)


window = Tk()
window.geometry("600x400")
window.resizable(0, 0)
window.title(str(datetime.now()))

hour = StringVar()
mins = StringVar()
sec = StringVar()
alarm_label = Label(window, text='Alarm time HH:MM:SS', fg="red", font='arial 22 bold').pack()
alarm_t = Label(window, text="Hour        Minutes     Seconds", font='arial 12 bold').place(x=210, y=60)
Entry(window, textvariable=hour, bg="yellow", width=10).place(x=205, y=100)
Entry(window, textvariable=mins, bg="yellow", width=10).place(x=285, y=100)
Entry(window, textvariable=sec, bg="yellow", width=10).place(x=365, y=100)
mus = Label(window, text="Select the sound", font='arial 12 bold').place(x=250, y=150)
music = ['funny', 'laugh']
melody = StringVar(value=music[0])
combobox = Combobox(values=music, textvariable=melody).place(x=250, y=180)
button = Button(window, text="Set the alarm", fg="red", command=alarm_time).place(x=280, y=250)
window.mainloop()
